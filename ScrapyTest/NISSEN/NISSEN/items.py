# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NissenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    descript = scrapy.Field()
    URL = scrapy.Field()
    Photo = scrapy.Field()
    imagename = scrapy.Field()
    brandName = scrapy.Field()
    name = scrapy.Field()
