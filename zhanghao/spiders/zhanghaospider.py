# -*- coding: utf-8 -*-
import scrapy
from zhanghao.items import ZhanghaoItem

class ZhanghaospiderSpider(scrapy.Spider):
    name = "zhanghaospider"
    allowed_domains = ["zhanghao.cc"]
    start_urls = (
        'http://www.zhanghao.cc',
    )

    def parse(self, response):
        for tr in response.xpath('//table/tr'):
            type = tr.xpath('td[1]/text()').extract()[0]
            account = tr.xpath('td[1]/font/text()').extract()[0]
            password = ''
            yield ZhanghaoItem(type=type,account=account,password=password)
    pass
