# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy.loader import ItemLoader
from scrapy_splash import SplashRequest

from amazon_scraper.items import AmazonScraperItem

from amazon_scraper.utils import get_start_urls


class AmazonEditioralRecommendationsSpider(scrapy.Spider):
    name = 'amazon'

    lua_script = """
                function main(splash, args)
                assert (splash:go(args.url))
                assert (splash:wait(8.5))
                splash:wait(8.5)
                return {
                    html = splash:html(),
                    png = splash:png(),
                    har = splash:har(),
                }
                end
              """

    date = datetime.datetime.now()
    FEED_URI = f'KEYWORDWINNER_{date.year}_{date.month}_{date.day}.csv'
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': FEED_URI
    }

    def start_requests(self):
        self.start_urls = get_start_urls()
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='execute',
                                args={
                                    'lua_source': self.lua_script,
                                    'wait': 8.5,
                                })

    def parse(self, response):
        loader = ItemLoader(item=AmazonScraperItem(), response=response)

        source_link = response.url
        scraped_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        loader.add_value('scraped_date', scraped_date)
        loader.add_value('source_link', source_link)
        loader.add_css('publisher', '.a-fixed-left-grid-col>div.a-row>a.a-link-normal::text')
        loader.add_css('link', 'div.a-spacing-medium>.a-link-normal.s-no-hover::attr(href)')
        loader.add_css('posted_date', '.a-spacing-small>.a-color-secondary::text')
        loader.add_css('title', 'h5.a-spacing-small>span.a-size-large::text')

        return loader.load_item()
