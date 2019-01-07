from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from automobile.spiders.automobile_spider import AutomobileSpiderSpider

process = CrawlerProcess(get_project_settings())
process.crawl(AutomobileSpiderSpider)
process.start()
