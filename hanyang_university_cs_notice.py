import scrapy
from scrapy.crawler import CrawlerProcess


class CSHanyangCrawler(scrapy.Spider):
    name = 'cs.hanyang - crawler'
    start_urls = ['http://cs.hanyang.ac.kr/?page=intro/intro03']

    def parse(self, response):
        query_notice_title = '.tover > div > a::text'
        query_notice_number = 'body > table > tr:nth-child(2) > td > table > tr:nth-child(2) > td:nth-child(2) >' \
                              ' div > table:nth-child(7) > tr > td > table > tr:nth-child(1) > td:nth-child(1) >' \
                              ' font::text'

        numbers = [int(text) for text in response.css(query_notice_number).extract() if text.isdigit()]
        titles = response.css(query_notice_title).extract()

        pairs = zip(numbers, titles)

        for number, pair in pairs:
            print number, pair

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(CSHanyangCrawler)
process.start()
