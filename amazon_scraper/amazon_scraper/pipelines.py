# -*- coding: utf-8 -*-
class AmazonScraperPipeline(object):
    def process_item(self, item, spider):
        item.setdefault('publisher', 'No editorial recommendation')
        item.setdefault('link', ' ')
        item.setdefault('posted_date', ' ')
        item.setdefault('title', ' ')
        return item
