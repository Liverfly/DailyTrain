from lxml import etree
from StringIO import StringIO

xmlfile="""<?xml version="1.0" encoding="ISO-8859-1"?>
<bookstore>

<book category="COOKING">
  <title lang="en">Everyday Italian</title>
  <author>Giada De Laurentiis</author>
  <year>2005</year>
  <price>30.00</price>
</book>

<book category="CHILDREN">
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

<book category="WEB">
  <title lang="en">XQuery Kick Start</title>
  <author>James McGovern</author>
  <author>Per Bothner</author>
  <author>Kurt Cagle</author>
  <author>James Linn</author>
  <author>Vaidyanathan Nagarajan</author>
  <year>2003</year>
  <price>49.99</price>
</book>

<book category="WEB">
  <title lang="ch">Learning XML</title>
  <author>Erik T. Ray</author>
  <year>2003</year>
  <price>39.95</price>
</book>

</bookstore>
"""

f=StringIO(xmlfile)
tree=etree.parse(f)

tree.xpath('//title')[0].tag
tree.xpath('//title')[0].text

##  closure for query
def QResF(tree):
	def QResFunction(query):
		print query
		res=tree.xpath(query)
		try:
			reslsT=[q.tag for q in res]
			resls=[q.text for q in res]
			print zip(reslsT,resls)
		except AttributeError:
			resls='\n'.join([q for q in res])
			print resls
		return len(res)
	return QResFunction

Q=QResF(tree)

Q('//title')
Q('//author')
Q('/bookstore/book/title')
Q('/bookstore/book[price > 25]')
Q('//book/title[@*]')
Q('//@*')
Q('//*')
Q('//@lang')
Q('//book/title| //book/price')
Q('//bookstore/child::year')
Q('//nothing')
Q('/book/child::year')
Q('//book/child::*')
Q('//book/title[@lang]')

Q('//text()')