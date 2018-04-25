# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['sandiego.craigslist.org']
    start_urls = ['http://sandiego.craigslist.org/']

    def parse(self, response):
        pass
