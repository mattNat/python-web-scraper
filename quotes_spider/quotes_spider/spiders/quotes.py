# -*- coding: utf-8 -*-
import scrapy

# subclass scrapy.Spider
class QuotesSpider(scrapy.Spider):
    # name ids spider name, must be unique
    name = 'quotes'
    # list of domains
    allowed_domains = ['quotes.toscrape.com/']
    # can be defined as a list
    start_urls = ['http://quotes.toscrape.com//']

    # scrapy default method
    # self: class
    # response: get response ojbect or source code from page
    def parse(self, response):
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        # yield to print to scrappy output
        yield {'H1 Tag': h1_tag, 'Tags': tags}