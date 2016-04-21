# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi       #导入twisted的包
import MySQLdb
import MySQLdb.cursors

from scrapy import signals
import json
import codecs
import urllib

class NissenPipeline(object):
    def process_item(self, item, spider):
        return item

class MYSQLWithDataPipeline(object):
    def __init__(self):
        self.file = codecs.open('Yamaxun_iPhone.txt', 'w', encoding='utf-8')
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
        db = 'productdata',
        user = 'root',
        passwd = 'DESHENG',
        cursorclass = MySQLdb.cursors.DictCursor,
        charset = 'utf8',
        use_unicode = False)

    def process_item(self, item, spider):
        #print "test---------------->>>>>>>:price:",len(item["price"]),"descript:" ,item["descript"],"URL:", item["URL"],"Photo:", item["Photo"]
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    def _conditional_insert(self, tx, item):
        #print "_conditional_insert---------------->>>>>>>:price:",len(item["price"]),"descript:" ,len(item["descript"]),"URL:", len(item["URL"]),"Photo:", len(item["Photo"])
        for i in range(len(item["URL"])):
            sql = "insert into nissenproduct (name,brand_name,price,descript,URL,Photo,imagename) values (%s, %s, %s, %s, %s, %s, %s)"
            #sql.join([item["price"][i], item["descript"][i], item["URL"][i], item["Photo"][i]])
            #print "test---------------->>>>>>>:name",item["name"][i],"brand_name",item["brand_name"][i],"price:",item["price"][i],"descript:" ,item["descript"][i],"URL:", item["URL"][i],"Photo:", item["Photo"][i]
            tx.execute(sql,(item["name"][i], item["brandName"][i],item["price"][i], item["descript"][i], item["URL"][i], item["Photo"][i],item["Photo"][i].split('/')[-1]))
            imagepath = item["Photo"][i].split('/')[-1]
            urllib.urlretrieve('http://www.nissen.co.jp'+item["Photo"][i],'download/'+imagepath)
        #print "test---------------->>>>>>>:price:",item["price"],"descript:" ,item["descript"],"URL:", item["URL"],"Photo:", item["Photo"]