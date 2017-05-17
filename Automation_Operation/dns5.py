#__*__ coding:utf-8 __*__
#Filename:dns5.py


import dns.resolver
import os
import httplib


iplist=[]
appdomain="www.baidu.com"


def get_iplist(domain):
    try:
        A = dns.resolver.query(domain,'A')
    except Exception,e:
        print'dns resolver error:',str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j)
    return True


def checkip(ip):
    checkurl=str(ip)+':80'
    getcontent=""
    httplib.socket.setdefaulttimeout(5)
    conn=httplib.HTTPConnection(checkurl)
    try:
        conn.request("GET","/",headers={"Host":appdomain})
        r=conn.getresponse()
        getcontent=r.read(15)
    finally:
        if getcontent=="<!DOCTYPE html>":
            print ip," [OK]"
        else:
            print ip," [Error]"


def main():
    if get_iplist(appdomain) and len(iplist)>0:
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error."