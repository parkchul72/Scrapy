# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class KobisItem(scrapy.Item):
    title_kr = scrapy.Field()
    title_en = scrapy.Field()
    production_year = scrapy.Field()
    production_country = scrapy.Field()
    type = scrapy.Field()
    genre = scrapy.Field()
    production_state = scrapy.Field()
    director = scrapy.Field()
    production_company = scrapy.Field()