# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import scrapy

class JsonPrintPipeline(object):
    def process_item(self, item, spider):
        line = json.dumps(dict(item), encoding="UTF-8", ensure_ascii=False)
        print(line)
        return item
