#_*_ coding:utf-8 _*_


#怎么执行程序 	：scray crawl pursuit(这是自己指定的爬虫名)
#scrapy crawl pursuit -o pursuit_teacher.json -t json

import scrapy

from mySpider.items import PursuitItem

class PursuitSpider(scrapy.spiders.Spider):
	#这些名称都是内置的
	name = "pursuit"
	allowd_damains = ["http://itcast.cn"]
	start_urls = ["http://www.itcast.cn/channel/teacher.shtml#ac"]
	

	def parse(self,response):
		# file_name = "teacher.html"
		# open(file_name,"wb+").write(response.body)
		items = []
		for site in response.xpath('//div[@class="li_txt"]'):
			teacher_name = site.xpath('h3/text()').extract()
			teacher_level = site.xpath('h4/text()').extract()
			teacher_info = site.xpath('p/text()').extract()

			item = PursuitItem()
			item['name'] = teacher_name
			item['level'] = teacher_level
			item['info']  = teacher_info

			items.append(item)

		return items









