# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EditedItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    colour = scrapy.Field()
    size = scrapy.Field()
    reviews_count = scrapy.Field()
    reviews_score = scrapy.Field()
