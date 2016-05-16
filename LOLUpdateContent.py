import scrapy
from scrapy.crawler import CrawlerProcess


class LOLUpdateContent(scrapy.Spider):
    name = 'LOL Update Content'
    start_urls = ['http://www.leagueoflegends.co.kr/?m=news&cate=update']
    def parse(self, response):
        url = response.css("td.tleft a::attr(href)").extract()
        title = response.css("td.tleft a::text").extract()

        total = []
        print 'League of Legends Update Note'

        for i in range(10):
            temp_title = title[i]
            temp_url = url[i]
            total.append((temp_title,temp_url))


        for temp_title,temp_url in total:
            print 'http://www.leagueoflegends.co.kr' + temp_url + ' ' + temp_title

    pass

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(LOLUpdateContent)
process.start()