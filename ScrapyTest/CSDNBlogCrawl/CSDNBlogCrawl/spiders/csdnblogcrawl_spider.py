# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.selector import Selector
from CSDNBlogCrawl.items import CsdnblogcrawlItem


class CsdnblogcrawlSpider(CrawlSpider):

	name = 'CSDNBlogCrawl'
	download_delay = 2
	allowed_domains = ['blog.csdn.net']
	start_urls = ['http://blog.csdn.net/u012150179/article/details/11749017']

	# rules = [
		# Rule(LinkExtractor(allow='/u012150179/article/details',
					# restrict_xpaths='//li[@class="next_article"]'),
			# follow = True),
			
		# Rule(LinkExtractor(allow='/u012150179/article/details'),
			# callback='parse_item',
			# follow = False)
	# ]
	
	rules = [
		Rule(LinkExtractor(allow='/u012150179/article/details',
					restrict_xpaths='//li[@class="next_article"]'), 
		callback='parse_item', 
		follow=True)
	]

	def parse_item(self, response):	
		item = CsdnblogcrawlItem()
		sel = Selector(response)
		blog_url = str(response.url)
		blog_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()
		
		item['blog_name'] = [n.encode("utf-8") for n in blog_name]
		item['blog_url'] = blog_url.encode('utf-8')
		#i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
		#i['name'] = response.xpath('//div[@id="name"]').extract()
		#i['description'] = response.xpath('//div[@id="description"]').extract()
		yield item
