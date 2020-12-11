
LINK_PARAMS = {
    # LINKS params of the relation Router-HOST
    'rr1_lon1,h1_lon': {'params1': {'ip': ('100.42.141.1/30', 'cafe:da7a:141::1/120')},
                        'params2': {'ip': ('100.42.141.2/30', 'cafe:da7a:141::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20},
    'r_gra1,h1_gra': {'params1': {'ip': ('100.42.142.1/30', 'cafe:da7a:142::1/120')},
                      'params2': {'ip': ('100.42.142.2/30', 'cafe:da7a:142::2/120')},
                      'ospf_hello_int':  5,
                      'ospf_dead_int':  20,
                      'ospf6_hello_int':  5,
                      'ospf6_dead_int':  20},
    'r_rbx1,h1_rbx': {'params1': {'ip': ('100.42.144.1/30', 'cafe:da7a:144::1/120')},
                      'params2': {'ip': ('100.42.144.2/30', 'cafe:da7a:144::2/120')},
                      'ospf_hello_int':  5,
                      'ospf_dead_int':  20,
                      'ospf6_hello_int':  5,
                      'ospf6_dead_int':  20},
    'rr2_par1,h1_par': {'params1': {'ip': ('100.42.145.1/30', 'cafe:da7a:145::1/120')},
                        'params2': {'ip': ('100.42.145.2/30', 'cafe:da7a:145::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20},
    'r_ymq1,h1_ymq': {'params1': {'ip': ('100.42.240.1/30', 'cafe:da7a:240::1/120')},
                      'params2': {'ip': ('100.42.240.2/30', 'cafe:da7a:240::2/120')},
                      'ospf_hello_int':  5,
                      'ospf_dead_int':  20,
                      'ospf6_hello_int':  5,
                      'ospf6_dead_int':  20},  # minimal hello-multiplier 4
    'rr2_bhs1,h1_bhs': {'params1': {'ip': ('100.42.241.1/30', 'cafe:da7a:241::1/120')},
                        'params2': {'ip': ('100.42.241.2/30', 'cafe:da7a:241::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20},
    'rr1_nwk1,h1_nwk': {'params1': {'ip': ('100.42.242.1/30', 'cafe:da7a:242::1/120')},
                        'params2': {'ip': ('100.42.242.2/30', 'cafe:da7a:242::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20},
    # LINKS params of the relation Router-Router
    'rr1_lon2,rr1_nwk2': {'params1': {'ip': ('100.42.1.1/30', 'cafe:da7a:1::1/120')},
                          'params2': {'ip': ('100.42.1.2/30', 'cafe:da7a:1::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 20},
    'rr1_lon1,rr1_nwk1': {'params1': {'ip': ('100.42.2.1/30', 'cafe:da7a:2::1/120')},
                          'params2': {'ip': ('100.42.2.2/30', 'cafe:da7a:2::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 20},

    'rr1_lon1,rr1_lon2': {'params1': {'ip': ('100.42.120.1/30', 'cafe:da7a:120::1/120')},
                          'params2': {'ip': ('100.42.120.2/30', 'cafe:da7a:120::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20},
    'rr1_lon1,r_gra1': {'params1': {'ip': ('100.42.101.1/30', 'cafe:da7a:101::1/120')},
                        'params2': {'ip': ('100.42.101.2/30', 'cafe:da7a:101::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20,
                        'igp_metric': 4},
    'rr1_lon1,r_rbx1': {'params1': {'ip': ('100.42.102.1/30', 'cafe:da7a:102::1/120')},
                        'params2': {'ip': ('100.42.102.2/30', 'cafe:da7a:102::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'igp_metric': 6},
    'rr1_lon2,r_gra2': {'params1': {'ip': ('100.42.103.1/30', 'cafe:da7a:103::1/120')},
                        'params2': {'ip': ('100.42.103.2/30', 'cafe:da7a:103::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'igp_metric': 4},
    'r_gra1,rr2_par1': {'params1': {'ip': ('100.42.104.1/30', 'cafe:da7a:104::1/120')},
                        'params2': {'ip': ('100.42.104.2/30', 'cafe:da7a:104::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20,
                        'igp_metric': 3},
    'r_rbx1,rr2_par1': {'params1': {'ip': ('100.42.105.1/30', 'cafe:da7a:105::1/120')},
                        'params2': {'ip': ('100.42.105.2/30', 'cafe:da7a:105::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20,
                        'igp_metric': 5},
    'rr1_lon2,r_rbx2': {'params1': {'ip': ('100.42.106.1/30', 'cafe:da7a:106::1/120')},
                        'params2': {'ip': ('100.42.106.2/30', 'cafe:da7a:106::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'igp_metric': 6},
    'r_gra2,rr2_par2': {'params1': {'ip': ('100.42.107.1/30', 'cafe:da7a:107::1/120')},
                        'params2': {'ip': ('100.42.107.2/30', 'cafe:da7a:107::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'igp_metric': 3},
    'r_rbx2,rr2_par2': {'params1': {'ip': ('100.42.108.1/30', 'cafe:da7a:108::1/120')},
                        'params2': {'ip': ('100.42.108.2/30', 'cafe:da7a:108::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20,
                        'igp_metric': 5},
    'r_gra1,r_gra2': {'params1': {'ip': ('100.42.121.1/30', 'cafe:da7a:121::1/120')},
                      'params2': {'ip': ('100.42.121.2/30', 'cafe:da7a:121::2/120')},
                      'ospf_hello_int':  5,
                      'ospf_dead_int':  20,
                      'ospf6_hello_int':  5,
                      'ospf6_dead_int':  20},
    'r_rbx1,r_rbx2': {'params1': {'ip': ('100.42.122.1/30', 'cafe:da7a:122::1/120')},
                      'params2': {'ip': ('100.42.122.2/30', 'cafe:da7a:122::2/120')},
                      'ospf_hello_int':  5,
                      'ospf_dead_int':  20,
                      'ospf6_hello_int':  5,
                      'ospf6_dead_int':  20},
    'rr2_par1,rr2_par2': {'params1': {'ip': ('100.42.123.1/30', 'cafe:da7a:123::1/120')},
                          'params2': {'ip': ('100.42.123.2/30', 'cafe:da7a:123::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20},

    'rr1_nwk1,rr2_bhs1': {'params1': {'ip': ('100.42.201.1/30', 'cafe:da7a:201::1/120')},
                          'params2': {'ip': ('100.42.201.2/30', 'cafe:da7a:201::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 10},
    'rr2_bhs2,r_ymq1': {'params1': {'ip': ('100.42.202.1/30', 'cafe:da7a:202::1/120')},
                        'params2': {'ip': ('100.42.202.2/30', 'cafe:da7a:202::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20,
                        'igp_metric': 2},
    'rr1_nwk2,rr2_bhs2': {'params1': {'ip': ('100.42.203.1/30', 'cafe:da7a:203::1/120')},
                          'params2': {'ip': ('100.42.203.2/30', 'cafe:da7a:203::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 10},
    'rr2_bhs1,r_ymq1': {'params1': {'ip': ('100.42.204.1/30', 'cafe:da7a:204::1/120')},
                        'params2': {'ip': ('100.42.204.2/30', 'cafe:da7a:204::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20,
                        'igp_metric': 2},
    'rr1_nwk1,rr1_nwk2': {'params1': {'ip': ('100.42.220.1/30', 'cafe:da7a:220::1/120')},
                          'params2': {'ip': ('100.42.220.2/30', 'cafe:da7a:220::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20},
    'rr2_bhs1,rr2_bhs2': {'params1': {'ip': ('100.42.221.1/30', 'cafe:da7a:221::1/120')},
                          'params2': {'ip': ('100.42.221.2/30', 'cafe:da7a:221::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20},

    # LINKS params of the relation Router-eRouter
    # For host
    'r_cogent,h1_cogent': {"params1": {"ip": ("100.43.101.1/30", "cafe:3:1::1/120")},
                           "params2": {"ip": ("100.43.101.2/30", "cafe:3:1::2/120")},
                           'ospf_hello_int':  5,
                           'ospf_dead_int':  20,
                           'ospf6_hello_int':  5,
                           'ospf6_dead_int':  20,
                           "igp_metric": 1},
    'r_level3,h1_level3': {"params1": {"ip": ("100.44.101.1/30", "cafe:4:1::1/120")},
                           "params2": {"ip": ("100.44.101.2/30", "cafe:4:1::2/120")},
                           'ospf_hello_int':  5,
                           'ospf_dead_int':  20,
                           'ospf6_hello_int':  5,
                           'ospf6_dead_int':  20,
                           "igp_metric": 1},
    'r_telia,h1_telia': {"params1": {"ip": ("100.45.101.1/30", "cafe:5:1::1/120")},
                         "params2": {"ip": ("100.45.101.2/30", "cafe:5:1::2/120")},
                         'ospf_hello_int':  5,
                         'ospf_dead_int':  20,
                         'ospf6_hello_int':  5,
                         'ospf6_dead_int':  20,
                         "igp_metric": 1},
    'r_google,h1_google': {"params1": {"ip": ("100.46.101.1/30", "cafe:6:1::1/120")},
                           "params2": {"ip": ("100.46.101.2/30", "cafe:6:1::2/120")},
                           'ospf_hello_int':  5,
                           'ospf_dead_int':  20,
                           'ospf6_hello_int':  5,
                           'ospf6_dead_int':  20,
                           "igp_metric": 1},
    'r_amazon,h1_amazon': {"params1": {"ip": ("100.47.101.1/30", "cafe:7:1::1/120")},
                           "params2": {"ip": ("100.47.101.2/30", "cafe:7:1::2/120")},
                           'ospf_hello_int':  5,
                           'ospf_dead_int':  20,
                           'ospf6_hello_int':  5,
                           'ospf6_dead_int':  20,
                           "igp_metric": 1},
    # For router
    'rr1_nwk1,r_cogent': {'params1': {'ip': ('100.42.245.1/30', 'cafe:da7a:245::1/120')},
                          'params2': {'ip': ('100.42.245.2/30', 'cafe:da7a:245::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 1},
    'rr1_nwk2,r_cogent': {'params1': {'ip': ('100.42.246.1/30', 'cafe:da7a:246::1/120')},
                          'params2': {'ip': ('100.42.246.2/30', 'cafe:da7a:246::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 1},
    'rr1_lon1,r_cogent': {'params1': {'ip': ('100.42.247.1/30', 'cafe:da7a:247::1/120')},
                          'params2': {'ip': ('100.42.247.2/30', 'cafe:da7a:247::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 1},
    'rr1_nwk1,r_level3': {'params1': {'ip': ('100.42.248.1/30', 'cafe:da7a:248::1/120')},
                          'params2': {'ip': ('100.42.248.2/30', 'cafe:da7a:248::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 1},
    'rr1_nwk2,r_level3': {'params1': {'ip': ('100.42.249.1/30', 'cafe:da7a:249::1/120')},
                          'params2': {'ip': ('100.42.249.2/30', 'cafe:da7a:249::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 1},
    'rr1_lon1,r_level3': {'params1': {'ip': ('100.42.250.1/30', 'cafe:da7a:250::1/120')},
                          'params2': {'ip': ('100.42.250.2/30', 'cafe:da7a:250::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 1},
    'rr1_nwk1,r_telia': {'params1': {'ip': ('100.42.251.1/30', 'cafe:da7a:251::1/120')},
                         'params2': {'ip': ('100.42.251.2/30', 'cafe:da7a:251::2/120')},
                         'ospf_hello_int':  5,
                         'ospf_dead_int':  20,
                         'ospf6_hello_int':  5,
                         'ospf6_dead_int':  20,
                         'igp_metric': 1},
    'rr1_nwk2,r_telia': {'params1': {'ip': ('100.42.252.1/30', 'cafe:da7a:252::1/120')},
                         'params2': {'ip': ('100.42.252.2/30', 'cafe:da7a:252::2/120')},
                         'ospf_hello_int':  5,
                         'ospf_dead_int':  20,
                         'ospf6_hello_int':  5,
                         'ospf6_dead_int':  20,
                         'igp_metric': 1},
    'rr1_lon1,r_telia': {'params1': {'ip': ('100.42.253.1/30', 'cafe:da7a:253::1/120')},
                         'params2': {'ip': ('100.42.253.2/30', 'cafe:da7a:253::2/120')},
                         'ospf_hello_int':  5,
                         'ospf_dead_int':  20,
                         'ospf6_hello_int':  5,
                         'ospf6_dead_int':  20,
                         'igp_metric': 1},
    'rr1_lon1,r_amazon': {'params1': {'ip': ('100.42.254.1/30', 'cafe:da7a:254::1/120')},
                          'params2': {'ip': ('100.42.254.2/30', 'cafe:da7a:254::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 1},
    'rr2_par1,r_cogent': {'params1': {'ip': ('100.42.255.1/30', 'cafe:da7a:255::1/120')},
                          'params2': {'ip': ('100.42.255.2/30', 'cafe:da7a:255::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 1},
    'rr2_par2,r_amazon': {'params1': {'ip': ('100.42.234.1/30', 'cafe:da7a:234::1/120')},
                          'params2': {'ip': ('100.42.234.2/30', 'cafe:da7a:234::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 1},
    'rr2_par1,r_level3': {'params1': {'ip': ('100.42.235.1/30', 'cafe:da7a:235::1/120')},
                          'params2': {'ip': ('100.42.235.2/30', 'cafe:da7a:235::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 1},
    'rr2_par1,r_google': {'params1': {'ip': ('100.42.236.1/30', 'cafe:da7a:236::1/120')},
                          'params2': {'ip': ('100.42.236.2/30', 'cafe:da7a:236::2/120')},
                          'ospf_hello_int':  5,
                          'ospf_dead_int':  20,
                          'ospf6_hello_int':  5,
                          'ospf6_dead_int':  20,
                          'igp_metric': 1},
    'r_ymq1,r_amazon': {'params1': {'ip': ('100.42.237.1/30', 'cafe:da7a:237::1/120')},
                        'params2': {'ip': ('100.42.237.2/30', 'cafe:da7a:237::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20,
                        'igp_metric': 1},
    'r_ymq1,r_google': {'params1': {'ip': ('100.42.238.1/30', 'cafe:da7a:238::1/120')},
                        'params2': {'ip': ('100.42.238.2/30', 'cafe:da7a:238::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20,
                        'igp_metric': 1},
    # For anycast
    'rr2_bhs2,r_any1': {'params1': {'ip': ('100.42.239.1/30', 'cafe:da7a:239::1/120')},
                        'params2': {'ip': ('100.42.239.2/30', 'cafe:da7a:239::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20,
                        'igp_metric': 1},
    'rr2_bhs1,r_any1': {'params1': {'ip': ('100.42.232.1/30', 'cafe:da7a:232::1/120')},
                        'params2': {'ip': ('100.42.232.2/30', 'cafe:da7a:232::2/120')},
                        'ospf_hello_int':  5,
                        'ospf_dead_int':  20,
                        'ospf6_hello_int':  5,
                        'ospf6_dead_int':  20,
                        'igp_metric': 5},
    'r_gra2,r_any2': {'params1': {'ip': ('100.42.143.1/30', 'cafe:da7a:143::1/120')},
                      'params2': {'ip': ('100.42.143.2/30', 'cafe:da7a:143::2/120')},
                      'ospf_hello_int':  5,
                      'ospf_dead_int':  20,
                      'ospf6_hello_int':  5,
                      'ospf6_dead_int':  20,
                      'igp_metric': 1},
    'r_gra1,r_any2': {'params1': {'ip': ('100.42.147.1/30', 'cafe:da7a:147::1/120')},
                      'params2': {'ip': ('100.42.147.2/30', 'cafe:da7a:147::2/120')},
                      'ospf_hello_int':  5,
                      'ospf_dead_int':  20,
                      'ospf6_hello_int':  5,
                      'ospf6_dead_int':  20,
                      'igp_metric': 5},
    'r_any1,serv1_any': {'params1': {'ip': ('100.42.233.1/30', 'cafe:da7a:233::1/120')},
                         'params2': {'ip': ('100.42.233.2/30', 'cafe:da7a:233::2/120')},
                         'ospf_hello_int':  5,
                         'ospf_dead_int':  20,
                         'ospf6_hello_int':  5,
                         'ospf6_dead_int':  20,
                         'igp_metric': 1,
                         'igp_area': '1.1.1.1'},
    'r_any2,serv2_any': {'params1': {'ip': ('100.42.146.1/30', 'cafe:da7a:146::1/120')},
                         'params2': {'ip': ('100.42.146.2/30', 'cafe:da7a:146::2/120')},
                         'ospf_hello_int':  5,
                         'ospf_dead_int':  20,
                         'ospf6_hello_int':  5,
                         'ospf6_dead_int':  20,
                         'igp_metric': 1,
                         'igp_area': '2.2.2.2'}
}