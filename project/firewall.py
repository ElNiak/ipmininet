from ipmininet.router.config.iptables import Rule,ChainRule

# https://www.sans.org/media/score/checklists/FirewallChecklist.pdf
# https://javapipe.com/blog/iptables-ddos-protection/
# https://unix.stackexchange.com/questions/205867/viewing-all-iptables-rules

def port_restriction(routerInterface):
    rules = []
    # port_restriction
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 22 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 21 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 23 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 53 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p udp --dport 69 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 87 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p udp --dport 111 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 111 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --match multiport --dport 512:514 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 515 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 540 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p udp --dport 2000 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 2000 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p udp --dport 2049 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 2049 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p udp --match multiport --dport 6000:6255 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --match multiport --dport 6000:6255 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p udp --match multiport --dport 0:20 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --match multiport --dport 0:20 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p udp --dport 37 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 37 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --match multiport --dport 109:110 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 143 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 8000 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 8080 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A INPUT -i {}-eth{} -p tcp --dport 8888 -j DROP".format(routerInterface[0], routerInterface[1]))]

    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 179 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 22 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 21 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 23 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 53 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p udp --dport 69 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 87 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p udp --dport 111 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 111 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --match multiport --dport 512:514 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 515 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 540 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p udp --dport 2000 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 2000 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p udp --dport 2049 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 2049 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p udp --match multiport --dport 6000:6255 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --match multiport --dport 6000:6255 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p udp --match multiport --dport 0:20 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --match multiport --dport 0:20 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p udp --dport 37 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 37 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --match multiport --dport 109:110 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 143 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 8000 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 8080 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A FORWARD -i {}-eth{} -p tcp --dport 8888 -j DROP".format(routerInterface[0], routerInterface[1]))]

    # no_external_ospf  # Redudant with passive interface but more secure
    rules += [Rule("-A INPUT -i {}-eth{} -p 89 -j DROP".format(routerInterface[0], routerInterface[1]))]
    rules += [Rule("-A OUTPUT -o {}-eth{} -p 89 -j DROP".format(routerInterface[0], routerInterface[1]))]

    return rules

#https://javapipe.com/blog/iptables-ddos-protection/
def port_restriction_cmd(routerInterface):
    rules = []

    #Block New Packets That Are Not SYN
    rules += ["iptables -t mangle -A PREROUTING -p tcp ! --syn -m conntrack --ctstate NEW -j DROP"]
    rules += ["ip6tables -t mangle -A PREROUTING -p tcp ! --syn -m conntrack --ctstate NEW -j DROP"]

    #Block Uncommon MSS Values
    rules += ["iptables -t mangle -A PREROUTING -p tcp -m conntrack --ctstate NEW -m tcpmss ! --mss 536:65535 -j DROP"]
    rules += ["ip6tables -t mangle -A PREROUTING -p tcp -m conntrack --ctstate NEW -m tcpmss ! --mss 536:65535 -j DROP"]

    #Block Packets With Bogus TCP Flags: blocks packets that use bogus TCP flags, ie. TCP flags that legitimate packets wouldn’t use.
    rules += ["iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN FIN,SYN -j DROP"]
    rules += ["ip6tables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN FIN,SYN -j DROP"]

    rules += ["iptables -t mangle -A PREROUTING -p tcp --tcp-flags SYN,RST SYN,RST -j DROP"]
    rules += ["ip6tables -t mangle -A PREROUTING -p tcp --tcp-flags SYN,RST SYN,RST -j DROP"]

    rules += ["iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,RST FIN,RST -j DROP"]
    rules += ["ip6tables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,RST FIN,RST -j DROP"]

    rules += ["iptables  -t mangle -A PREROUTING -p tcp --tcp-flags FIN,ACK FIN -j DROP"]
    rules += ["ip6tables  -t mangle -A PREROUTING -p tcp --tcp-flags FIN,ACK FIN -j DROP"]

    rules += ["iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,URG URG -j DROP"]
    rules += ["ip6tables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,URG URG -j DROP"]

    rules += ["iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,PSH PSH -j DROP"]
    rules += ["ip6tables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,PSH PSH -j DROP"]

    rules += ["iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL NONE -j DROP"]
    rules += ["ip6tables -t mangle -A PREROUTING -p tcp --tcp-flags ALL NONE -j DROP"]
    return rules


ip6_rules = {
    # https://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml
    "anti_spoofing": [
        # reserved by IANA for Unique Local Addresses (ULA)
        Rule("-A INPUT -s fc00::/7 -j DROP"),
        Rule("-A INPUT -d fc00::/7 -j DROP"),
        Rule("-A INPUT -s fd00::/8 -j DROP"),
        Rule("-A INPUT -d fd00::/8 -j DROP"),
        # reserved by IANA for Unique Local Addresses (ULA)
        Rule("-A OUTPUT -s fc00::/7 -j DROP"),
        Rule("-A OUTPUT -d fc00::/7 -j DROP"),
        Rule("-A OUTPUT -s fd00::/8 -j DROP"),
        Rule("-A OUTPUT -d fd00::/8 -j DROP"),
        # reserved by IANA for Unique Local Addresses (ULA)
        Rule("-A FORWARD -s fc00::/7 -j DROP"),
        Rule("-A FORWARD -d fc00::/7 -j DROP"),
        Rule("-A FORWARD -s fd00::/8 -j DROP"),
        Rule("-A FORWARD -d fd00::/8 -j DROP")
    ],
    "allow_http_to_public": [
        Rule("-A INPUT -p tcp -m tcp --dport 80 -j ACCEPT"),
        Rule("-A INPUT -p tcp -m tcp --dport 443 -j ACCEPT")
    ],
    "global_unical_address": [
        Rule("-A INPUT -s 2000::/3 -j DROP"),
        Rule("-A INPUT -d 2000::/3 -j DROP"),
        Rule("-A OUTPUT -s 2000::/3 -j DROP"),
        Rule("-A OUTPUT -d 2000::/3 -j DROP")
    ],
    "no_benchmarking": [
        Rule("-A INPUT -s 2001:2::/48 -j DROP"),
        Rule("-A INPUT -d 2001:2::/48 -j DROP"),
        Rule("-A OUTPUT -s 2001:2::/48 -j DROP"),
        Rule("-A OUTPUT -d 2001:2::/48 -j DROP")
    ],
    "limit_con": [
        Rule("-A INPUT -p tcp -m connlimit --connlimit-above 80 -j REJECT --reject-with tcp-reset")
    ],
    "limit_tcp_per_client": [
        Rule("-A INPUT -p tcp -m conntrack --ctstate NEW -m limit --limit 60/s --limit-burst 20 -j ACCEPT"),
        Rule("-A INPUT -p tcp -m conntrack --ctstate NEW -j DROP")
    ],
    "loopback_spoofing":[ #https://www.ellipsix.net/geninfo/firewall/iptables/index.html
        Rule("-A INPUT -s ::1/128 -i ! lo -j DROP"),
        Rule("-A INPUT -d ::1/128 -i ! lo -j DROP"),
        Rule("-A OUTPUT -s ::1/128 -o ! lo -j DROP"),
        Rule("-A OUTPUT -d ::1/128 -o ! lo -j DROP")
    ]
}
ip4_rules = {
    # https://www.iana.org/assignments/ipv4-address-space/ipv4-address-space.xhtml
    "anti_spoofing": [
        Rule("-A INPUT -s 10.0.0.0/8 -j DROP"),
        Rule("-A INPUT -d 10.0.0.0/8 -j DROP"),
        Rule("-A INPUT -s 172.16.0.0/12 -j DROP"),
        Rule("-A INPUT -d 172.16.0.0/12 -j DROP"),
        Rule("-A INPUT -s 192.168.0.0/16 -j DROP"),
        Rule("-A INPUT -d 192.168.0.0/16 -j DROP"),
        Rule("-A INPUT -s 240.0.0.0 -j DROP"),
        Rule("-A INPUT -d 240.0.0.0 -j DROP"),
        Rule("-A INPUT -s 0.0.0.0 -j DROP"),
        Rule("-A INPUT -d 0.0.0.0 -j DROP"),

        Rule("-A OUTPUT -s 10.0.0.0/8 -j DROP"),
        Rule("-A OUTPUT -d 10.0.0.0/8 -j DROP"),
        Rule("-A OUTPUT -s 172.16.0.0/12 -j DROP"),
        Rule("-A OUTPUT -d 172.16.0.0/12 -j DROP"),
        Rule("-A OUTPUT -s 192.168.0.0/16 -j DROP"),
        Rule("-A OUTPUT -d 192.168.0.0/16 -j DROP"),
        Rule("-A OUTPUT -s 240.0.0.0 -j DROP"),
        Rule("-A OUTPUT -d 240.0.0.0 -j DROP"),
        Rule("-A OUTPUT -s 0.0.0.0 -j DROP"),
        Rule("-A OUTPUT -d 0.0.0.0 -j DROP"),

        Rule("-A FORWARD -s 10.0.0.0/8 -j DROP"),
        Rule("-A FORWARD -d 10.0.0.0/8 -j DROP"),
        Rule("-A FORWARD -s 172.16.0.0/12 -j DROP"),
        Rule("-A FORWARD -d 172.16.0.0/12 -j DROP"),
        Rule("-A FORWARD -s 192.168.0.0/16 -j DROP"),
        Rule("-A FORWARD -d 192.168.0.0/16 -j DROP"),
        Rule("-A FORWARD -s 240.0.0.0 -j DROP"),
        Rule("-A FORWARD -d 240.0.0.0 -j DROP"),
        Rule("-A FORWARD -s 0.0.0.0 -j DROP"),
        Rule("-A FORWARD -d 0.0.0.0 -j DROP"),
    ],
    "allow_http_to_public": [
        Rule("-A FORWARD -p tcp -m tcp --dport 80 -j ACCEPT"),
        Rule("-A FORWARD -p tcp -m tcp --dport 443 -j ACCEPT")
    ],
    "no_external_hsrp": [  # Cisco protocol => needed ? More security better than nothing
        Rule("-A INPUT -s 224.0.0.2 -p udp --dport 1985 -j DROP"),
        Rule("-A OUTPUT -s 224.0.0.2 -p udp --dport 1985 -j DROP"),
        Rule("-A INPUT -d 224.0.0.2 -p udp --dport 1985 -j DROP"),
        Rule("-A OUTPUT -d 224.0.0.2 -p udp --dport 1985 -j DROP"),

        Rule("-A FORWARD -s 224.0.0.2 -p udp --dport 1985 -j DROP"),
        Rule("-A FORWARD -d 224.0.0.2 -p udp --dport 1985 -j DROP")
    ],
    "no_benchmarking": [
        Rule("-A INPUT -s 198.18.0.0/15 -j DROP"),
        Rule("-A INPUT -d 198.18.0.0/15 -j DROP"),
        Rule("-A OUTPUT -s 198.18.0.0/15 -j DROP"),
        Rule("-A OUTPUT -d 198.18.0.0/15 -j DROP")
    ],
    "limit_con": [
        Rule("-A INPUT -p tcp -m connlimit --connlimit-above 80 -j REJECT --reject-with tcp-reset")
    ],
    "limit_tcp_per_client": [
        Rule("-A INPUT -p tcp -m conntrack --ctstate NEW -m limit --limit 60/s --limit-burst 20 -j ACCEPT"),
        Rule("-A INPUT -p tcp -m conntrack --ctstate NEW -j DROP")
    ],
    "loopback_spoofing":[ #https://www.ellipsix.net/geninfo/firewall/iptables/index.html => not working
        Rule("-A INPUT -s 127.0.0.0/8 -i ! lo -j DROP"),
        Rule("-A INPUT -d 127.0.0.0/8 -i ! lo -j DROP"),
        Rule("-A OUTPUT -s 127.0.0.0/8 -o ! lo -j DROP"),
        Rule("-A OUTPUT -d 127.0.0.0/8 -o ! lo -j DROP")
    ]
}
