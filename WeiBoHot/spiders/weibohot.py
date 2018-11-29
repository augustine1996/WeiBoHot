# -*- coding: utf-8 -*-
import scrapy


class WeibohotSpider(scrapy.Spider):
    name = 'weibohot'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com/']

    def parse(self, response):
        pass
