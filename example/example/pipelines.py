# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import datetime

DEBUG = True

if DEBUG:
    dbuser = 'root'
    dbpass = 'zjz4818774'
    dbname = 'weather'
    dbhost = '127.0.0.1'
    dbport = '3306'
else:
    dbuser = 'root'
    dbpass = 'zjz4818774'
    dbname = 'weather'
    dbhost = 'localhost'
    dbport = '3306'

class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        #清空表：
        self.cursor.execute("truncate table weather;")
        self.conn.commit()

    def process_item(self, item, spider):
        curTime =  datetime.datetime.now()
        try:
            self.cursor.execute("""INSERT INTO weather (weatherDate,  weatherWea, weatherTem1, weatherTem2, weatherWin, updateTime)
                            VALUES (%s, %s, %s, %s, %s, %s)""",
                            (
                                item['weatherDate'][0].encode('utf-8'),
                               # item['weatherDate2'][0].encode('utf-8'),
                                item['weatherWea'][0].encode('utf-8'),
                                item['weatherTem1'][0].encode('utf-8'),
                                item['weatherTem2'][0].encode('utf-8'),
                                item['weatherWin'][0].encode('utf-8'),
                                curTime,
                            )
            )

            self.conn.commit()


        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item