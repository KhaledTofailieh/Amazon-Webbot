import scrapy
from ..items import AmazonScrapyItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/s?k=funny&i=stripbooks-intl-ship&ref=nb_sb_noss'
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getProductItem(self, response):
        all_items = response.css('.s-latency-cf-section')
        item = AmazonScrapyItem()
        for item_ in all_items:
            item['product_name'] = item_.css('.a-color-base.a-text-normal::text').extract()
            item['product_author'] = item_.css('.a-color-secondary .a-row .a-size-base+ .a-size-base , .a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
            item['product_rate'] = item_.css('.a-icon-alt::text').extract()
            date = item_.css('.a-color-secondary.a-text-normal::text').extract()
            print(date)
            item['product_date'] = date
            # .a - color - secondary.a - text - normal
            # prices = item_.css('.a-link-normal.a-text-bold , .a-price-fraction , .a-price-whole').css('::text').extract()
            yield item
        yield None

    def start_requests(self):
        pass

    def parse(self, response, **kwargs):
        for item in self.getProductItem(response=response):
            yield item
