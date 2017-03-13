# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy import Request

from toeic.items import ToeicLesson
from toeic.items import ToeicWord

class ToeicSpider(Spider):
	name = "toeic"
	allowed_domains = ["600tuvungtoeic.com"]
	start_urls = [
		"http://600tuvungtoeic.com",
	]

	def parse(self, response):
		res_lessons = response.css('div.gallery-item')
		for item in res_lessons:
			lesson = ToeicLesson()
			url = "http://600tuvungtoeic.com/" + item.css('div.overlay a::attr(href)').extract_first()
			lesson['url'] = url
			lesson['title'] = item.css('div.content-gallery h3::text').extract_first()
			lesson['image'] = item.css('div.image img::attr(src)').extract_first()
			details_lesson_request = Request(url, callback=self.parse_details_lesson)
			details_lesson_request.meta['lesson'] = lesson
			yield details_lesson_request
		yield lesson
		

	def parse_details_lesson(self, response):
		lesson = response.meta['lesson']
		lesson['words'] = []
		words = response.css('div.tuvung')

		for item in words:
			word = ToeicWord()
			word['vocabulary'] = item.css('div.noidung span::text').extract_first()
			word['spelling'] = item.css('div.noidung span::text').extract()[1]
			word['image'] = "http://600tuvungtoeic.com/" + item.css('div.hinhanh img::attr(src)').extract_first()
			word['explain'] = item.xpath('span[contains(., "Giải")]/following-sibling::text()').extract_first()
			word['meaning'] = "Du lieu test meaning"
			word['en_example'] = "Du lieu test en_example"
			#item.css('following-sibling::span.bold::text').extract()[0]
			word['vi_example'] = "Du lieu test vi_example"
			word['audio'] = "http://600tuvungtoeic.com/" + item.css('div.noidung audio source::attr(src)').extract_first()
			print "word " + word['explain']
			print "Lesson!!!" + lesson['title'] + " " + lesson['url']
			lesson['words'].append(word)
			
		return lesson


