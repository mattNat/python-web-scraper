# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['sandiego.craigslist.org']
    start_urls = ['https://sandiego.craigslist.org/search/web']

    def parse(self, response):
        # listings = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        listings = response.xpath('//li[@class="result-row"]')
        for listing in listings:
            # # print(listing)
            # yield {
            #     'Listing': listing
            # }
            date = listing.xpath('.//*[@class="result-date"]/@datetime').extract_first()
            link = listing.xpath('.//a[@class="result-title hdrlnk"]/@href').extract_first()
            text = listing.xpath('.//a[@class="result-title hdrlnk"]/text()').extract_first()

            compensation = response.xpath('//*[@class="attrgroup"]/span[1]/b/text()').extract_first()
            type = response.xpath('//*[@class="attrgroup"]/span[2]/b/text()').extract_first()

            # yield {
            #     'date': date,
            #     'link': link,
            #     'text': text
            # }

            yield scrapy.Request(
                link, 
                callback=self.parse_listing, 
                meta={'date': date, 'link': link, 'text': text}
                )

        next_page_url = response.xpath('//a[text()="next > "]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
    
    def parse_listing(self, response):
        date = response.meta['date']
        link = response.meta['link']
        text = response.meta['text']
        