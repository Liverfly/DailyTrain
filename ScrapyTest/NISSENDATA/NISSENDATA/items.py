# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NissendataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #商品类型 
    productType = scrapy.Field()
    #商品品牌
    productBrand = scrapy.Field()
    #商品介绍
    productIntroduce = scrapy.Field()
    #商品用途
    productPurpose = scrapy.Field()
    #商品番号
    productDesignation = scrapy.Field()
    #商品来源
    productSource = scrapy.Field()
    #商品地址
    productAddress = scrapy.Field()
    #关联商品名称和地址
    similarProduct = scrapy.Field()