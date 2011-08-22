#This contains global definition of Browser class and other useful thing
#######################################################################################
#                                                                                     #
#    File: browser_bogus.py                                                           #
#    Part of 2dgal-cheater                                                            #
#    Home: http://2dgal-cheater.googlecode.com                                        #
#                                                                                     #
#    The MIT License                                                                  #
#                                                                                     #
#    Copyright (c) 2010-2011 <araya.akashic@gmail.com>                                #
#                                                                                     #
#    Permission is hereby granted, free of charge, to any person obtaining a copy     #
#    of this software and associated documentation files (the "Software"), to deal    #
#    in the Software without restriction, including without limitation the rights     #
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell        #
#    copies of the Software, and to permit persons to whom the Software is            #
#    furnished to do so, subject to the following conditions:                         #
#                                                                                     #
#    The above copyright notice and this permission notice shall be included in       #
#    all copies or substantial portions of the Software.                              #
#                                                                                     #
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR       #
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,         #
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE      #
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER           #
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,    #
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN        #
#    THE SOFTWARE.                                                                    #
#                                                                                     #
#######################################################################################
#Author: Araya

import urllib2
import cookielib

class Browser():
    def __init__(self, user, passwd, user_agent="Python-urllib/2.7"):
        self.username = user
        self.password = passwd
        self.user_agent = user_agent
        self.cookie = cookielib.CookieJar()
        self.urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        self.logout_URI = ""
        #ad link
        self.ad_link = ""