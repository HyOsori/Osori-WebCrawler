#-*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess


class NdhsMealCrawler(scrapy.Spider):
    name = 'NDHS_CRAWLER'
    start_urls = ['http://www.ndhs.or.kr/2014/sub_community/sub2.php']

    def parse(self, response):
        l = response.css("div > div > div > div > div > div > table > tbody > tr > th").extract()
        m = response.css("div > div > div > div > div > div > table > tbody > tr > td").extract()

        for i in range(len(l)):
            if i == 5 :
                l[i] = l[i][40:-12]
            elif i == 6:
                l[i] = l[i][38:-12]
            else:
                l[i] = l[i][16:-5]

        for i in range(len(m)):
            m[i] = m[i][4:-5]

        for i in range(7):
            print l[i]
            print "조식 : ",
            print m[3*i + 0]
            print "중식 : ",
            print m[3*i + 1]
            print "석식 : ",
            print m[3*i + 2 ]

    pass

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MyCrawler)
process.start()
