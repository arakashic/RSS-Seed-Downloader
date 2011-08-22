
#! -*- coding: utf-8 -*-
'''
Created on Aug 21, 2011

@author: flyxian
'''

#import hashlib

NAME = "AA RSS News Reader"
VERSION = 0.1

seed_list = []

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
    print seed_info
    seed_list.append(seed_info)




if __name__ == "__main__":
    print "globals: Hello world."
#    add_seed_info(title)