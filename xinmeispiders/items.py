# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XinmeispidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    domain = scrapy.Field()
    kw = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    brief = scrapy.Field()

class StackItem(scrapy.Item):
	title = scrapy.Field()
	url = scrapy.Field()
