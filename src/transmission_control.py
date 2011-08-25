
#! -*- coding: utf-8 -*-
'''
Created on Aug 22, 2011

@author: flyxian
'''

import transmissionrpc

import globals

#globals.init_configs("test_config.yaml")
#print globals.trconfig

tc = None

#create rpc connection to transmission
def connect():
    global tc
    tc = transmissionrpc.Client(globals.trconfig["host"], 
                                port=globals.trconfig["port"], 
                                user=globals.trconfig["user"], 
                                password=globals.trconfig["password"])

def download_seed(seed_info):
    global tc
    try:
        if globals.site_config["torrent_file"]:
            tc.add(seed_info["seed"])
        else:
            if globals.site_config["backup_site"]:
                tc.add_uri(seed_info["seed"])
            else:
                tc.add_uri(seed_info["magnet"])
    except transmissionrpc.error.TransmissionError, e:
        globals.write_log(0, 
                          e.message, 
                          "Error :\t%s" % seed_info["title"], 
                          "\t%s" % seed_info["post"], 
                          "\t%s" % seed_info["seed"][-41:], 
                          "\t%s" % seed_info["magnet"][:52])
        return
        
            
    globals.write_log(0, 
                      "Add :\t%s" % seed_info["title"], 
                      "\t%s" % seed_info["post"], 
                      "\t%s" % seed_info["seed"][-41:],
                      "\t%s" % seed_info["magnet"][:52])


if __name__ == "__main__":
    print "transmission_control: Hello world."
    connect()
    tc.list()
    