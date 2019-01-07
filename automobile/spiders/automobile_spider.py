# -*- coding: utf-8 -*-
from __future__ import print_function
from automobile.items import AutomobileItem
from scrapy import Request
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

        annonces = response.css('article.list-entry')
        for annonce in annonces:

            try:
                title = annonce.css('h3.vehicle-title::text').extract_first().strip()
            except:
                print('ERROR TITLE PARSE...' + response.url)
            try:
                link = response.urljoin(annonce.css('a.vehicle-data::attr(href)').extract_first())
            except:
                print('ERROR LINK PARSE...' + response.url)
            try:
                price = annonce.css('p.seller-currency::text').extract_first().strip()
            except:
                print('ERROR PRICE PARSE...' + response.url)
            try:
                picture = annonce.css('img.img-thumbnail::attr(src)').extract_first()
            except:
                print('ERROR TITLE PARSE...' + response.url)
            try:
                raiting = annonce.css('div.star-rating-s::attr(data-rating)').extract_first()
            except:
                print('ERROR RAITING PARSE...' + response.url)
            '''
            try:
                postal_code = annonce.css('div.u-text-grey-60 > p::text').extract_first()[:5] if annonce.css('div.u-text-grey-60 > p::text').extract_first()[:5].isdigit() == True else ' '
            except:
                print('ERROR POSTAL CODE PASRSE...' + response.url)
            '''
            yield Request(link, callback=self.parse_item, meta={'link': link, 'title': title, 'price': price, 'picture': picture, 'raiting': raiting})


        relative_next_url = response.xpath('//a[@class="pagination-nav pagination-nav-right btn btn--muted btn--s"]/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)
	yield Request(absolute_next_url, callback=self.parse)


    def parse_item(self, response):
        item = AutomobileItem()

        item['TITLE'] = response.meta.get('title')
        item['LINK'] = response.meta.get('link')
        item['PRICE'] = response.meta.get('price')

        '''
        Don't need picture in result.csv
        item['PICTURE'] = response.meta.get('picture')
        '''

        item['RAITING'] = response.meta.get('raiting')
        item['PHONE'] = response.css('p.seller-phone::text').extract_first().strip()
        adress = response.css('div.u-margin-bottom-9 > p::text').extract()
        item['ADRESS'] = adress[1].strip() + ' ' + adress[2].strip() if len(adress) == 3 else ' '


        yield item
