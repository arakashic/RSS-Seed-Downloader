
#! -*- coding: utf-8 -*-
'''
Created on Sep 12, 2011

@author: Flyxian
'''

def find(string, keyword):
    hit_q = []
    len_str = len(string)
    len_key = len(keyword)
<<<<<<< HEAD
    i = 0
    
    while i < len_str:
=======
    if len_str < len_str or len_key == 0:
        return False
    
    i = 0
    
    while i < len_str - len_key:
>>>>>>> release-0.4
        j = 0
        while j < len_key:
            if i + j >= len_str:
                return False
            if string[i+j] != keyword[j]:
                break
            j += 1
        
        if j == len_key:
            return True
        
        i += 1
    return False



if __name__ == "__main__":
    print ": Hello world."
<<<<<<< HEAD
    str1 = "【SOSG字幕&月光恋曲】★【Fairy Tail_妖精的尾巴】【第96话 消除生命的人】[MP4][480p]"
    str2 = "能設計好字型且會時軸的基本使"
    keyword1 = "妖精的尾巴"
    keyword2 = "MP4"
    print find(str1.lower(), keyword1.lower())
=======
    str1 = "[轻之国度][青之驱魔师][第22话][GB][480P][MP4]"
    str2 = "能設計好字型且會時軸的基本使"
    keyword1 = "青之驱魔师"
    keyword2 = "MP4"
    print find(str1, keyword1)
>>>>>>> release-0.4
    print find(str2, keyword1)
    print find(str1, keyword2)
    print find(str2, keyword2)
    

#! -*- coding: utf-8 -*-
'''
Created on Sep 12, 2011

@author: Flyxian
'''

def find(string, keyword):
    hit_q = []
    len_str = len(string)
    len_key = len(keyword)
    if len_str < len_str or len_key == 0:
        return False
    
    i = 0
    
    while i < len_str - len_key:
        j = 0
        while j < len_key:
            if i + j >= len_str:
                return False
            if string[i+j] != keyword[j]:
                break
            j += 1
        
        if j == len_key:
            return True
        
        i += 1
    return False



if __name__ == "__main__":
    print ": Hello world."
    str1 = "[杞讳箣鍥藉害][闈掍箣椹遍瓟甯圿[绗�2璇漖[GB][480P][MP4]"
    str2 = "鑳借ō瑷堝ソ瀛楀瀷涓旀渻鏅傝桓鐨勫熀鏈娇"
    keyword1 = "闈掍箣椹遍瓟甯�
    keyword2 = "MP4"
    print find(str1, keyword1)
    print find(str2, keyword1)
    print find(str1, keyword2)
    print find(str2, keyword2)
    