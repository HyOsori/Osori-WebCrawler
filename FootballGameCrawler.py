import scrapy
from scrapy.crawler import CrawlerProcess


class FootballGameCrawler(scrapy.Spider):
    name = 'FootballGameCrawler'
    start_urls = ['http://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%ED%95%B4%EC%99%B8%EC%B6%95%EA%B5%AC+%EA%B2%BD%EA%B8%B0+%EA%B2%B0%EA%B3%BC&tltm=1']

    def parse(self, response):
        time = response.css('#testTbl > table > tbody > tr > td.cont1 > em::text').extract()
        league = response.css('#testTbl > table > tbody > tr > td.cont1 > span > a::text').extract()
        team1 = response.css('#testTbl > table > tbody > tr > td.cont2 > a > div > div.home > span::text').extract()
        score1 = response.css('#testTbl > table > tbody > tr > td.cont2 > a > div > div.home > em::text').extract()
        score2 = response.css('#testTbl > table > tbody > tr > td.cont2 > a > div > div.away > em::text').extract()
        team2 = response.css('#testTbl > table > tbody > tr > td.cont2 > a > div > div.away > span::text').extract()
        table = zip(time, league, team1, score1, score2, team2)
        for item in table:
            print item[0], item[1], item[2], item[3], item[4], item[5]

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(FootballGameCrawler)
process.start()