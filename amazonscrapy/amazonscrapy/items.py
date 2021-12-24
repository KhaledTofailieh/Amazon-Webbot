# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonScrapyItem(scrapy.Item):
    product_name = scrapy.Field()
    product_rate = scrapy.Field()
    product_author = scrapy.Field()
    product_date = scrapy.Field()
    img_link = scrapy.Field()
    price = scrapy.Field()
