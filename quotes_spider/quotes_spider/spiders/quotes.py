# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from quotes_spider.items import QuotesSpiderItem

# subclass scrapy.Spider
class QuotesSpider(scrapy.Spider):
    # name ids spider name, must be unique
    name = 'quotes'
    # # list of domains
    # allowed_domains = ['http://quotes.toscrape.com/']
    # # can be defined as a list
    # start_urls = ['http://quotes.toscrape.com/']

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    # scrapy default method
    # self: class
    # response: get response ojbect or source code from page
    def parse(self, response):
        l = ItemLoader(item=QuotesSpiderItem(), response=response)
        # h1_tag = response.xpath('//h1/a/text()').extract_first()
        # tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        # # yield to print to scrappy output
        # yield {'H1 Tag': h1_tag, 'Tags': tags}
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            # quote.xpath('.//*[@itemprop="text"]/text()').extract_first()
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author =  quote.xpath('.//*[@itemprop="author"]/text()').extract_first()


            # string or unicode
            # quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
            # list
            # quote.xpath('.//*[@class="tag"]/text()').extract()
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

            # l.add_value('text', text)
            # l.add_value('author', author)
            # l.add_value('tags', tags)            

            # print("\n")
            # print(text)
            # print(author)
            # print(tags)
            # print("\n")

            yield {
                'Text': text,
                'Author': author,
                'Tags': tags
            }

            # return l.load_item()

        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)    
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)
            
        
            # recursively follow the link to the next page
            # if next_page_url is not None:
            #     # callback function below if not in parse function

            #     # next_page_url = response.urljoin(next_page_url)
            #     # yield scrapy.Request(next_page_url, callback=self.parse)
            #     yield response.follow(next_page_url, callback=self.parse)
                