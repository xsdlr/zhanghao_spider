# -*- coding: utf-8 -*-
import scrapy
import random
from zhanghao.items import ZhanghaoItem

class ZhanghaospiderSpider(scrapy.Spider):
    name = "zhanghaospider"
    allowed_domains = ["zhanghao.cc"]
    start_urls = (
        'http://www.zhanghao.cc',
    )

    def randomIp(self):
        _randomIp = ''
        for i in range(4):
            _randomIp += '.' + str(random.randint(1, 255))
        return _randomIp[1:]

    def parse(self, response):
        sel = scrapy.Selector(response)
        for tr in sel.xpath('//table/tr'):
            item = ZhanghaoItem()
            type = tr.xpath('td[1]/text()').extract()[0][:-2]
            id = tr.xpath('td[2]/input/@id').extract()[0]
            item['type'] = type
            item['account'] = tr.xpath('td[1]/font/text()').extract()[0]
            item['id'] = id
            url = "http://www.zhanghao.cc//index.php?c=main&a=getpass&id={id}".format(id=id)
            ip = self.randomIp()
            headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip,deflate",
                "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Client-Ip": ip,
                "X-Forwarded-For": ip
            }
            request = scrapy.Request(url=url, headers=headers,
                             callback=self.parse_password)
            request.meta['item'] = item
            yield request

    def parse_password(self, response):
        item = response.meta['item']
        item = response.meta['item']
        item['password'] = response.body
        return item