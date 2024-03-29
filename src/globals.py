
#! -*- coding: utf-8 -*-
'''
Created on Aug 21, 2011

@author: flyxian
'''

#import hashlib
import yaml
import time
import codecs
import hashlib

NAME = "AA RSS News Reader"
VERSION = 0.4

debug = 0

#configs
trconfig = {"host" : "192.168.1.5", 
            "port" : 9091,
            "user" : "flyxian", 
            "password" : "bt880326"}

rss_config = {"update_period" : 5, 
              "keywords_list" : "./keywords", 
              "shell_output" : True}

site_config = {"backup_site" : False,
               "torrent_file" : False}

def init_configs(filename):
    configs = yaml.load(file(filename))
    
    global trconfig
    global rss_config
    global site_config
    
    trconfig = configs["trconfig"]
    rss_config = configs["rss_config"]
    site_config = configs["site_config"]
    
    global debug
    if rss_config["shell_output"]:
        debug = 1
        
    write_log(0, "Read configs from %s" % filename) 

#runtime variables
last_update_tag = ""

seed_list = []

local_torrent_list = set()

def check_duplication(seed_info):
    seed_hash = hashlib.md5(seed_info["title"].encode('utf-8')).hexdigest()
    if seed_hash not in local_torrent_list:
        local_torrent_list.add(seed_hash)
        return True
    else:
        return False

def add_seed_info(title, post_link, seed_link, magnet_link=""):
    #check duplication
    seed_info = {"title" : title,
                 "post" : post_link,
                 "seed" : seed_link,
                 "magnet" : magnet_link}
#    h = hashlib.new(title)
#    h.update(post_link)
#    h.update(seed_link)
#    key = h.hexdigest()
#    print key
    if debug > 2:
        print seed_info
    seed_list.append(seed_info)
    
  
    
#logging
logfile = codecs.open("log", "w+", "utf-8")
log_output_level= 3

sep = "-----------------------------"
def write_log(level=0, *args):
    if level > log_output_level:
        return
    
    timestamp = time.strftime("[%a, %d %b %Y %H:%M:%S +0000]", time.gmtime())
    if len(args) > 1:
        print >> logfile, sep
        print >> logfile, timestamp
        if debug > 0:
            print sep
            print timestamp
    else:
        print >> logfile, timestamp,
        if debug > 0:
            print timestamp,
    for arg in args:
        print >> logfile, arg
        if debug > 0:
            print arg
        
    logfile.flush()
        




if __name__ == "__main__":
    print "globals: Hello world."
#    init_configs("config.yaml")
    print trconfig
    print rss_config
#    add_seed_info(title)
