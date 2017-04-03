# -*- coding: utf-8 -*-
import scrapy


class SuperbalitaSpider(scrapy.Spider):
    name = "superbalita"
    allowed_domains = ["http://www.sunstar.com.ph/superbalita-cebu/"]
    start_urls = ['http://http://www.sunstar.com.ph/superbalita-cebu//']

    def parse(self, response):
        for category in response.xpath('//ul[@id="superfish-10"]/li//a[contains(@href,"superbalita-cebu")]/text()').extract():
            yield scrapy.Request(response.urljoin(category),
                                callback=self.parse_category)


    def parse_category(self, response):
        for href in response.xpath('//div[@class="view-content"]/div/div/div//h3[@class="title"]//a/@href').extract():
            yield scrapy.Request(response.urljoin(href),
                                callback=self.parse_page)

        next_page = response.xpath('//div[@class="item-list"]//ul[@class="pager"]/li[contains(@class, "pager-current")]/following-sibling::li[1]//a/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_category)

    def parse_page(self, response):
        def parse-article(parlist):
            ' '.join(parlist)

        yield {
            'title': response.xpath('//h1[@class="title"]/text()').extract_first().strip(),
            'article': parse-article(response.xpath ('//div[@class = "field-item even"]/p/text()').extract()),
        }
