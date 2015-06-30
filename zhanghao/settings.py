# -*- coding: utf-8 -*-

# Scrapy settings for zhanghao project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zhanghao'

SPIDER_MODULES = ['zhanghao.spiders']
NEWSPIDER_MODULE = 'zhanghao.spiders'

LOG_LEVEL = 'INFO'

ITEM_PIPELINES = {
    # 'zhanghao.pipelines.CalcPassWord': 1,
    'zhanghao.pipelines.JsonPrintPipeline': 2
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhanghao (+http://www.yourdomain.com)'
