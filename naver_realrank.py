import scrapy
from scrapy.crawler import CrawlerProcess


class NaverRealRankCrawler(scrapy.Spider):
    name = 'naver realrank'
    start_urls = ['http://www.naver.com']

    def parse(self, response):
        query_real_rank = '#realrank'
        print response.css(query_real_rank).extract()

        titles = response.css('#realrank > li > a::attr(title)').extract()
        urls = response.css('#realrank > li > a::attr(href)').extract()

        results = zip(titles, urls)

        for title, url in results:
            print title, url

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(NaverRealRankCrawler)
process.start()
