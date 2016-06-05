import scrapy

from scrapy.crawler import CrawlerProcess

class SteamSpider(scrapy.Spider):
    name = 'steam sale off'
    start_urls =['http://store.steampowered.com/search/?specials=1&os=win#sort_by=_ASC&specials=1&page=1']

    def parse(self, response):
        query_steam_sale='#search_result_container'
        print response.css(query_steam_sale).extract()
        numberList = 0

        titles = response.css('#search_result_container > div > a > div:nth-child(2) > div:nth-child(1) > span::text').extract()
        saleOff = response.css('#search_result_container > div:nth-child(2) > a > div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_discount.responsive_secondrow>span::text').extract()
        defaultPrice = response.css('#search_result_container > div:nth-child(2) > a > div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_price.discounted.responsive_secondrow>span>strike::text').extract()
        results = zip(titles, saleOff, defaultPrice)
        for title in results:
            print title

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(SteamSpider)
process.start()
