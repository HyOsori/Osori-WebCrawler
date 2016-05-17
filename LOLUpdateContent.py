import scrapy
from scrapy.crawler import CrawlerProcess


class LOLUpdateContent(scrapy.Spider):
    name = 'LOL Update Content'
    start_urls = ['http://www.leagueoflegends.co.kr/?m=news&cate=update']
    def parse(self, response):
        url = response.css("td.tleft a::attr(href)").extract()
        title = response.css("td.tleft a::text").extract()

        print 'League of Legends Update Note'

	final = zip(title,url)

	for title,url in final:
		print 'http://www.leagueoflegends.co.kr' + url + ' ' + title

    pass

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(LOLUpdateContent)
process.start()
