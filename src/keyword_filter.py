
#! -*- coding: utf-8 -*-
'''
Created on Aug 21, 2011

@author: flyxian
'''
test_kwl = [["花开", "轻之国度"],
            ["美食", "mkv", "异域字幕组"]]

#keyword list, if without initialization use test_kwl
keywords_list = test_kwl

def init_keywords_list():
    pass

def check_keywords(keywords, title):
    counter = 0
    checkee = title.lower()
    for word in keywords:
        if checkee.find(word) >= 0:
            counter += 1
    
    if counter == len(keywords):
        return True
    else:
        return False
    
def check(text):
#    print text
    for keywords in keywords_list:
        if check_keywords(keywords, text):
            return True
    #no match
    return False



if __name__ == "__main__":
    print "keyword_filter: Hello world."
    