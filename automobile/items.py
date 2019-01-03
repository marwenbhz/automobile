# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutomobileItem(scrapy.Item):
    # define the fields for your item here like:
    TITLE = scrapy.Field()
    LINK = scrapy.Field()
    PRICE = scrapy.Field()
    PICTURE = scrapy.Field()
    RAITING = scrapy.Field()