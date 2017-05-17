# coding:utf-8

#zipfile在dos中正常工作

# import zipfile
# from zipfile import ZipFile
# filename = r"F:\1\angular.js-1.4.13.zip"
# z = ZipFile(filename,'r')
# for f in z.namelist():
#     print f

#gzip在dos中正常工作

# import gzip
# import os
# def un_gz(file_name):
#     """ungz zip file"""
#     f_name = file_name.replace(".gz", "")
#     #获取文件的名称，去掉
#     g_file = gzip.GzipFile(file_name)
#     #创建gzip对象
#     open(f_name, "w+").write(g_file.read())
#     #gzip对象用read()打开后，写入open()建立的文件中。
#     g_file.close()
#     #关闭gzip对象


#注意！！！！！！！！！！！！！！！！！！！！！！！不能在代码的同一行添加中文注释！！！！不然报错
from unrar import rarfile
file = rarfile.RarFile(r"F:\1\echarts3.rar")
file.extractall(r'F:\2')