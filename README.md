# Next Gig

## Summary
Next Gig is a web scraper built with the Scrapy framework.  Its core feature includes scraping web pages on Craigslist to find jobs under the category "web developer" or a profession of your choice.  

### Core Features
1. Scrape date, title of job, and the url.

![alt text](https://github.com/mattNat/python-web-scraper/master/images/craigslist-title.png)

2. In each url, scrape "compensation", "employment type", images, and description of job.

![alt text](https://github.com/mattNat/python-web-scraper/master/images/craigslist-url.png)

3. Using Scrapy settings, output data to CSV and/or JSON to view on spreadsheet program. 

### Extension Ideas
1. Extract data into database MongoDB.
2. Extend scraper to include finding jobs in LinkedIn.