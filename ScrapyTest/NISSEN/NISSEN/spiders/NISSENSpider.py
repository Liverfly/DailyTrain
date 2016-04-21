from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
#from JD.misc.log import *  
from NISSEN.items import NissenItem 
from NISSEN.Util import *
import urllib
class NISSENSpider(CrawlSpider):
    name = 'NISSEN'
    download_delay = 2
    allowed_domains = ['www.nissen.co.jp']
    start_urls = ['http://www.nissen.co.jp/cate008/event/BH15SU101/sho_index/BH15SU101_005_004_000-01.htm?2nd=ntop_osusume2_004']

    #rules = [
    #    Rule(LinkExtractor(allow='/s/ref',
    #             restrict_xpaths="//a[@id='pagnNextLink']/@href"),
    #        follow = True),

    #    Rule(LinkExtractor(allow='/s/ref'),
    #    callback='parse',
    #    follow = False)
    #]

    #with open('product.txt','r') as f:
    #     start_urls = f.read().split(',')
    #处理response
    def parse(self,response):
    #在处理response传来的页面时，先判断有无下一页，有的话链接加到URL的集合里面
        NextPage = response.xpath("//li[@class='next']//a/@href").extract()
        sites =response.xpath("//div[@id='search_listArea']//ul[@class='item_column']/li").extract()
        #分别对每个手机商品的信息进行处理
        #items = []
        #//div[@id="search_listArea"]//ul//li//div//p[@class="name"]
        for site in sites:
            NISSEN = NissenItem() 
            #print "YamaxunSpider----------------->site:" , site
            NISSEN['brandName'] = Selector(text=site).xpath("//div[@class='itembox']/p[@class='brandName']/text()").extract()
            NISSEN['name'] = Selector(text=site).xpath("//div[@class='itembox']/p[@class='name']/a/text()").extract()
            NISSEN['price'] = Selector(text=site).xpath("//div[@class='itembox']/p[@class='price']/text()").extract()
            #NISSEN['price'] = Selector(text=site).xpath("//li/div/div[4]/div[1]/a/span[1]/text()").extract() #手机价格
            NISSEN['descript'] = Selector(text=site).xpath("//div[@class='itembox']/p[@class='copy']/text()").extract()
            NISSEN['URL'] = Selector(text=site).xpath("//div[@class='itembox']/p[@class='thumb']/a/@href").extract()
            NISSEN['Photo'] = Selector(text=site).xpath("//div[@class='itembox']/p[@class='thumb']/a/img/@src").extract()
            #NISSEN['imagename'] = NISSEN['Photo'][0].split('/')[-1]
            #print "YamaxunSpider----------------->price:" ,Yamaxun['price'],"descript:",Yamaxun['descript'],"URL:",Yamaxun['URL'],"Photo:",Yamaxun['Photo']
            yield NISSEN
            #items.append(Yamaxun)  
            #print 'parsed ' + str(Yamaxun)
        #return items  #item最后会传递给pipline处理
        if(NextPage !=[]):  
            #print "YamaxunSpider----------------->nextlink:" ,'http://www.amazon.cn' + NextPage[0]
            req = Request(url='http://www.nissen.co.jp' + NextPage[0], callback=self.parse)
            yield req

    def _process_request(self, request):  
     #   info('process ' + str(request))  
        return request