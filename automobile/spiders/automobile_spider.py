# -*- coding: utf-8 -*-
import scrapy


class AutomobileSpiderSpider(scrapy.Spider):
    name = 'automobile_spider'
    allowed_domains = ['automobile.fr']
    start_urls = ['https://www.automobile.fr/cat%C3%A9gorie/voiture/vhc:car,dmg:false']
    custom_settings = {
    'LOG_FILE': 'logs/automobile.log',
    'LOG_LEVEL':'ERROR'
     }


    def parse(self, response):
        print('PROCESSING...' + response.url)
