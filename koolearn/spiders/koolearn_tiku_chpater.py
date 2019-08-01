# -*- coding: utf-8 -*-
import scrapy
from koolearn.db import Db
from koolearn.items import ChapterItem

class KoolearnTikuChpaterSpider(scrapy.Spider):
    name = 'koolearn_tiku_chpater'
    allowed_domains = ['www.koolearn.com']
    start_urls = ['https://www.koolearn.com/']

    def start_requests(self):
        db = Db()
        result = db.readKoolearnCates()
        for row in result:
            yield scrapy.Request('https://' + self.allowed_domains[0] + row[3], callback=self.parse, meta={'items': {'exam_type':row[1],'cate':row[2]}})

    def parse(self, response):
        meta = response.meta['items']
        item = ChapterItem();
        #print response.url
        secondCateDivPath = response.xpath("//div[@class='i-left p-left']/div/div/div[@class='content']/div[@class='part ji-part']")
        #secondCateUrl = secondCateDivPath.xpath("dl/dd/a/@href").extract();
        #secondCateText = secondCateDivPath.xpath("dl/dd/a/text()").extract();

        #chapterUrl = secondCateDivPath.xpath("dl/dd/dl/dd/a/@href").extract();
        #chapterText = secondCateDivPath.xpath("dl/dd/dl/dd/a/text()").extract();
        #print chapterUrl
        #print chapterText

        for i in secondCateDivPath:
            chapterUrl = i.xpath("dl/dd/dl/dd/a/@href").extract()
            chapterText = i.xpath("dl/dd/dl/dd/a/text()").extract()
            for k, v in dict(zip(chapterText, chapterUrl)).items():
                item['exam_type'] = meta['exam_type']
                item['cate'] = meta['cate']
                item['second_cate'] = i.xpath("dl/dd/a/text()").extract()[0]
                item['chapter_name'] = k
                item['url'] = v
                yield item


