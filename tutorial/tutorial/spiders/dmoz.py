from scrapy.selector import Selector
from scrapy.spiders import Spider
from tutorial.items import DmozItem

class DmozSpider(Spider):
	name = 'dmoz'
	allowned_domains =['dmoz.org']
	start_urls = [
			"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",  
        	"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
			]

	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//ul/li')
		for site in sites:
			item = DmozItem()
			item['title'] = site.xpath('a/text()').extract()
			# title = site.xpath('a/text()').extract()
			print item['title']
			# yield item


		# print response.body