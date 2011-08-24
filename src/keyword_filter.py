
#! -*- coding: utf-8 -*-
'''
Created on Aug 21, 2011

@author: flyxian
'''
debug = 2

test_kwl = [["花开", "轻之国度"],
            ["美食", "mkv", "异域字幕组"]]

#keyword list, if without initialization use test_kwl
keywords_list = test_kwl

def init_keywords_list(filename="keywords"):
    fp = open(filename, "r")
    lines = fp.readlines()
    fp.close()
    
    global keywords_list
    keywords_list = []
    for line in lines:
        if line[0] == "#" or len(line) == 0:
            continue
        
        if debug > 2:
            print line.strip()
            
        words = line.strip().lower().split(" ")
        keywords_list.append(words)
        
    if debug > 2:
        print keywords_list

def check_keywords(keywords, title):
    counter = 0
    checkee = title.lower()
    for word in keywords:
        if debug > 3:
            print "Checking: %s" % word
        if checkee.encode("utf-8").find(word) >= 0:
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
    init_keywords_list()
    
    