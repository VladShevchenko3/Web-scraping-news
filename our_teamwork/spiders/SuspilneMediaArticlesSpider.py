import scrapy
from scrapy.http import Request
import json
import hashlib

from our_teamwork.items import OurTeamworkItem


class SuspilneMediaArticlesSpider(scrapy.Spider):
    name = 'volonteriarticles'
    ARTICLE_TITLE_TEXT_XPATH = '//h1/text()'
    ARTICLE_AUTHOR_TEXT_XPATH = '//a[@class="c-article-info-share__author"]/text()'
    ARTICLE_TEXT_XPATH = '//div[@class="c-article-content c-article-content--bordered"]//p/text()'

    def start_requests(self):
        data = []
        with open('suspilne_media.json') as json_file:
            data = json.load(json_file)

        for link_url in data[950:1000]:
            print('URL: ' + link_url['article_link'])
            request = Request(link_url['article_link'],
                              callback=self.parse)
            yield request

    def parse(self, response):
        item = OurTeamworkItem()
        item['article_uuid'] = hashlib.sha256(str(response.url).encode('utf-8')).hexdigest()
        item['article_title'] = response.xpath(self.ARTICLE_TITLE_TEXT_XPATH).extract()
        item['article_author'] = response.xpath(self.ARTICLE_AUTHOR_TEXT_XPATH).extract()
        item['article_text'] = "\n".join(response.xpath(self.ARTICLE_TEXT_XPATH).extract())
        yield item
