# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OurTeamworkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article_link = scrapy.Field()
    article_uuid = scrapy.Field()
    article_text = scrapy.Field()
    article_title = scrapy.Field()
    article_author = scrapy.Field()