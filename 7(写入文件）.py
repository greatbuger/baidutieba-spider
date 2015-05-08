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
    def __init__(self,baseUrl,seeLZ,floorTag):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()
        self.file = None
        self.floor = 1
        self.default = u'百度贴吧'
        self.floorTag = floorTag

    def getPageCode(self,pageNum):
        try:
            url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接错误，原因：",e.reason
                return None



    def getPageSum(self,pageCode):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,pageCode)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getPageTitle(self,pageCode):
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result = re.search(pattern,pageCode)
        if result:
            return result.group(1).strip()
        else:
            return None


    def getPageContent(self,pageCode):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,pageCode)
        contents = []
        for item in items:
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
        return contents

    def setFileTitle(self,title):
        if title is not None:
            self.file = open(title + ".txt","w+")
        else:
            self.file = open(self.defaultTitle + ".txt","w+")



    def writeData(self,contents):
        for item in contents:
            if self.floorTag == '1':
                floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1


    def start(self):
        indexPageCode = self.getPageCode(1)
        pageSum = self.getPageSum(indexPageCode)
        title = self.getPageTitle(indexPageCode)
        self.setFileTitle(title)

        try:
            print "该帖子共有" + str(pageSum) + " 页"
            for i in range(1,int(pageSum)+1):
                print "正在写入第" + str(i) + "页数据"
                pageCode = self.getPageCode(i)
                contents = self.getPageContent(pageCode)
                self.writeData(contents)
        except IOError,e:
            print "写入异常，原因" + e.message
        finally:
            print "写入任务完成"




baseUrl = 'http://tieba.baidu.com/p/3138733512'
seeLZ = raw_input("是否获取楼主发言，是输入1,否输入0\n")
floorTag = raw_input("是否写入楼层信息，是输入1,否输入0\n")
bdtb = BaiduTieba(baseUrl,seeLZ,floorTag)
bdtb.start()
