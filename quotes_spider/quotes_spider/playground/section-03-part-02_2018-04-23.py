In [1]: fetch("http://quotes.toscrape.com/")
2018-04-24 15:52:08 [scrapy.core.engine] INFO: Spider opened
2018-04-24 15:52:08 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)
2018-04-24 15:52:08 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/> (referer: None)

In [2]: response
Out[2]: <200 http://quotes.toscrape.com/>

In [3]: request
Out[3]: <GET http://quotes.toscrape.com/>

In [4]: response.css
Out[4]: <bound method TextResponse.css of <200 http://quotes.toscrape.com/>>

In [5]: response.css('h1')
Out[5]: [<Selector xpath='descendant-or-self::h1' data='<h1>\n                    <a href="/" sty'>]

In [6]: response.css('h1::text')
Out[6]: 
[<Selector xpath='descendant-or-self::h1/text()' data='\n                    '>,
 <Selector xpath='descendant-or-self::h1/text()' data='\n                '>]

In [7]: response.xpath('h1')
Out[7]: []

In [8]: response.xpath('//h1')
Out[8]: [<Selector xpath='//h1' data='<h1>\n                    <a href="/" sty'>]

In [9]: response.xpath('//h1/a')
Out[9]: [<Selector xpath='//h1/a' data='<a href="/" style="text-decoration: none'>]

In [10]: response.xpath('//h1/a/text()')
Out[10]: [<Selector xpath='//h1/a/text()' data='Quotes to Scrape'>]

In [11]: response.xpath('//h1/a/text()').extract()
Out[11]: ['Quotes to Scrape']

In [12]: response.xpath('//h1/a/text()').extract_first()
Out[12]: 'Quotes to Scrape'

In [13]: response.xpath('//*[@class=""]')
Out[13]: []

In [14]: response.xpath('//*[@class="tag"]')
Out[14]: 
[<Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/change/page/1/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/deep-thoughts/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/thinking/page/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/world/page/1/"'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/abilities/page'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/choices/page/1'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/inspirational/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/life/page/1/">'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/live/page/1/">'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/miracle/page/1'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/miracles/page/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/aliteracy/page'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/books/page/1/"'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/classic/page/1'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/humor/page/1/"'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/be-yourself/pa'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/inspirational/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/adulthood/page'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/success/page/1'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/value/page/1/"'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/life/page/1/">'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/love/page/1/">'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/edison/page/1/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/failure/page/1'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/inspirational/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/paraphrased/pa'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/misattributed-'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/humor/page/1/"'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/obvious/page/1'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/simile/page/1/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 28px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 26px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 26px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 24px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 22px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 14px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 10px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 8px" hr'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 8px" hr'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 6px" hr'>]

In [15]: response.xpath('//*[@class="tag-item"]')
Out[15]: 
[<Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>]

In [16]:  len(response.xpath('//*[@class="tag-item"]')
    ...: )
Out[16]: 10

In [17]:  len(response.xpath('//*[@class="tag-item"]'))
Out[17]: 10

In [18]:  len(response.xpath('//*[@class="tag-item"]/a'))
Out[18]: 10

In [19]:  response.xpath('//*[@class="tag-item"]/a')
Out[19]: 
[<Selector xpath='//*[@class="tag-item"]/a' data='<a class="tag" style="font-size: 28px" h'>,
 <Selector xpath='//*[@class="tag-item"]/a' data='<a class="tag" style="font-size: 26px" h'>,
 <Selector xpath='//*[@class="tag-item"]/a' data='<a class="tag" style="font-size: 26px" h'>,
 <Selector xpath='//*[@class="tag-item"]/a' data='<a class="tag" style="font-size: 24px" h'>,
 <Selector xpath='//*[@class="tag-item"]/a' data='<a class="tag" style="font-size: 22px" h'>,
 <Selector xpath='//*[@class="tag-item"]/a' data='<a class="tag" style="font-size: 14px" h'>,
 <Selector xpath='//*[@class="tag-item"]/a' data='<a class="tag" style="font-size: 10px" h'>,
 <Selector xpath='//*[@class="tag-item"]/a' data='<a class="tag" style="font-size: 8px" hr'>,
 <Selector xpath='//*[@class="tag-item"]/a' data='<a class="tag" style="font-size: 8px" hr'>,
 <Selector xpath='//*[@class="tag-item"]/a' data='<a class="tag" style="font-size: 6px" hr'>]

In [20]:  response.xpath('//*[@class="tag-item"]/a').extract()
Out[20]: 
['<a class="tag" style="font-size: 28px" href="/tag/love/">love</a>',
 '<a class="tag" style="font-size: 26px" href="/tag/inspirational/">inspirational</a>',
 '<a class="tag" style="font-size: 26px" href="/tag/life/">life</a>',
 '<a class="tag" style="font-size: 24px" href="/tag/humor/">humor</a>',
 '<a class="tag" style="font-size: 22px" href="/tag/books/">books</a>',
 '<a class="tag" style="font-size: 14px" href="/tag/reading/">reading</a>',
 '<a class="tag" style="font-size: 10px" href="/tag/friendship/">friendship</a>',
 '<a class="tag" style="font-size: 8px" href="/tag/friends/">friends</a>',
 '<a class="tag" style="font-size: 8px" href="/tag/truth/">truth</a>',
 '<a class="tag" style="font-size: 6px" href="/tag/simile/">simile</a>']

In [21]:  response.xpath('//*[@class="tag-item"]/a').extract_first()
Out[21]: '<a class="tag" style="font-size: 28px" href="/tag/love/">love</a>'

In [22]:  response.xpath('//*[@class="tag-item"]/a/text()')
Out[22]: 
[<Selector xpath='//*[@class="tag-item"]/a/text()' data='love'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='inspirational'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='life'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='humor'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='books'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='reading'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='friendship'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='friends'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='truth'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='simile'>]

In [23]:  response.xpath('//*[@class="tag-item"]/a/text()').extract()
Out[23]: 
['love',
 'inspirational',
 'life',
 'humor',
 'books',
 'reading',
 'friendship',
 'friends',
 'truth',
 'simile']

In [24]: 
