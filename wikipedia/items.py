# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader


class WikipediaItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    image_url = scrapy.Field()
    image = scrapy.Field()


class WikipediaItemLoader(ItemLoader):
    def format_image(image_url):
        return "http:" + image_url

    default_input_processor = TakeFirst()
    default_output_processor = TakeFirst()

    image_url_in = MapCompose(format_image)
    description_in = Join('')

