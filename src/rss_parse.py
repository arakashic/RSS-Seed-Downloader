
#! -*- coding: utf-8 -*-
'''
Created on Aug 21, 2011

@author: flyxian
'''

import feedparser

import globals

import browser_bogus
import share_dmhy_net
import keyword_filter

#USER_AGENT = "UniversalFeedParser/5.0.1 +http://feedparser.org/"
USER_AGENT = "%s/%f" % (globals.NAME, globals.VERSION)

user = browser_bogus.Browser("", "", USER_AGENT)

#def login(user):
    
feed_url = share_dmhy_net.host + share_dmhy_net.feed_uri

feed = feedparser.parse(feed_url, 
                        agent=USER_AGENT);

def get_post_link(item):
    ret = ""
    for link in item["links"]:
        if link["rel"] == "alternate":
            ret = link["href"]
            break
    return ret

def get_seed_link(item):
    ret = ""
    for link in item["links"]:
        if link["rel"] == "enclosure":
            ret = link["href"]
            break
    return ret

#def check_keywords(keywords, title):
#    counter = 0
#    checkee = title.lower()
#    for word in keywords:
#        if checkee.find(word.lower()) >= 0:
#            counter += 1
#    
#    if counter == len(keywords):
#        return True
#    else:
#        return False
    
def get_magnet_link(post_link):
    result = user.urlOpener.open(post_link)
    pagelines = result.readlines()
    
    for line in pagelines:
        start = line.find("href=\"magnet")
        if start >= 0:
            return line[start+len("href=\""):line.find("\">")]
        
def parse():
    #check for update
    if globals.last_update_tag == feed["entries"][0]["updated"]:
        print "No update"
        globals.write_log(0, "Checking RSS...", "No Update.")
        return False
    else:
        globals.write_log(0, "Checking RSS...")
        globals.last_update_tag = feed["entries"][0]["updated"]
        
    counter = 0
    #parse seed info
    for item in feed["entries"]:
#        for k, v in item.iteritems():
#            print k, ":", v
#        print item["title"]
        if globals.last_update_tag == item["updated"]:
            #only check the updated part
            break
        
        if keyword_filter.check(item["title"]):
            globals.add_seed_info(item["title"], 
                                  get_post_link(item), 
                                  get_seed_link(item), 
                                  get_magnet_link(get_post_link(item)))
        counter += 1
#            if check_keywords(keywords, item["title"]):
#                globals.add_seed_info(item["title"], 
#                                      get_post_link(item), 
#                                      get_seed_link(item), 
#                                      get_magnet_link(get_post_link(item)))
#                    print get_post_link(item)
#                    print get_seed_link(item)
#                    print get_magnet_link(get_post_link(item))
    msg = "Checked %d new items" % counter
    print msg
    globals.write_log(0, msg)
    return True
if __name__ == "__main__":
    print "rss_parse: Hello world."
#    for k, v in feed.iteritems():
#        print k
#    print "--------------------------------------------------"
#    print feed["entries"][0]
#    for item in feed["entries"]:
#        for k, v in item.iteritems():
#            print k, ":", v
#            
#        print check_keywords([tag_string], item["title"])
#        print get_post_link(item)
#        print get_seed_link(item)
#        print get_magnet_link(get_post_link(item))
#        break
    keyword_filter.init_keywords_list()
    parse()
    print globals.seed_list