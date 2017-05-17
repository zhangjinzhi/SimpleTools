# -*- coding: UTF-8 -*-
import requests
import Queue
import threading
import time
import date as date_list
import pagenumber as GetTotalPageNumber
import postpacketpayload as GetPostPacket
import write as WriteInCSV

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name + "\n"
        process_data(self.name, self.q)
        print "Exiting " + self.name + "\n"
def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s的%s页\n" % (threadName,Date, data)
            url = "http://spds.qhrb.com.cn/SP10/SPOverSee1.aspx"
            payload = GetPostPacket.getQingLiangZuPayload(data,Date)     #要加上一个参数用来判断哪一组
            headers = GetPostPacket.getQingLiangZuHeaders()
            response = requests.request("POST", url, data=payload, headers=headers)
            page_source = response.text
            result_successfully = WriteInCSV.select_data(page_source)
            print "存储"+Date +"的"+ str(data) + "页中的数据\n"
            print result_successfully
        else:
            queueLock.release()
        time.sleep(0)


if __name__ == "__main__":
    total_start =time.clock()
    Datelist = date_list.get_date_list('2016-04-01','2016-05-01')

    for Date in Datelist:
        start =time.clock()
        exitFlag = 0
        TotalPageNmber = GetTotalPageNumber.getOneDayTotalPageNumber(Date)
        nameList = [i for i in  range(1,int(TotalPageNmber)+1)]
        threadList  = ["thread-" + str(n) for n in nameList]
        queueLock = threading.Lock()
        workQueue = Queue.Queue(int(TotalPageNmber))
        threads = []
        threadID = 1
        # 创建新线程
        for tName in threadList:
            thread = myThread(threadID, tName, workQueue)
            thread.start()
            threads.append(thread)
            threadID += 1
        # 填充队列
        queueLock.acquire()
        for word in nameList:
            workQueue.put(word)
        queueLock.release()
        # 等待队列清空
        while not workQueue.empty():
            pass
        # 通知线程是时候退出
        exitFlag = 1
        # 等待所有线程完成
        for t in threads:
            t.join()
        print "Exiting Main Thread\n"
        end = time.clock()
        print 'all threads of '+Date+' Running time: %s Seconds\n'%(end-start)



    total_end = time.clock()
    print 'whole project Running time: %s Seconds\n'%(total_end-total_start)
