# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SmilecatCrawlSpider(CrawlSpider):
    name = 'smilecat_crawl'
    allowed_domains = ['smilecat.com']
    start_urls = [
        'http://www.smilecat.com/mall/category.jsp?commodity=6002&size=5504&theme=0&left=6501&page_no=1&sort=1',
        'http://www.smilecat.com/mall/category.jsp?commodity=6002&size=5504&theme=0&left=6501&page_no=2&sort=1',
        'http://www.smilecat.com/mall/category.jsp?commodity=6002&size=5504&theme=0&left=6501&page_no=3&sort=1',
        'http://www.smilecat.com/mall/category.jsp?commodity=6002&size=5504&theme=0&left=6501&page_no=4&sort=1',
        'http://www.smilecat.com/mall/category.jsp?commodity=6002&size=5504&theme=0&left=6501&page_no=5&sort=1',
        'http://www.smilecat.com/mall/category.jsp?commodity=6002&size=5504&theme=0&left=6501&page_no=6&sort=1',
        'http://www.smilecat.com/mall/category.jsp?commodity=6002&size=5504&theme=0&left=6501&page_no=7&sort=1',
        'http://www.smilecat.com/mall/category.jsp?commodity=6002&size=5504&theme=0&left=6501&page_no=8&sort=1',
        'http://www.smilecat.com/mall/category.jsp?commodity=6002&size=5504&theme=0&left=6501&page_no=9&sort=1',
        'http://www.smilecat.com/mall/category.jsp?commodity=6002&size=5504&theme=0&left=6501&page_no=10&sort=1',
    ]

    rules = (
        Rule(LinkExtractor(allow=r'mall\/info_calendar\.jsp\?code1=\d+&code2=\d+&code3=\d+.*'),
             callback='parse_item',
             follow=True),
        Rule(LinkExtractor(allow=r'mall/category.jsp?commodity=6002&size=5504&theme=0&left=6501&page_no=\d+&&sort=1'))
    )

    def parse_item(self, response):
        item = {
            'name': response.xpath('//*[@id="commodity_name"]/text()').extract(),
            'price': response.xpath('//*[@id="price_span"]/text()').extract(),
            'point': response.xpath('//*[@id="commodity_reward"]/text()').extract_first().replace('[', '')
        }
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
