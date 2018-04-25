In [1]: from scrapy.selector import Selector

In [2]: %paste
html_doc = '''
<html>
  <head>
    <title>Title of the page</title>
  </head>
  <body>
    <h1>H1 Tag</h1>
    <h2>H2 Tag with <a href="#">link</a></h2>
    <p>First Paragraph</p>
    <p>Second Paragraph</p>
  </body>
</html>
'''

## -- End pasted text --

In [3]: sel = Selector(text=html_doc)

In [4]: sel.extract()
Out[4]: '<html>\n  <head>\n    <title>Title of the page</title>\n  </head>\n  <body>\n    <h1>H1 Tag</h1>\n    <h2>H2 Tag with <a href="#">link</a></h2>\n    <p>First Paragraph</p>\n    <p>Second Paragraph</p>\n  </body>\n</html>'

In [5]: sel.xpath('/html/head/title')
Out[5]: [<Selector xpath='/html/head/title' data='<title>Title of the page</title>'>]

In [6]: sel.xpath('/html/head/title/text()')
Out[6]: [<Selector xpath='/html/head/title/text()' data='Title of the page'>]

In [7]: sel.xpath('/html/head/title/text()').extract()
Out[7]: ['Title of the page']

In [8]: sel.xpath('/html/head/title/text()').extract_first()
Out[8]: 'Title of the page'

In [9]: sel.xpath('/html/head/title').extract()
Out[9]: ['<title>Title of the page</title>']

In [10]: sel.xpath('//title').extract()
Out[10]: ['<title>Title of the page</title>']

In [11]: sel.xpath('//text()').extract()
Out[11]: 
['\n  ',
 '\n    ',
 'Title of the page',
 '\n  ',
 '\n  ',
 '\n    ',
 'H1 Tag',
 '\n    ',
 'H2 Tag with ',
 'link',
 '\n    ',
 'First Paragraph',
 '\n    ',
 'Second Paragraph',
 '\n  ',
 '\n']

In [12]: sel.xpath('/html/body/p').extract()
Out[12]: ['<p>First Paragraph</p>', '<p>Second Paragraph</p>']

In [13]: sel.xpath('//p').extract()
Out[13]: ['<p>First Paragraph</p>', '<p>Second Paragraph</p>']

In [14]: sel.xpath('//p[1]').extract()
Out[14]: ['<p>First Paragraph</p>']

In [15]: sel.xpath('//p[2]').extract()
Out[15]: ['<p>Second Paragraph</p>']

In [16]: sel.xpath('//p[2]')[0].extract()
Out[16]: '<p>Second Paragraph</p>'

In [17]: sel.xpath('//p[2]')[1].extract()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-17-c55d8d6995e3> in <module>()
----> 1 sel.xpath('//p[2]')[1].extract()

/media/merlin/DarthVader/python/web-scraper/venv/lib/python3.5/site-packages/parsel/selector.py in __getitem__(self, pos)
     59 
     60     def __getitem__(self, pos):
---> 61         o = super(SelectorList, self).__getitem__(pos)
     62         return self.__class__(o) if isinstance(pos, slice) else o
     63 

IndexError: list index out of range

In [18]: sel.xpath('//p')[1].extract()
Out[18]: '<p>Second Paragraph</p>'

In [19]: sel.xpath('//p')[0].extract()
Out[19]: '<p>First Paragraph</p>'

In [20]: sel.xpath('//p/text()')[0].extract()
Out[20]: 'First Paragraph'

In [21]: sel.xpath('//p/text()').extract_first()
Out[21]: 'First Paragraph'

In [22]: sel.xpath('//h2').extract()
Out[22]: ['<h2>H2 Tag with <a href="#">link</a></h2>']

In [23]: sel.xpath('//h2/a').extract()
Out[23]: ['<a href="#">link</a>']

In [24]: sel.xpath('//h2/a/@href').extract()
Out[24]: ['#']

In [25]: sel.css('h2')
Out[25]: [<Selector xpath='descendant-or-self::h2' data='<h2>H2 Tag with <a href="#">link</a></h2'>]

In [26]: 
