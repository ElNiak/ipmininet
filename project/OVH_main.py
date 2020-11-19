#!/usr/bin/env python3

from ipmininet.cli import IPCLI
from ipmininet.ipnet import IPNet
from ipmininet.iptopo import IPTopo
from ipmininet.router.config import (AF_INET, AF_INET6, BGP, OSPF, OSPF6,RIPng,
                                     SHARE, RouterConfig, bgp_fullmesh,
                                     ebgp_session, set_rr, AccessList, CLIENT_PROVIDER)
from ipmininet.router.config.zebra import AccessListEntry, CommunityList, PERMIT, DENY
from link_params import LINK_PARAMS

class OSPFNetOVH(IPTopo):

    def __init__(self, link_params={}, *args, **kwargs):
        '''
        :param ospf_params: Parameter to set on the OSPF deamon of routers
        :param link_params: Parameter to set on the links
        :param args:
        :param kwargs:
        '''
        self.link_params = link_params
        super().__init__( *args, **kwargs)

    def build(self, *args, **kwargs):
        
        ###########################################
        ###             HOST LANs               ###
        ###########################################

        lan_ovh_h1_lon = '100.42.141.0/24'
        lan_ovh_h1_gra = '100.42.142.0/24'
        lan_ovh_h1_rbx = '100.42.144.0/24'
        lan_ovh_h1_par = '100.42.145.0/24'
        lan_ovh_h1_ymq = '100.42.240.0/24'
        lan_ovh_h1_bhs = '100.42.241.0/24'
        lan_ovh_h1_nwk = '100.42.242.0/24'

        lan6_ovh_h1_lon = 'cafe:da7a:141::/64'
        lan6_ovh_h1_gra = 'cafe:da7a:142::/64'
        lan6_ovh_h1_rbx = 'cafe:da7a:144::/64'
        lan6_ovh_h1_par = 'cafe:da7a:145::/64'
        lan6_ovh_h1_ymq = 'cafe:da7a:240::/64' 
        lan6_ovh_h1_bhs = 'cafe:da7a:241::/64'
        lan6_ovh_h1_nwk = 'cafe:da7a:242::/64'
        
        
        lan_cogent_h1  = '100.43.101.0/24' 
        lan_level3_h1  = '100.44.101.0/24'
        lan_telia_h1   = '100.45.101.0/24'
        lan_google_h1  = '100.46.101.0/24'
        lan_amazon_h1  = '100.47.101.0/24'
        
        lan6_cogent_h1  = 'cafe:3:1::/64'
        lan6_level3_h1  = 'cafe:4:1::/64'
        lan6_telia_h1   = 'cafe:5:1::/64'
        lan6_google_h1  = 'cafe:6:1::/64'
        lan6_amazon_h1  = 'cafe:7:1::/64'

        ###########################################
        ###       Router loopback address       ###
        ###########################################

        loopback_address_r = { 
            'rr1_lon1':('100.42.10.1/32', 'cafe:da7a:10::/128'), 
            'rr1_lon2':('100.42.11.1/32', 'cafe:da7a:11::/128'), 
            'rr2_par1':('100.42.12.1/32', 'cafe:da7a:12::/128'), 
            'rr2_par2':('100.42.13.1/32', 'cafe:da7a:13::/128'),
            'r_gra1'  :('100.42.14.1/32', 'cafe:da7a:14::/128'), 
            'r_gra2'  :('100.42.15.1/32', 'cafe:da7a:15::/128'),  
            'r_rbx1'  :('100.42.16.1/32', 'cafe:da7a:16::/128'),
            'r_rbx2'  :('100.42.17.1/32', 'cafe:da7a:17::/128'), 

            'rr1_nwk1':('100.42.50.1/32', 'cafe:da7a:50::/128'), 
            'rr1_nwk2':('100.42.51.1/32', 'cafe:da7a:51::/128'),
            'r_ymq1'  :('100.42.52.3/32', 'cafe:da7a:52::/128'),
            'rr2_bhs1':('100.42.53.3/32', 'cafe:da7a:53::/128'), 
            'rr2_bhs2':('100.42.54.1/32', 'cafe:da7a:54::/128')
        }


        loopback_addres_foreign_r = {
            'r_cogent':('100.43.101.3/32','cafe:3:1::3/128'),
            'r_level3':('100.44.101.3/32','cafe:4:1::3/128'),
            'r_telia' :('100.45.101.3/32','cafe:5:1::3/128'),
            'r_google':('100.46.101.3/32','cafe:6:1::3/128'),
            'r_amazon':('100.47.101.3/32','cafe:7:1::3/128'),
        }


        ###########################################
        ###            Adding Router            ###
        ###########################################

        rr1_lon1  = self.addRouter('rr1_lon1', config=RouterConfig, lo_addresses=loopback_address_r['rr1_lon1']) 
        rr1_lon2  = self.addRouter('rr1_lon2', config=RouterConfig, lo_addresses=loopback_address_r['rr1_lon2']) 
        r_gra1    = self.addRouter('r_gra1',   config=RouterConfig, lo_addresses=loopback_address_r['r_gra1']) 
        r_gra2    = self.addRouter('r_gra2',   config=RouterConfig, lo_addresses=loopback_address_r['r_gra2']) 
        rr2_par1  = self.addRouter('rr2_par1', config=RouterConfig, lo_addresses=loopback_address_r['rr2_par1']) 
        rr2_par2  = self.addRouter('rr2_par2', config=RouterConfig, lo_addresses=loopback_address_r['rr2_par2']) 
        r_rbx1    = self.addRouter('r_rbx1',   config=RouterConfig, lo_addresses=loopback_address_r['r_rbx1']) 
        r_rbx2    = self.addRouter('r_rbx2',   config=RouterConfig, lo_addresses=loopback_address_r['r_rbx2']) 
        rr1_nwk1  = self.addRouter('rr1_nwk1', config=RouterConfig, lo_addresses=loopback_address_r['rr1_nwk1']) 
        rr1_nwk2  = self.addRouter('rr1_nwk2', config=RouterConfig, lo_addresses=loopback_address_r['rr1_nwk2']) 
        rr2_bhs1  = self.addRouter('rr2_bhs1', config=RouterConfig, lo_addresses=loopback_address_r['rr2_bhs1']) 
        rr2_bhs2  = self.addRouter('rr2_bhs2', config=RouterConfig, lo_addresses=loopback_address_r['rr2_bhs2']) 
        r_ymq1    = self.addRouter('r_ymq1',   config=RouterConfig, lo_addresses=loopback_address_r['r_ymq1']) 

        r_cogent = self.addRouter('r_cogent', config=RouterConfig, lo_addresses=loopback_addres_foreign_r['r_cogent']) 
        r_level3 = self.addRouter('r_level3', config=RouterConfig, lo_addresses=loopback_addres_foreign_r['r_level3']) 
        r_telia  = self.addRouter('r_telia',  config=RouterConfig, lo_addresses=loopback_addres_foreign_r['r_telia'])  
        r_google = self.addRouter('r_google', config=RouterConfig, lo_addresses=loopback_addres_foreign_r['r_google']) 
        r_amazon = self.addRouter('r_amazon', config=RouterConfig, lo_addresses=loopback_addres_foreign_r['r_amazon']) 

        
        routers = { 'rr1_lon1':rr1_lon1,
                    'rr1_lon2':rr1_lon2, 
                    'r_gra1'  :r_gra1, 
                    'r_gra2'  :r_gra2, 
                    'rr2_bhs1':rr2_bhs1, 
                    'rr2_bhs2':rr2_bhs2, 
                    'rr2_par1':rr2_par1, 
                    'rr2_par2':rr2_par2, 
                    'rr1_nwk1':rr1_nwk1, 
                    'rr1_nwk2':rr1_nwk2,
                    'r_rbx1'  :r_rbx1,
                    'r_rbx2'  :r_rbx2, 
                    'r_ymq1'  :r_ymq1                    
        }
        
        routers_extern = {
                    'r_cogent':[r_cogent,lan_cogent_h1,lan6_cogent_h1],
                    'r_level3':[r_level3,lan_level3_h1,lan6_level3_h1],
                    'r_telia' :[r_telia ,lan_telia_h1, lan6_telia_h1],
                    'r_google':[r_google,lan_google_h1,lan6_google_h1],
                    'r_amazon':[r_amazon,lan_amazon_h1,lan6_amazon_h1]
        }

        ###########################################
        ### Defining Anycast Server/Router      ###
        ###########################################
        #Anycast address
        lo6_any   = 'cafe:da7a:cafe:da7a::/128'
        lo4_any   = '100.42.42.42/32'
        serv1_any = self.addHost("serv1_any") #Note this host/server is only here to see the "ping"
        serv2_any = self.addHost("serv2_any")
        r_any1    = self.addRouter('r_any1', config=RouterConfig, lo_addresses=(lo4_any,lo6_any)) #Anycast address 
        r_any2    = self.addRouter('r_any2', config=RouterConfig, lo_addresses=(lo4_any,lo6_any)) 
        anycast_server = {
            'r_any1':r_any1,
            'r_any2':r_any2
        }

        ###########################################
        ###            Adding As                ###
        ###########################################
        
        self.addAS(16276, tuple(routers.values()) + (r_any2,r_any1))
        self.addAS(174,   (r_cogent,))
        self.addAS(3356,  (r_level3,))
        self.addAS(1299,  (r_telia,))
        self.addAS(15169, (r_google,))
        self.addAS(16509, (r_amazon,))

        ###########################################
        ###            Setup Daemon OVH         ###
        ###########################################

        europe_community_l1   = [rr1_nwk1, rr1_nwk2, rr1_lon1, rr1_lon2, rr2_par1,  rr2_par2]
        europe_community_l2   = [rr1_lon1, rr1_lon2, r_rbx1, r_rbx2,  r_gra1, r_gra2, rr2_par1, rr2_par2, r_any2]
        american_community_l1 = [rr1_nwk1, rr1_nwk2, rr2_bhs1,  rr2_bhs2, rr1_lon1, rr1_lon2]
        american_community_l2 = [rr1_nwk1, rr1_nwk2, rr2_bhs1,  rr2_bhs2,  r_ymq1, r_any1]
        
        family6 = AF_INET6(redistribute=['ospf6','connected'],)
        family4 = AF_INET( redistribute=['ospf','connected'],)
        network6=(lan6_ovh_h1_lon,lan6_ovh_h1_rbx,lan6_ovh_h1_par,lan6_ovh_h1_gra,lan6_ovh_h1_nwk,lan6_ovh_h1_bhs,lan6_ovh_h1_ymq,lo6_any,)
        network4=(lan_ovh_h1_lon,lan_ovh_h1_rbx,lan_ovh_h1_par,lan_ovh_h1_gra,lan_ovh_h1_nwk,lan_ovh_h1_bhs,lan_ovh_h1_ymq,lo4_any,)
        for k ,router in routers.items():
            router.addDaemon(OSPF)  
            router.addDaemon(OSPF6)
            if 'rr' in k:
                router.addDaemon(BGP,debug = ("neighbor",), 
                                    address_families=(AF_INET6(networks=network6, redistribute=['ospf6','connected']),  
                                                       AF_INET(networks=network4, redistribute=['ospf','connected']),)) 
            else:
                router.addDaemon(BGP,debug = ("neighbor",), 
                                    address_families=(family6, family4,)) 
            if 'rr1_lon' in k:                        #LEVEL 1 EU
                europe_community_l1.remove(router)
                set_rr(self, rr=router, peers=europe_community_l1)
                europe_community_l1.append(router)
            elif 'rr2_par' in k:                      #LEVEL 2 EU
                europe_community_l2.remove(router)
                set_rr(self, rr=router, peers=europe_community_l2)
                europe_community_l2.append(router)
            elif 'rr1_nwk' in k:                      #LEVEL 1 US
                american_community_l1.remove(router)
                set_rr(self, rr=router, peers=american_community_l1)
                american_community_l1.append(router)
            elif 'rr2_bhs' in k:                      #LEVEL 2 US
                american_community_l2.remove(router)
                set_rr(self, rr=router, peers=american_community_l2)
                american_community_l2.append(router)


        ###########################################
        ###   Setup Daemon external network     ###
        ###########################################

        for k, router in routers_extern.items():
            router[0].addDaemon(OSPF)
            router[0].addDaemon(OSPF6)
            router[0].addDaemon(BGP,debug = ("neighbor",), 
                                address_families=(AF_INET(networks=(router[1],),redistribute=['ospf','connected']), 
                                                 AF_INET6(networks=(router[2],),redistribute=['ospf6','connected']),))

        ###########################################
        ###        Setup Daemon Anycast         ###
        ###########################################

        for k, router in anycast_server.items():
            router.addDaemon(OSPF,  address_families=(family4,family6,))
            router.addDaemon(OSPF6, address_families=(family4,family6,))
            router.addDaemon(BGP,debug = ("neighbor",), 
                                 address_families=(AF_INET( networks=(lo4_any,),redistribute=['rip','ospf','connected']),
                                                   AF_INET6(networks=(lo6_any,),redistribute=['rip','ospf6','connected']),))

        ###########################################
        ###           Add Host                  ###
        ###########################################

        h1_lon = self.addHost('h1_lon') 
        h1_gra = self.addHost('h1_gra') 
        h1_rbx = self.addHost('h1_rbx') 
        h1_par = self.addHost('h1_par')
        h1_nwk = self.addHost('h1_nwk') 
        h1_bhs = self.addHost('h1_bhs') 
        h1_ymq = self.addHost('h1_ymq') 
        
        h1_cogent = self.addHost('h1_cogent') 
        h1_level3 = self.addHost('h1_level3') 
        h1_telia  = self.addHost('h1_telia')
        h1_google = self.addHost('h1_google')
        h1_amazon = self.addHost('h1_amazon') 
       
        ###########################################
        ###           Add Links                 ###
        ###########################################

        self.addLinks(
                     # ADD links between the routers and (hosts)
                    (rr1_lon1,rr1_lon2, self.link_params.get('rr1_lon1,rr1_lon2', {})), (rr1_lon1,r_gra1,  self.link_params.get('rr1_lon1,r_gra1', {})),    (rr1_lon1,rr1_nwk1, self.link_params.get('rr1_lon1,rr1_nwk1', {})), (rr1_lon1,r_rbx1, self.link_params.get('rr1_lon1,r_rbx1', {})), (rr1_lon1,h1_lon, self.link_params.get('rr1_lon1,h1_lon', {})),
                    (rr1_lon2,r_gra2,   self.link_params.get('rr1_lon2,r_gra2', {})),   (rr1_lon2,r_rbx2,  self.link_params.get('rr1_lon2,r_rbx2', {})),    (rr1_lon2,rr1_nwk2, self.link_params.get('rr1_lon2,rr1_nwk2', {})),
                    (r_gra1,r_gra2,     self.link_params.get('r_gra1,r_gra2', {})),     (r_gra1,rr2_par1,  self.link_params.get('r_gra1,rr2_par1', {})),    (r_gra1,h1_gra,     self.link_params.get('r_gra1,h1_gra', {})),
                    (r_gra2,rr2_par2,   self.link_params.get('r_gra2,rr2_par2', {})),
                    (r_rbx1,r_rbx2,     self.link_params.get('r_rbx1,r_rbx2', {})),     (r_rbx1,rr2_par1,  self.link_params.get('r_rbx1,rr2_par1', {})),    (r_rbx1,h1_rbx,     self.link_params.get('r_rbx1,h1_rbx', {})),
                    (r_rbx2,rr2_par2,   self.link_params.get('r_rbx2,rr2_par2', {})),
                    (rr2_par1,rr2_par2, self.link_params.get('rr2_par1,rr2_par2', {})), (rr2_par1,h1_par,  self.link_params.get('rr2_par1,h1_par', {})),
                    (rr1_nwk1,rr1_nwk2, self.link_params.get('rr1_nwk1,rr1_nwk2', {})), (rr1_nwk1,rr2_bhs1,self.link_params.get('rr1_nwk1,rr2_bhs1', {})),  (rr1_nwk1,h1_nwk,    self.link_params.get('rr1_nwk1,h1_nwk', {})),
                    (rr1_nwk2,rr2_bhs2, self.link_params.get('rr1_nwk2,rr2_bhs2', {})),
                    (rr2_bhs1,rr2_bhs2, self.link_params.get('rr2_bhs1,rr2_bhs2', {})), (rr2_bhs1,r_ymq1,  self.link_params.get('rr2_bhs1,r_ymq1', {})),    (rr2_bhs1,h1_bhs,   self.link_params.get('rr2_bhs1,h1_bhs', {})),
                    (rr2_bhs2,r_ymq1,   self.link_params.get('rr2_bhs2,r_ymq1', {})),
                    (r_ymq1,h1_ymq,     self.link_params.get('r_ymq1,h1_ymq', {}))
        )
        
        self.addLinks(
		            #For other AS 
                    (rr1_lon1,r_cogent,self.link_params.get('rr1_lon1,r_cogent', {})), (rr1_lon1,r_level3, self.link_params.get('rr1_lon1,r_level3', {})),(rr1_lon1,r_telia, self.link_params.get('rr1_lon1,r_telia', {})),(rr1_lon1,r_amazon,   self.link_params.get('rr1_lon1,r_amazon', {})),(r_cogent, h1_cogent,self.link_params.get('r_cogent,h1_cogent', {})),
                    (rr1_nwk1,r_cogent,self.link_params.get('rr1_nwk1,r_cogent', {})), (rr1_nwk1,r_level3, self.link_params.get('rr1_nwk1,r_level3', {})),(rr1_nwk1,r_telia, self.link_params.get('rr1_nwk1,r_telia', {})),(r_amazon, h1_amazon, self.link_params.get('r_amazon,h1_amazon', {})),
                    (rr1_nwk2,r_cogent,self.link_params.get('rr1_nwk2,r_cogent', {})), (rr1_nwk2,r_level3, self.link_params.get('rr1_nwk2,r_level3', {})),(rr1_nwk2,r_telia, self.link_params.get('rr1_nwk2,r_telia', {})),(r_telia, h1_telia,   self.link_params.get('r_telia,h1_telia', {})),
                    (rr2_par1,r_cogent,self.link_params.get('rr2_par1,r_cogent', {})), (rr2_par1,r_level3, self.link_params.get('rr2_par1,r_level3', {})),(rr2_par1,r_google,self.link_params.get('rr2_par1,r_google', {})),(r_google, h1_google,self.link_params.get('r_google,h1_google', {})),
                    (rr2_par2,r_amazon,self.link_params.get('rr2_par2,r_amazon', {})), (r_level3,h1_level3,self.link_params.get('r_level3,h1_level3', {})),
                    (r_ymq1,r_amazon,  self.link_params.get('r_ymq1,r_amazon', {})),   (r_ymq1,r_google,   self.link_params.get('r_ymq1,r_google', {}))
        )

        self.addLinks(
                    #For ANYCAST
		            (rr2_bhs2, r_any1, self.link_params.get('rr2_bhs2,r_any1', {})),  (r_gra2, r_any2,   self.link_params.get('r_gra2,r_any2', {})),
                    (r_any1, serv1_any,self.link_params.get('r_any1,serv1_any', {})), (r_any2, serv2_any,self.link_params.get('r_any2,serv2_any', {}))
        )

        ###########################################
        ###       Add ebg_session               ###
        ###########################################

        # BGP Session Cogent (Transit)
        ebgp_session(self, rr1_lon1, r_cogent)
        ebgp_session(self, rr1_nwk1, r_cogent)
        ebgp_session(self, rr1_nwk2, r_cogent)
        ebgp_session(self, rr2_par1, r_cogent)

        # EBGP Session Level3 (Transit)
        ebgp_session(self, rr1_lon1, r_level3)
        ebgp_session(self, rr1_nwk1, r_level3)
        ebgp_session(self, rr1_nwk2, r_level3)
        ebgp_session(self, rr2_par1, r_level3)

        #EBGP Session Telia (Transit)
        ebgp_session(self, rr1_lon1, r_telia)
        ebgp_session(self, rr1_nwk1, r_telia)
        ebgp_session(self, rr1_nwk2, r_telia)

        #EBGP Session Amazon (Stub)
        ebgp_session(self, rr1_lon1, r_amazon)
        ebgp_session(self, rr2_par2, r_amazon)
        ebgp_session(self, r_ymq1,   r_amazon)

        #EBGP Session Google (Stub)
        ebgp_session(self, rr2_par1, r_google)
        ebgp_session(self, r_ymq1,   r_google)
        

        ###########################################
        ###          Community  List            ###
        ###########################################

        all_al = AccessList('All', ('any',))
        
        peers_link = CommunityList(name='from-peers', community=1, action=PERMIT)
        up_link    = CommunityList(name='from-up', community=3, action=PERMIT)
        
        learnt_from_na = CommunityList(name='learnt_from_na', community=4001, action=PERMIT)
        learnt_from_eu = CommunityList(name='learnt_from_eu', community=4201, action=PERMIT)

        customer_default = CommunityList(name='customer-default', community=490, action=PERMIT)
        customer_backup  = CommunityList(name='customer-backup', community=480, action=PERMIT)
        
        prepend_all_1 = CommunityList(name='prepend_all_1', community=421, action=PERMIT)
        prepend_all_2 = CommunityList(name='prepend_all_2', community=422, action=PERMIT)
        prepend_all_3 = CommunityList(name='prepend_all_3', community=423, action=PERMIT)
        
        prepend_na_1 = CommunityList(name='prepend_na_1', community=4021, action=PERMIT)
        prepend_na_2 = CommunityList(name='prepend_na_2', community=4022, action=PERMIT)
        prepend_na_3 = CommunityList(name='prepend_na_3', community=4023, action=PERMIT)
        
        prepend_eu_1 = CommunityList(name='prepend_eu_1', community=4221, action=PERMIT)
        prepend_eu_2 = CommunityList(name='prepend_eu_2', community=4222, action=PERMIT)
        prepend_eu_3 = CommunityList(name='prepend_eu_3', community=4223, action=PERMIT)
        
        no_advertise_all = CommunityList(name='no_advertise_all', community=429, action=PERMIT)
        no_advertise_na  = CommunityList(name='no_advertise_na', community=4029, action=PERMIT)
        no_advertise_eu  = CommunityList(name='no_advertise_eu', community=4229, action=PERMIT)

        
        border_router_eu   = [(rr1_lon1,r_cogent, CLIENT_PROVIDER),(rr1_lon1,r_amazon, SHARE),(rr1_lon1,r_telia, CLIENT_PROVIDER), (rr1_lon1,r_level3, CLIENT_PROVIDER),
                              (rr2_par1, r_google, SHARE), (rr2_par1, r_cogent, CLIENT_PROVIDER), (rr2_par1, r_level3, CLIENT_PROVIDER),
                              (rr2_par2, r_amazon, SHARE)]
                              
        border_router_us   = [(r_ymq1,r_amazon, SHARE),(r_ymq1,r_google, SHARE),
                              (rr1_nwk1,r_cogent, CLIENT_PROVIDER), (rr1_nwk1,r_level3, CLIENT_PROVIDER),(rr1_nwk1,r_telia, CLIENT_PROVIDER),
                              (rr1_nwk2,r_cogent, CLIENT_PROVIDER),(rr1_nwk2,r_level3, CLIENT_PROVIDER), (rr1_nwk2,r_telia, CLIENT_PROVIDER)]
        
        ###########################################
        ###          For european router        ###
        ###########################################
        for router,peer,link_type in border_router_eu:
                ###########################################
                ###          SHARE ebg                  ###
                ###########################################
                if link_type == SHARE:
                    router.get_config(BGP).set_community(community = '16276:1 16276:4201', from_peer=peer, matching=(all_al,), name='import-from-peer-' + peer, order = 10)
                    router.get_config(BGP).set_local_pref(150, from_peer=peer, matching=(all_al,), name='import-from-peer-' + peer, order = 10)
                    peer.get_config(BGP).set_community(community = 1, from_peer=router, matching=(all_al,), name='import-from-peer-' + router, order = 10)
                    peer.get_config(BGP).set_local_pref(150, from_peer=router, matching=(all_al,), name='import-from-peer-' + router, order = 10)
                    
                    router.get_config(BGP).deny('export-to-peer-' + peer, to_peer=peer, matching=(up_link,), order=10)
                    router.get_config(BGP).deny('export-to-peer-' + peer, to_peer=peer, matching=(peers_link,), order=15)
                    router.get_config(BGP).permit('export-to-peer-' + peer, to_peer=peer, matching=(all_al,), order=25)
                    
                    peer.get_config(BGP).deny('export-to-peer-' + router, to_peer=router, matching=(up_link,), order=10)
                    peer.get_config(BGP).deny('export-to-peer-' + router, to_peer=router, matching=(peers_link,), order=15)
                    peer.get_config(BGP).permit('export-to-peer-' + router, to_peer=router, matching=(all_al,), order=25)
                ###########################################
                ###          CLIENT_PROVIDER ebg        ###
                ###########################################    
                elif link_type == CLIENT_PROVIDER:
                    router.get_config(BGP).set_community(community = '16276:3 16276:4001', from_peer=peer, matching=(all_al,), name='import-from-up-' + peer, order = 10)
                    router.get_config(BGP).set_local_pref(100, from_peer=peer, matching=(all_al,), name='import-from-up-' + peer, order = 10)
                    peer.get_config(BGP).set_community(community = 2, from_peer=router, matching=(all_al,), name='import-from-down-' + router, order = 10)
                    peer.get_config(BGP).set_local_pref(200, from_peer=router, matching=(all_al,), name='import-from-down-' + router, order = 10)
                    
                    router.get_config(BGP).deny('export-to-up-' + peer, to_peer=peer, matching=(up_link,), order=10)
                    router.get_config(BGP).deny('export-to-up-' + peer, to_peer=peer, matching=(peers_link,), order=15)
                    router.get_config(BGP).permit('export-to-up-' + peer, to_peer=peer, matching=(all_al,), order=25)
                
                ###########################################
                ###    Prepending and communities       ###
                ###########################################

                router.get_config(BGP).set_local_pref(name = 'import-from-'+link_type+'-'+peer, local_pref = 240, from_peer=peer, matching=(customer_default,), order = 5)
                router.get_config(BGP).set_local_pref(name = 'import-from-'+link_type+'-'+peer, local_pref = 220, from_peer=peer, matching=(customer_backup,), order = 6)
                
                router.get_config(BGP).set_community(name = 'import-from-'+link_type+'-'+peer, community = 4201, from_peer=peer, matching=(customer_default,), order = 5)
                router.get_config(BGP).set_community(name = 'import-from-'+link_type+'-'+peer, community = 4201, from_peer=peer, matching=(customer_backup,), order = 6)
        
                router.get_config(BGP).deny('export-to-'+link_type+'-'+peer, to_peer = peer, matching=(no_advertise_all,), order=5)
                router.get_config(BGP).deny('export-to-'+link_type+'-'+peer, to_peer = peer, matching=(no_advertise_eu,), order=6)
                
                router.get_config(BGP).set_prepend(name = 'export-to-'+link_type+'-'+peer, size=1, asn=16276, to_peer = peer, matching=(prepend_all_1,), order = 16)
                router.get_config(BGP).set_prepend(name = 'export-to-'+link_type+'-'+peer, size=2, asn=16276, to_peer = peer, matching=(prepend_all_2,), order = 17)
                router.get_config(BGP).set_prepend(name = 'export-to-'+link_type+'-'+peer, size=3, asn=16276, to_peer = peer, matching=(prepend_all_3,), order = 18)
                router.get_config(BGP).set_prepend(name = 'export-to-'+link_type+'-'+peer, size=1, asn=16276, to_peer = peer, matching=(prepend_eu_1,), order = 19)
                router.get_config(BGP).set_prepend(name = 'export-to-'+link_type+'-'+peer, size=2, asn=16276, to_peer = peer, matching=(prepend_eu_2,), order = 20)
                router.get_config(BGP).set_prepend(name = 'export-to-'+link_type+'-'+peer, size=3, asn=16276, to_peer = peer, matching=(prepend_eu_3,), order = 21)

        ###########################################
        ###            For US router            ###
        ###########################################  
        for router,peer,link_type in border_router_us:
                if link_type == SHARE:
                    router.get_config(BGP).set_community(community = '16276:1 16276:4201', from_peer=peer, matching=(all_al,), name='import-from-peer-' + peer, order = 10)
                    router.get_config(BGP).set_local_pref(150, from_peer=peer, matching=(all_al,), name='import-from-peer-' + peer, order = 10)
                    peer.get_config(BGP).set_community(community = 1, from_peer=router, matching=(all_al,), name='import-from-peer-' + router, order = 10)
                    peer.get_config(BGP).set_local_pref(150, from_peer=router, matching=(all_al,), name='import-from-peer-' + router, order = 10)
                    
                    router.get_config(BGP).deny('export-to-peer-' + peer, to_peer=peer, matching=(up_link,), order=10)
                    router.get_config(BGP).deny('export-to-peer-' + peer, to_peer=peer, matching=(peers_link,), order=15)
                    router.get_config(BGP).permit('export-to-peer-' + peer, to_peer=peer, matching=(all_al,), order=25)
                    
                    peer.get_config(BGP).deny('export-to-peer-' + router, to_peer=router, matching=(up_link,), order=10)
                    peer.get_config(BGP).deny('export-to-peer-' + router, to_peer=router, matching=(peers_link,), order=15)
                    peer.get_config(BGP).permit('export-to-peer-' + router, to_peer=router, matching=(all_al,), order=25)
                    
                elif link_type == CLIENT_PROVIDER:
                    router.get_config(BGP).set_community(community = '16276:3 16276:4001', from_peer=peer, matching=(all_al,), name='import-from-up-' + peer, order = 10)
                    router.get_config(BGP).set_local_pref(100, from_peer=peer, matching=(all_al,), name='import-from-up-' + peer, order = 10)
                    peer.get_config(BGP).set_community(community = 2, from_peer=router, matching=(all_al,), name='import-from-down-' + router, order = 10)
                    peer.get_config(BGP).set_local_pref(200, from_peer=router, matching=(all_al,), name='import-from-down-' + router, order = 10)
                    
                    router.get_config(BGP).deny('export-to-up-' + peer, to_peer=peer, matching=(up_link,), order=10)
                    router.get_config(BGP).deny('export-to-up-' + peer, to_peer=peer, matching=(peers_link,), order=15)
                    router.get_config(BGP).permit('export-to-up-' + peer, to_peer=peer, matching=(all_al,), order=25)
                
                router.get_config(BGP).set_local_pref(name = 'import-from-'+link_type+'-'+peer, local_pref = 240, from_peer=peer, matching=(customer_default,), order = 5)
                router.get_config(BGP).set_local_pref(name = 'import-from-'+link_type+'-'+peer, local_pref = 220, from_peer=peer, matching=(customer_backup,), order = 6)
                
                router.get_config(BGP).set_community(name = 'import-from-'+link_type+'-'+peer, community = 4001, from_peer=peer, matching=(customer_default,), order = 5)
                router.get_config(BGP).set_community(name = 'import-from-'+link_type+'-'+peer, community = 4001, from_peer=peer, matching=(customer_backup,), order = 6)
             
                router.get_config(BGP).deny('export-to-'+link_type+'-'+peer, to_peer = peer, matching=(no_advertise_all,), order=5)
                router.get_config(BGP).deny('export-to-'+link_type+'-'+peer, to_peer = peer, matching=(no_advertise_na,), order=6)
                
                router.get_config(BGP).set_prepend(name = 'export-to-'+link_type+'-'+peer, size=1, asn=16276, to_peer = peer, matching=(prepend_all_1,), order = 16)
                router.get_config(BGP).set_prepend(name = 'export-to-'+link_type+'-'+peer, size=2, asn=16276, to_peer = peer, matching=(prepend_all_2,), order = 17)
                router.get_config(BGP).set_prepend(name = 'export-to-'+link_type+'-'+peer, size=3, asn=16276, to_peer = peer, matching=(prepend_all_3,), order = 18)
                router.get_config(BGP).set_prepend(name = 'export-to-'+link_type+'-'+peer, size=1, asn=16276, to_peer = peer, matching=(prepend_na_1,), order = 19)
                router.get_config(BGP).set_prepend(name = 'export-to-'+link_type+'-'+peer, size=2, asn=16276, to_peer = peer, matching=(prepend_na_2,), order = 20)
                router.get_config(BGP).set_prepend(name = 'export-to-'+link_type+'-'+peer, size=3, asn=16276, to_peer = peer, matching=(prepend_na_3,), order = 21)

        super().build(*args, **kwargs)



if __name__ == '__main__':
    
    net = IPNet(topo=OSPFNetOVH(link_params=LINK_PARAMS),allocate_IPs=False)
    try:
        net.start()
        IPCLI(net)
    finally:
        net.stop()


        #Security:
        # * OSPF:
        #   - message-digest authentification key
        #   - 
        # * BGP:
        #   - no multihop -> neighbor PEER ttl-security 3
        #   - neighbor PEER password PASSWORD
        #   - neighbor PEER maximum-prefix 1000
        # * Anycast:
        #   - OSPF area in link params

        #T-E:
        # * OSPF:
        #   - MPLS
        #   - Segment Routing
        #
        # * BGP:
        #   - link-params (MPLS)
        #   - local-pref (outgoing traffic) 
        #   - selective route advertisement TODO
        #   - Community based 
        #   - Prepending

        # AnyCast 
        #   - good with netcat
        #   - good with traceroute