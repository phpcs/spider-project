# -*- coding: utf-8 -*-
"""
获取根据一级分类获取二级分类
"""
import scrapy
from koolearn.items import CateItem


class KoolearnTikuCateSpider(scrapy.Spider):
    name = 'koolearn_tiku_cate'
    allowed_domains = ['www.koolearn.com']
    start_urls = [
        'www.koolearn.com/shiti/tk-2-16-0-0-1.html',
        'www.koolearn.com/shiti/tk-3-22-0-0-1.html',
        'www.koolearn.com/shiti/tk-4-24-0-0-1.html',
        'www.koolearn.com/shiti/tk-5-31-0-0-1.html'
    ]

    def start_requests(self):
        firstCate = ['金融类', '经济师', '教师考试', '人力行政']
        for i in self.start_urls:
            key = self.start_urls.index(i)
            #print firstCate[key]
            yield scrapy.Request('https://' + i, callback=self.parse, meta={'items': firstCate[key]})

    def parse(self, response):
        item = CateItem()
        cateDiv = response.xpath("//div[@class='i-filter-card']/div[@class='main']/div[2]/ul/li/a/@href").extract()
        cateDivText = response.xpath("//div[@class='i-filter-card']/div[@class='main']/div[2]/ul/li/a/text()").extract()
        for k, v in dict(zip(cateDivText, cateDiv)).items():
            item['exam_type'] = response.meta['items']
            item['cate'] = k
            item['url'] = v
            #print item
            yield item