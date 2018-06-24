# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        


    	quotes = response.xpath('//*[@class="quote"]')
    	for quote in quotes:
        	h1_tag = response.xpath('//h1/a/text()').extract_first()
          tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

    	yield {'H1 tag': h1_tag, 'Tags': tags}
