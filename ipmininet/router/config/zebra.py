import os
import socket
from ipaddress import IPv4Network, IPv6Network, ip_network
from typing import Optional, Union, Sequence, Tuple
from abc import abstractmethod, ABC
from .base import RouterDaemon
from .utils import ConfigDict

#  Route Map actions
DENY = 'deny'
PERMIT = 'permit'

def get_family(prefix: Union[str, IPv4Network, IPv6Network]) -> Optional[str]:
    pfx = ip_network(prefix) if isinstance(prefix, str) else prefix
    if pfx.version == 4:
        return 'ipv4'
    elif pfx.version == 6:
        return 'ipv6'

    return None
    
class QuaggaDaemon(RouterDaemon):
    """The base class for all Quagga-derived daemons"""

    # Additional parameters to pass when starting the daemon
    STARTUP_LINE_EXTRA = ''

    @property
    def startup_line(self):
        return '{name} -f {cfg} -i {pid} -z {api} -u root {extra}'\
                .format(name=self.NAME,
                        cfg=self.cfg_filename,
                        pid=self._file('pid'),
                        api=self.zebra_socket,
                        extra=self.STARTUP_LINE_EXTRA)

    @property
    def zebra_socket(self):
        """Return the path towards the zebra API socket for the given node"""
        return os.path.join(self._node.cwd,
                            '%s_%s.api' % ('quagga', self._node.name))

    def build(self):
        cfg = super().build()
        cfg.debug = self.options.debug
        return cfg

    def set_defaults(self, defaults):
        """:param debug: the set of debug events that should be logged"""
        defaults.debug = ()
        super().set_defaults(defaults)

    @property
    def dry_run(self):
        return '{name} -Cf {cfg} -u root'\
               .format(name=self.NAME,
                       cfg=self.cfg_filename)


class Zebra(QuaggaDaemon):
    NAME = 'zebra'
    PRIO = 0
    # We want zebra to preserve existing routes in the kernel RT (e.g. those
    # set via ip route)
    STARTUP_LINE_EXTRA = '-k'
    KILL_PATTERNS = (NAME,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.files.append(self.zebra_socket)

    def build(self):
        cfg = super().build()
        # Update with preset defaults
        cfg.update(self.options)
        # Track interfaces
        cfg.interfaces = (ConfigDict(name=itf.name,
                                     description=itf.describe)
                          for itf in self._node.intfList())
        return cfg

    def set_defaults(self, defaults):
        """:param debug: the set of debug events that should be logged
        :param access_lists: The set of AccessList to create, independently
                             from the ones already included by route_maps
        :param route_maps: The set of RouteMap to create"""
        defaults.access_lists = []
        defaults.route_maps = []
        super().set_defaults(defaults)

    def has_started(self):
        # We override this such that we wait until we have the API socket
        # and until wa can connect to it
        return os.path.exists(self.zebra_socket) and self.listening()

    def listening(self) -> bool:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            sock.connect(self.zebra_socket)
            sock.close()
            return True
        except socket.error:
            return False


class CommunityList:
    """A zebra community-list entry"""
    # Number of CmL
    count = 0

    def __init__(self, name: Optional[str] = None, action=PERMIT,
                 community: Union[int, str] = 0):
        """

        :param name:
        :param action:
        :param community:
        """
        CommunityList.count += 1
        self.name = name if name else 'cml%d' % CommunityList.count
        self.action = action
        self.community = community
        self.family = 'community'

    def __eq__(self, other):
        return self.name == other.name and self.action == other.action

class Entry:
    def __init__(self, prefix: Union[str, IPv4Network, IPv6Network],
                 action=PERMIT, family=None):
        """
        :param prefix: The ip_interface prefix for that ACL entry
        :param action: Whether that prefix belongs to the ACL (PERMIT)
                       or not (DENY)
        """

        if isinstance(prefix, str):
            if prefix == 'any':
                assert family is not None
                _prefix = prefix
            else:
                _prefix = ip_network(prefix)
                if family is not None:
                    assert get_family(_prefix) == family, "prefix family %s != family (%s)" % (get_family(_prefix), family)
        else:
            _prefix = prefix

        self.prefix = _prefix
        self.action = action
        self.family = family if family else get_family(self.prefix)
    
    @property
    def zebra_family(self):
        if self.family == 'ipv4':
            return 'ip'
        return 'ipv6'
    
        
class AccessListEntry(Entry):
    """A zebra access-list entry"""

    def __init__(self, prefix: Union[str, IPv4Network, IPv6Network], action=PERMIT, family=None):
        super().__init__(prefix, action, family)
        
class PrefixListEntry(Entry):
    def __init__(self, prefix: Union[str, IPv4Network, IPv6Network], action=PERMIT, family=None, le=None, ge=None):
        type_mask = {'ipv4': 32, 'ipv6': 128}

        super().__init__(prefix, action, family)

        # The 'any' prefix-list entry has a special action
        if self.prefix == 'any':
            self.prefix = ip_network("0.0.0.0/0") if self.family == 'ipv4' \
                else ip_network('::/0')
            self.le = type_mask[self.family]
            return

        if le is not None:
            assert 0 <= le <= type_mask[self.family], "assertion %d <= le (%d) <= %d failed" % (
            0, le, type_mask[self.family])
        if ge is not None:
            assert 0 <= ge <= type_mask[self.family], "assertion %d <= ge (%d) <= %d failed" % (
            0, ge, type_mask[self.family])
        if le is not None and ge is not None:
            assert le >= ge, "assertion le (%d) >= ge (%d) failed! le must be lower than ge" % (le, ge)

        self.le = le
        self.ge = ge
        

class ZebraList(ABC):
    count = 0

    @property
    @abstractmethod
    def prefix_name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def Entry(self):
        raise NotImplementedError

    def __init__(self, family, entries: Sequence[Union['ZebraList.Entry',
                                                       str, IPv4Network,
                                                       IPv6Network]] = (), name=None):
        assert family in {'ipv4', 'ipv6'}, "PrefixList unknown %s type. type must be either ipv4 or ipv6" % family

        ZebraList.count += 1

        self.name = name if name else '%s%d' % (self.prefix_name, ZebraList.count)
        self.entries = []
        for e in entries:
            if isinstance(e, self.Entry):
                assert e.family == family, "The prefix entry must be of the same type"
                self.entries.append(e)
            elif isinstance(e, str) and e == 'any':
                self.entries.append(self.Entry(prefix=e, family=family))
            elif isinstance(e, IPv4Network) or isinstance(e, IPv6Network) or isinstance(e, str):
                self.entries.append(self.Entry(prefix=e))
            else:
                raise ValueError('"%s" is not a valid prefix entry for the %s family' % (e, family))

        self.family = family

    def __eq__(self, other):
        return self.name == other.name


class AccessList(ZebraList):
    """A zebra access-list class. It contains a set of AccessListEntry,
    which describes all prefix belonging or not to this ACL"""

    @property
    def prefix_name(self):
        return 'acl'

    @property
    def Entry(self):
        return AccessListEntry

class PrefixList(ZebraList):
    @property
    def prefix_name(self):
        return 'pfxl'

    @property
    def Entry(self):
        return PrefixListEntry

class RouteMapMatchCond:
    """
    A class representing a RouteMap matching condition
    """

    def __init__(self, cond_type: str, condition, family=None):
        """
        :param condition: Can be an ip address, the id of an access
                          or prefix list
        :param cond_type: The type of condition access list, prefix list,
                          peer ...
        :param family: if cond_type is an access-list or a prefix-list,
                       specify the family of the list (either ipv4 or ipv6)
        """
        if family:
            assert family in {'ipv4', 'ipv6', 'community'}, "Unrecognized family type (%s)" % family
        self.condition = condition
        self.cond_type = cond_type
        self.family = family

    def __eq__(self, other):
        return self.condition == other.condition \
               and self.cond_type == other.cond_type \
               and self.family == other.family

class RouteMapSetAction:
    """
    A class representing a RouteMap set action
    """

    def __init__(self, action_type: str, value):
        """
        :param action_type: Type of value to me modified
        :param value: Value to be modified
        """
        self.action_type = action_type
        self.value = value

    def __eq__(self, other):
        return self.action_type == other.action_type \
               and self.value == other.value


class RouteMap:
    """A class representing a set of route maps applied to a given protocol"""

    # Number of route maps
    count = 0

    def __init__(self, name: Optional[str] = None, match_policy=PERMIT,
                 match_cond: Sequence[Union[RouteMapMatchCond, Tuple]] = (),
                 set_actions: Sequence[Union[RouteMapSetAction, Tuple]] = (),
                 call_action: Optional[str] = None,
                 exit_policy: Optional[str] = None, order=10,
                 proto: Sequence[str] = (), neighbor: Sequence = (),
                 direction='in',
                 family=None):
        """
        :param name: The name of the route-map, defaulting to rm##
        :param match_policy: Deny or permit the actions if the route match
                             the condition
        :param match_cond: Specify one or more conditions which must be matched
                           if the entry is to be considered further
        :param set_actions: Specify one or more actions to do
                            if there is a match
        :param call_action: call to an other route map
        :param exit_policy: An entry may, optionally specify an alternative exit
                            policy if the entry matched or of (action, [acl,
                            acl, ...]) tuples that will compose the route map
        :param order: Priority of the route map compare to others
        :param proto: The set of protocols to which this route-map applies
        :param neighbor: List of peers this route map is applied to
        :param direction: Direction of the routemap(in, out, both)
        """
        RouteMap.count += 1
        self.name = name if name else 'rm%d' % RouteMap.count
        self.match_policy = match_policy
        self.match_cond = [e if isinstance(e, RouteMapMatchCond)
                           else RouteMapMatchCond(cond_type=e[0],
                                                  condition=e[1])
                           for e in match_cond]
        self.set_actions = [e if isinstance(e, RouteMapSetAction)
                            else RouteMapSetAction(action_type=e[0], value=e[1])
                            for e in set_actions]
        self.call_action = call_action
        self.exit_policy = exit_policy
        self.neighbor = neighbor
        self.direction = direction
        self.order = order
        self.proto = proto
        self.family = family

    def __eq__(self, other):
        return self.neighbor == other.neighbor \
               and self.direction == other.direction \
               and self.exit_policy == other.exit_policy \
               and self.order == other.order \
                and self.family == other.family


    def append_match_cond(self, match_conditions):
        """

        :return:
        """
        for match_condition in match_conditions:
            if match_condition not in self.match_cond:
                self.match_cond.append(match_condition)

    def append_set_action(self, set_actions):
        """

        :param set_actions:
        :return:
        """
        for set_action in set_actions:
            if set_action not in self.set_actions:
                self.set_actions.append(set_action)

    @property
    def describe(self):
        """Return the zebra description of this route map and apply it to the
        relevant protocols"""
        return 'route-map'
