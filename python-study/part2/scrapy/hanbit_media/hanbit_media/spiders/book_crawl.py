# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookCrawlSpider(CrawlSpider):
    name = 'book_crawl'
    allowed_domains = ['hanbit.co.kr']
    start_urls = [
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=001',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=002',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=003',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=004',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=005',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=006',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=007',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=008',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=009',
    ]

    rules = (
        Rule(LinkExtractor(allow=r'store/books/look.php\?p_code=.*'),
             callback='parse_item',
             follow=True),
        Rule(LinkExtractor(allow=
                           r'store/books/category_list.html\?page=\d+&cate_cd=00\d+&srt=p_pub_date'))
    )

    def parse_item(self, response):

        # book_title = .store_product_info_box > h3
        # //*[@id="container"]/div[1]/div[1]/div[1]/div[2]/h3
        # book_author = .info_list > li:first-child > span
        # //*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[1]/span
        # book_translator = .info_list > li:nth-child(2) > span
        # //*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/span
        # book_pub_date = .info_list > li:nth-child(3) > span
        # //*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[3]/span
        # book_isbn = .info_list > li:nth-child(5) > span
        # //*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[5]/span

        item = {
            'book_title': response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/h3/text()')
                .extract(),
            'book_author': response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[1]/span/text()')
                .extract(),
            'book_translator': response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/span/text()')
                .extract(),
            'book_pub_date': response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[3]/span/text()')
                .extract(),
            'book_isbn': response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[5]/span/text()')
                .extract(),
        }

        return item
