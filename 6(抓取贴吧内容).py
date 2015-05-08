#coding:utf-8

__author__ = 'greatbuger'


import urllib,urllib2,re

class Tool:
    removeImage = re.compile('<img.*?>')
    removeAddr = re.compile('<a.*?>.*?</a>')
    replaceBR = re.compile('<br>')

    def replace(self,x):
        x = re.sub(self.removeImage," ",x)
        x = re.sub(self.removeAddr," ",x)
        x = re.sub(self.replaceBR,"\n",x)
        return x.strip()


class BaiduTieba:
    def __init__(self,baseUrl,seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()

    def getPageCode(self,pageNum):
        try:
            url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #print response.read()
            return response.read().decode('utf-8')
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接错误，原因：",e.reason
                return None



    def getPageSum(self):
        pageCode = self.getPageCode(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,pageCode)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getPageTitle(self):
        pageCode = self.getPageCode(1)
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result = re.search(pattern,pageCode)
        if result:
            return result.group(1).strip()
        else:
            return None


    def getPageContent(self,pageCode):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,pageCode)
        floor = 1
        for item in items:
            print floor,u'楼----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n'
            print self.tool.replace(item)
            print '\n'
            floor+=1

baseUrl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BaiduTieba(baseUrl,1)
bdtb.getPageContent(bdtb.getPageCode(1))
