# -*- coding: utf-8 -*-
import scrapy

from baidusearch.items import BaidusearchItem

class BaiduSpider(scrapy.Spider):
	name = "baidu"
	allowed_domains = ["test.com"]
	start_url = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
	]
	
	def parse(self,response):
		for sel in response.xpath('//div[@class="result c-container"]'):
			item = BaidusearchItem()
			item['name'] = sel.xpath('a/text()').extract()
			item['url'] = sel.xpath('a/@href').extract()
			item['des'] = sel.xpath('text()').extract()
			yield item