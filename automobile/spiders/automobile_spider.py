# -*- coding: utf-8 -*-
import scrapy


class AutomobileSpiderSpider(scrapy.Spider):
    name = 'automobile_spider'
    allowed_domains = ['automobile.fr']
    start_urls = ['http://automobile.fr/']

    def parse(self, response):
        pass
