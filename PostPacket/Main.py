# -*- coding: UTF-8 -*-
import time
from  OneGroupMain import GetOneGroup

def main():
   index = 0
   GroupList = ['QingLiangZu','ZhongLiangZu','JiJinZu','ChengXuHuaZu','JinRongQiHuo','YouSeJinShu','GuiJinShu','NongChanPin','NengYuanHuaGong','JingLiRun']
   #GroupList = ['JinRongQiHuo','YouSeJinShu','GuiJinShu','NongChanPin','NengYuanHuaGong','JingLiRun']
   #GroupList = ['QingLiangZu']
   #GroupList = ['NengYuanHuaGong']
   #GroupList = ['JingLiRun']

   try:
      for GroupType in GroupList:
           print "开始进行"+GroupType+"的抓取和存储工作"
           GetOneGroup(GroupType)
           index+=1
   except Exception as e:
        print e.message
        print "报错:"+GroupList[index]+"出现错误，程序终止"
   return "everything is OK"


if __name__ == "__main__":
     total_start =time.clock()

     main()

     total_end = time.clock()
     print 'whole project Running time: %s Seconds\n'%(total_end-total_start)