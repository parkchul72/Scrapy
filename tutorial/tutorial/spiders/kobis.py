# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import KobisItem

class KobisSpider(scrapy.Spider):
    name = "kobis"
    allowed_domains = ["kobis.org"]
    start_urls = [
        "http://www.kobis.or.kr/kobis/business/mast/mvie/searchMovieList.do"
    ]
    # Paging처리 요망 http://www.kobis.or.kr/kobis/business/mast/mvie/searchMovieList.do&curPage=

    def parse(self, response):
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
