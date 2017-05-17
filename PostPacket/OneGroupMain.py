# -*- coding: UTF-8 -*-
import time
import date as date_list
import pagenumber as GetTotalPageNumber
from Threading import myThread

def GetOneGroup(GroupType):
    total_start =time.clock()
    Datelist = date_list.get_date_list('2016-04-01','2016-09-30')
    for Date in Datelist:
        TotalPageNmber = GetTotalPageNumber.getOneDayTotalPageNumber(Date,GroupType)
        nameList = [i for i in  range(1,int(TotalPageNmber)+1)]
        #nameList = [i for i in  range(100,int(TotalPageNmber)+1)]
        #nameList = [i for i in  range(1,100)]
        threadList  = ["thread-" + str(n) for n in nameList]
        threadID = 1
        # 创建新线程
        for tName in threadList:
            thread = myThread(threadID, tName,Date,GroupType)
            #启动线程
            thread.start()
            threadID += 1

    total_end = time.clock()
    print GroupType+' Group Running time: %s Seconds\n'%(total_end-total_start)

if __name__ == "__main__":
     total_start =time.clock()

     GroupType = "QingLiangZu"
     GetOneGroup(GroupType)

     total_end = time.clock()
     print 'whole project Running time: %s Seconds\n'%(total_end-total_start)