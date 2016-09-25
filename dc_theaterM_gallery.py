import scrapy
from scrapy.crawler import CrawlerProcess
import logging

class TheaterM_gallery_Crawler(scrapy.Spider):
    name = 'DC Inside Theater Musical gallery recommend'
    start_urls = ['http://gall.dcinside.com/board/lists/?id=theaterM&page=1&exception_mode=recommend']
    base_urls = 'http://gall.dcinside.com'
    logging.getLogger('scrapy').propagate = False

    def parse(self, response):

        title = '.list_thead > tr > td:nth-child(2) > a::text'
        number = '.list_thead > tr > td:nth-child(1)::text'
        href = '.list_thead > tr > td:nth-child(2) > a:nth-child(1)::attr(href)'
        numbers = [int(text) for text in response.css(number).extract() if text.isdigit()]
        titles = response.css(title).extract()[4:]
        refs = (response.css(href).extract())[6:]
        results = zip(numbers, titles, refs)
        for number, title, ref in results:
            print(str(number) + "&^%987&^%" + title + "&^%987&^%" + self.base_urls + ref)

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(TheaterM_gallery_Crawler)
process.start()
