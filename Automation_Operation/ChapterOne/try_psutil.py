#coding:utf-8
import psutil
#获取cpu信息
print psutil.cpu_times()
#获取cpu的逻辑个数和物理个数
print psutil.cpu_count()
print psutil.cpu_count(logical=False)
#获取磁盘完整信息
print psutil.disk_partitions()
#获取磁盘IO个数
print psutil.disk_io_counters(perdisk=True)
#获取网络总的IO信息
print psutil.net_io_counters()
#获取当前登录系统的用户信息
print psutil.users()

#psutil.boot_time()获取开机时间，以linux时间戳格式返回，用datetime转换成自然格式
import datetime
print psutil.boot_time()
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y%m%d %H:%M:%S")

#进程管理
pids = psutil.pids()  #列出所有进程PID
print pids
PustilExample=psutil.Process(pids[2])
print PustilExample.memory_percent()   #进程内存利用率

print PustilExample.num_threads()   #进程开启的线程数