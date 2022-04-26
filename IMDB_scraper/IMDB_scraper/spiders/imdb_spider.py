# to run 
# scrapy crawl imdb_spider -o results.csv

import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    
    start_urls = ['https://www.imdb.com/title/tt1641384/?ref_=nv_sr_srsg_0']

    def parse(self, response):
        yield scrapy.Request("https://www.imdb.com/title/tt1641384/fullcredits/?ref_=tt_ql_cl", self.parse_full_credits)
    
    def parse_full_credits(self, response):
        for link in [a.attrib["href"] for a in response.css("td.primary_photo a")]:
            yield scrapy.Request(response.urljoin(link), callback=self.parse_actor_page)
    
    def parse_actor_page(self, response):
        name = response.css("title::text").get()[:-7]
        for item in response.css("div.filmo-row"):
            show_name = item.css("b a::text").get()
            yield {
                "actor" : name,
                "movie_or_TV_name" : show_name
            }