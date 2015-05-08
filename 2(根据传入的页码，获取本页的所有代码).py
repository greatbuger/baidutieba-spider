#coding:utf-8
__author__ = 'greatbuger'


import urllib,urllib2,re


class BaiduTieba:
    def __init__(self,baseUrl,seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)

    def getPageCode(self,pageNum):
        try:
            url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read()
            #return response.read().decode('utf-8')
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接错误，原因：",e.reason
                return None

baseUrl = 'http://tieba.baidu.com/p/3138733512'
bt=BaiduTieba(baseUrl,1)
bt.getPageCode(1)


