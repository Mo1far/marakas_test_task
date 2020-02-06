# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class AmazonScraperPipeline(object):
    def process_item(self, item, spider):
        item.setdefault('publisher', 'No editorial recommendation')
        item.setdefault('link', '')
        item.setdefault('posted_date', '')
        item.setdefault('title', '')
        return item
