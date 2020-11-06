hostname ${node.name}
password ${node.password}

% if node.ospfd.logfile:
log file ${node.ospfd.logfile}
% endif

% for section in node.ospfd.debug:
debug ospf ${section}
% endfor

% for intf in node.ospfd.interfaces:
interface ${intf.name}
# ${intf.description}
  # Highest priority routers will be DR
  ip ospf priority ${intf.priority}
  ip ospf cost ${intf.cost}
  % if not intf.passive and intf.active:
  ip ospf dead-interval ${intf.dead_int}
  ip ospf hello-interval ${intf.hello_int}
  % endif
  ip ospf authentication message-digest
  ip ospf message-digest-key 42 md5 my_string_authkey
  <%block name="interface"/>
!
% endfor

router ospf
  ospf router-id ${node.ospfd.routerid}
  % for r in node.ospfd.redistribute:
  redistribute ${r.subtype} metric-type ${r.metric_type} metric ${r.metric}
  % endfor
  % for net in node.ospfd.networks:
  network ${net.domain.with_prefixlen} area ${net.area}
  % endfor
  % for itf in node.ospfd.interfaces:
      % if itf.passive or not itf.active:
  passive-interface ${itf.name}
    % endif
  % endfor
  area 0.0.0.0 authentication message-digest
  
  % if ${node.name} == "r_bhs2" or ${node.name} == "r_gra2":
  network 172.31.255.124/32 area ${net.area}
  % endif
  mpls-te on
  mpls-te router-address ${node.ospfd.routerid}
  
  capability opaque
  segment-routing on
  segment-routing global-block 10000 19999
  segment-routing local-block 5000 5999
  segment-routing node-msd 8
  segment-routing prefix 127.0.0.1/32
  <%block name="router"/>
!
