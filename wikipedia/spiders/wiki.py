import scrapy
from wikipedia.helpers.xpaths import XPATH
from wikipedia.items import WikipediaItem, WikipediaItemLoader


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['pt.wikipedia.org']
    start_urls = ['https://pt.wikipedia.org/wiki/Angola']

    def parse(self, response):
        article = WikipediaItemLoader(item=WikipediaItem(), response=response)
        article.add_value('url', response.url)
        article.add_xpath('title', XPATH.title)
        article.add_xpath('description', XPATH.description)
        article.add_xpath('image_url', XPATH.image_url)

        return article.load_item()
