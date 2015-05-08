#coding:utf-8

__author__ = 'greatbuger'

import urllib,urllib2,re
class BaiduTieba:
    def __init__(self,baseUrl,seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        #测试输出
        url=self.baseUrl + self.seeLZ
        print url
baseUrl = 'http://tieba.baidu.com/p/3138733512'
bt=BaiduTieba(baseUrl,1)

