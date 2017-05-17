# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

class Weather2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    weatherDate = scrapy.Field()  # 星期
    weatherWea = scrapy.Field()   # 天气状况
    weatherTem1 = scrapy.Field()  # 最高温度
    weatherTem2 = scrapy.Field()  # 最低温度
    weatherWin = scrapy.Field()   # 风力
