# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


def update_link(link):
    return f'https://www.amazon.com{link}'


def take_first(l):
    return l[0]


def clean_date(date):
    return date[:12]


class AmazonScraperItem(scrapy.Item):
    title = scrapy.Field(input_processor=MapCompose(str.strip),
                         output_processor=TakeFirst()
                         )
    publisher = scrapy.Field(input_processor=MapCompose(str.strip),
                             output_processor=TakeFirst()
                             )
    link = scrapy.Field(input_processor=MapCompose(update_link),
                        output_processor=TakeFirst()
                        )
    posted_date = scrapy.Field(input_processor=MapCompose(str.strip, clean_date),
                               output_processor=TakeFirst()
                               )
    source_link = scrapy.Field(input_processor=MapCompose(str.strip),
                               output_processor=TakeFirst()
                               )
    scraped_date = scrapy.Field(input_processor=MapCompose(str.strip),
                               output_processor=TakeFirst()
                               )
