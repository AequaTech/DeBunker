from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SpiderSpider(CrawlSpider):
    name = 'spider'
    allowed_domains = ['lescienze.it']
    start_urls = ['http://www.lescienze.it']
    base_url = 'http://www.lescienze.it/'
    ROBOTSTXT_OBEY = True
    rules = [Rule(LinkExtractor(), follow=True)]




if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(SpiderSpider)
    process.start()