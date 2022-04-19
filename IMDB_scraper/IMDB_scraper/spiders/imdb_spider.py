# to run 
# scrapy crawl imdb_spider -o movies.csv

import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    
    start_urls = ['https://www.imdb.com/title/tt1641384/?ref_=nv_sr_srsg_0']

    def parse(self, response):
        yield scrapy.Request("https://www.imdb.com/title/tt1641384/fullcredits/?ref_=tt_ql_cl", callback=parse_full_credits(self,response))
    
    def parse_full_credits(self, response):
        yield [a.attrib["href"] for a in response.css("td.primary_photo a")]