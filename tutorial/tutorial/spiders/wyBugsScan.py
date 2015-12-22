# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import wyBugsScanItem
from scrapy.selector import Selector

class WybugsscanSpider(scrapy.Spider):
    name = "wyBugsScan"
    allowed_domains = ["wooyun.org"]
    start_urls = (
        'http://www.wooyun.org/bugs/new_submit/page/1',
    )

    def parse(self, response):
		sel = Selector(response)
		# content = sel.xpath('//td/a/@href').extract()
		# print content
		for site in sel.xpath('//tr'):
			item = wyBugsScanItem()
			item['bugDate'] = site.xpath('th/text()').extract()
			item['bugUrl'] = site.xpath('td/a/@href').extract()
			item['bugTitle'] = site.xpath('td/a/text()').extract()
			item['bugAuthor'] = site.xpath('th/a/text()').extract()
			# title = site.xpath('a/text()').extract()
			print item['bugDate']
			# yield item
