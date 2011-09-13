
#! -*- coding: utf-8 -*-
'''
Created on Aug 23, 2011

@author: flyxian
'''
import os
import sys
import time

import globals
import rss_parse
import transmission_control
import keyword_filter
import daemonize


if __name__ == "__main__":
    cwd = os.getcwd()
    output = os.path.join(cwd, "rss-seeddl.log")
    pid_file = os.path.join(cwd, "rss-seeddl.pid")
    daemonize.daemonize(stdout=output, stderr=output, pidfile=pid_file)
    os.chdir(cwd)
    
#    print "main: Hello world."
    globals.write_log(0, "Starting...", "")
    globals.init_configs("test_config.yaml")
    keyword_filter.init_keywords_list(globals.rss_config["keywords_list"])
    rss_parse.init()
    transmission_control.connect()
    
    globals.write_log(0, "Running...", "")
    while True:
        ret = rss_parse.parse()
        if ret > 0:
            for seed in globals.seed_list:
                transmission_control.download_seed(seed)
                
        time.sleep(globals.rss_config["update_period"]*60)
