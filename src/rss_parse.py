
#! -*- coding: utf-8 -*-
'''
Created on Aug 21, 2011

@author: flyxian
'''

import feedparser

import globals

import browser_bogus
import btsite 
import keyword_filter

#USER_AGENT = "UniversalFeedParser/5.0.1 +http://feedparser.org/"
USER_AGENT = "%s/%f" % (globals.NAME, globals.VERSION)

user = browser_bogus.Browser("", "", USER_AGENT)

#def login(user):
feed_url = btsite.host + btsite.feed_uri

#feed = feedparser.parse(feed_url, 
#                        agent=USER_AGENT);

def init():
    if globals.site_config["backup_site"]:
        btsite.site_ktxp()
        
    global feed_url
    feed_url = btsite.host + btsite.feed_uri
            
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
            offset = len("href=\"")
            end = line[start+offset:].find("\">")
            return line[start+offset:end]
        
def parse():
    feed = feedparser.parse(feed_url, 
                            agent=USER_AGENT);

    #check for update
    if globals.last_update_tag == feed["entries"][0]["updated"]:
        print "No update"
        globals.write_log(0, "No Update.")
        return 0
    else:
        print "Updating"
        globals.write_log(0, "Checking RSS...")
        
    counter = 0
    match = 0
    #parse seed info
    for item in feed["entries"]:
#        for k, v in item.iteritems():
#            print k, ":", v
#        print item["title"]
        if globals.last_update_tag == item["updated"]:
            #only check the updated part
            break
        
        print "Item: %s" % item["title"]
        if keyword_filter.check(item["title"]):
            match += 1
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
    globals.write_log(0, 
                      "Checked %d new items" % counter, 
                      " %d seed post matches" % match)
    globals.last_update_tag = feed["entries"][0]["updated"]
    return match
def test():
    feed = feedparser.parse(feed_url, 
                            agent=USER_AGENT);

    for k, v in feed.iteritems():
        print k
    print "--------------------------------------------------"
    print feed["encoding"]
    for item in feed["entries"]:
        for k, v in item.iteritems():
            print k, ":", v
        break
#        print check_keywords([tag_string], item["title"])
#        print get_post_link(item)
#        print get_seed_link(item)
#        print get_magnet_link(get_post_link(item))
#        break
    
    #check for update
    if globals.last_update_tag == feed["entries"][0]["updated"]:
        print "No update"
        globals.write_log(0, "No Update.")
        return False
    else:
        print "Updating"
        globals.write_log(0, "Checking RSS...")
        globals.last_update_tag = feed["entries"][0]["updated"]
        
if __name__ == "__main__":
    print "rss_parse: Hello world."
#    test()
    globals.init_configs("test_config.yaml")
    keyword_filter.init_keywords_list()
    init()
    parse()
    print globals.seed_list