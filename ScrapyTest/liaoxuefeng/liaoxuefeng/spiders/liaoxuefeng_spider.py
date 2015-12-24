# -*- coding:utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from liaoxuefeng.items import LiaoxuefengItem

class LiaoxuefengSpider(Spider):
	name = "liaoxuefeng"
	start_urls = [
		"http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
	]
	
	def parse(self,response):
		sel = Selector(response)
		sites = sel.xpath('//div[@class="x-sidebar-left-content"]/ul[2]/li')
		items = []
		
		for site in sites:
			item = LiaoxuefengItem()
			
			title = site.xpath('a/text()').extract()
			link = site.xpath('a/@href').extract()
			desc = site.xpath('@id').extract()
			
			item['title'] = [t.encode('utf-8') for t in title]
			item['link'] = [l.encode('utf-8') for l in link]
			item['desc'] = [d.encode('utf-8') for d in desc]
			
			items.append(item)
			
		return items