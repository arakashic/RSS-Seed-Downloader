
#! -*- coding: utf-8 -*-
'''
Created on Sep 12, 2011

@author: Flyxian
'''

def find(string, keyword):
    hit_q = []
    len_str = len(string)
    len_key = len(keyword)
    i = 0
    
    while i < len_str:
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
    str1 = "【SOSG字幕&月光恋曲】★【Fairy Tail_妖精的尾巴】【第96话 消除生命的人】[MP4][480p]"
    str2 = "能設計好字型且會時軸的基本使"
    keyword1 = "妖精的尾巴"
    keyword2 = "MP4"
    print find(str1.lower(), keyword1.lower())
    print find(str2, keyword1)
    print find(str1, keyword2)
    print find(str2, keyword2)
    