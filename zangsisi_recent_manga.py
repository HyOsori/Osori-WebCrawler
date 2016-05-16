#-*- coding: utf-8 -*-

import scrapy
from scrapy.crawler import CrawlerProcess

class ZangsisiCrawler(scrapy.Spider):
    name = 'zangsisi'
    start_urls = ['http://zangsisi.net/']

    def parse(self, response):
        query_date      = "#recent-manga > div > li > div.date::text"
        query_contents  = "#recent-manga > div > li > div.contents > a::text"
        query_details   = "#recent-manga > div > li > div.contents > a > span::text"

        date     =  response.css(query_date).extract()
        contents =  response.css(query_contents).extract()
        details  =  response.css(query_details).extract()

        print date[0]

        results = zip(contents, details)

        for content, detail in results:
            print content, detail

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(ZangsisiCrawler)
process.start()