import scrapy


class OurTeamworkItem(scrapy.Item):
    article_link = scrapy.Field()
    article_uuid = scrapy.Field()
    article_text = scrapy.Field()
    article_title = scrapy.Field()
    article_author = scrapy.Field()
