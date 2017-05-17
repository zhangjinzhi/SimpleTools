# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import scrapy
from example.items import Weather2Item

class CatchWeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['weather.com.cn']
    start_urls = [
        "http://www.weather.com.cn/weather/101200101.shtml",#武汉
        "http://www.weather.com.cn/weather/101200901.shtml",#宜昌
        "http://www.weather.com.cn/weather/101200201.shtml",#襄阳
        "http://www.weather.com.cn/weather/101201101.shtml",#十堰
        "http://www.weather.com.cn/weather/101200801.shtml",#荆州
        "http://www.weather.com.cn/weather/101050101.shtml",#哈尔滨
        "http://www.weather.com.cn/weather/101050201.shtml",#齐齐哈尔
        "http://www.weather.com.cn/weather/101050401.shtml",#佳木斯
        "http://www.weather.com.cn/weather/101150101.shtml",#西宁
        "http://www.weather.com.cn/weather/101150714.shtml",#格尔木
        "http://www.weather.com.cn/weather/101160101.shtml",#兰州
        "http://www.weather.com.cn/weather/101270101.shtml",#成都
        "http://www.weather.com.cn/weather/101271401.shtml",#乐山
        "http://www.weather.com.cn/weather/101271301.shtml",#资阳
        "http://www.weather.com.cn/weather/101310101.shtml",#海口
        "http://www.weather.com.cn/weather/101310201.shtml",#三亚
        "http://www.weather.com.cn/weather/101340201.shtml",#高雄
        "http://www.weather.com.cn/weather/101320101.shtml",#香港
        "http://www.weather.com.cn/weather/101220101.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101220201.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101220301.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101220401.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101220501.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101220601.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101220701.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101220801.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101220901.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101221001.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101221101.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101221201.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101221301.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101221401.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101221501.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101221601.shtml",#安徽地区各个城市
        "http://www.weather.com.cn/weather/101221701.shtml",#安徽地区各个城市

    ]

    def parse(self, response):
        for sel in response.xpath('//*[@id="7d"]/ul/li'):
            item = Weather2Item()
            item['weatherDate'] = sel.xpath('h1/text()').extract()
            #item['weatherDate2'] = sel.xpath('h2/text()').extract()
            item['weatherWea'] = sel.xpath('p[@class="wea"]/text()').extract()
            item['weatherTem1'] = sel.xpath('p[@class="tem"]/span/text()').extract() #+ sel.xpath('p[@class="tem tem1"]/i/text()').extract()
            item['weatherTem2'] = sel.xpath('p[@class="tem"]/i/text()').extract() #+ sel.xpath('p[@class="tem tem2"]/i/text()').extract()
            item['weatherWin'] = sel.xpath('p[@class="win"]/i/text()').extract()
            yield item