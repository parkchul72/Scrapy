# -*- coding: utf-8 -*-
import scrapy
import logging
from tutorial.items import KobisItem

logging.basicConfig(level=logging.DEBUG)

class KobisSpider(scrapy.Spider):
    name = "kobis"
    allowed_domains = ["kobis.or.kr"]
    start_urls = [
        "http://www.kobis.or.kr/kobis/business/mast/mvie/searchMovieList.do"
    ]
    # Paging처리 요망 http://www.kobis.or.kr/kobis/business/mast/mvie/searchMovieList.do?curPage=

    def parse(self, response):
        search_cnt = int(response.xpath('//div[@class="board_top02"]/em').re(':\s+([0-9]+)')[0])
        page = search_cnt / 10
        if (search_cnt % 10) > 0: page += 1

        for next_page_no in range(1, page+1):
            url = response.urljoin("?curPage=" + str(next_page_no))
            yield scrapy.Request(url, callback=self.parse_next_page)

    def parse_next_page(self, response):
        for sel in response.xpath('//table[@class="boardList03"]/tbody/tr'):
            title_list = sel.xpath('td/@title').extract()
            item = KobisItem()
            item['title_kr'] = title_list[0]
            item['title_en'] = title_list[1]
            item['production_year'] = title_list[2]
            item['production_country'] = title_list[3]
            item['type'] = title_list[4]
            item['genre'] = title_list[5]
            item['production_state'] = title_list[6]
            item['director'] = title_list[7]
            item['production_company'] = title_list[8]
            yield item
