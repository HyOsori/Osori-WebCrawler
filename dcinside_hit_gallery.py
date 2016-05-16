import scrapy
from scrapy.crawler import CrawlerProcess


class DCInsideHitGalleryCrawler(scrapy.Spider):
    name = 'DC Inside HitGallery - crawler'
    start_urls = ['http://gall.dcinside.com/board/lists/?id=hit&page=1']

    def parse(self, response):
        query_notice_title = '.list_thead > tr > td:nth-child(2) > a::text'
        query_notice_number = '.list_thead > tr > td:nth-child(1)::text'

        numbers = [int(text) for text in response.css(query_notice_number).extract() if text.isdigit()]
        titles = response.css(query_notice_title).extract()

        pairs = zip(numbers, titles)

        for number, pair in pairs:
            print number, pair

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(DCInsideHitGalleryCrawler)
process.start()
