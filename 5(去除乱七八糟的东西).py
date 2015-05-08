#coding:utf-8
__author__ = 'greatbuger'
import re

class Tool:
    removeImage = re.compile('<img.*?>')
    removeAddr = re.compile('<a.*?>.*?</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    removeBR = re.compile('<br>')
    replaceTD= re.compile('<td>')
    removeExtraTag = re.compile('<.*?>')

    def replace(self,x):
        x = re.sub(self.removeImage," ",x)
        x = re.sub(self.removeAddr," ",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.removeBR,"/n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.removeExtraTag,"",x)
        return x.strip()




