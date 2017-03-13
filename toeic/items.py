# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ToeicLesson(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()
    words = scrapy.Field()
    
    image_urls = Field()
    images = Field()
    pass

class ToeicWord(scrapy.Item):
	vocabulary = scrapy.Field()
	spelling = scrapy.Field()
	explain = scrapy.Field()
	meaning = scrapy.Field()
	image = scrapy.Field()
	en_example = scrapy.Field()
	vi_example = scrapy.Field()
	audio = scrapy.Field()
	pass

class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()