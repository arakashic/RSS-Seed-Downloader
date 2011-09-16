
#! -*- coding: utf-8 -*-
'''
Created on Aug 21, 2011

@author: flyxian
'''

host = "http://share.dmhy.me"
login_uri = "/user/login"

feed_uri = "/topics/rss/rss.xml"

def site_ktxp():
    global host
    global feed_uri
    host = "http://bt.ktxp.com"
    feed_uri = "/rss-sort-1.xml"



if __name__ == "__main__":
    print "share_dmhy_net: Hello world."
    site_ktxp()
    print host
    print feed_uri
    
    