# -*- coding: utf-8 -*-
import scrapy
from koolearn.db import Db
from koolearn.items import QuestionItem


class KoolearnTikuQuestionSpider(scrapy.Spider):
    name = 'koolearn_tiku_question'
    allowed_domains = ['www.koolearn.com']
    start_urls = ['http://www.koolearn.com/']

    def start_requests(self):
        db = Db()
        result = db.readKoolearnChapter()
        for row in result:
            yield scrapy.Request('https://' + self.allowed_domains[0] + row[1], callback=self.parse, meta={'items': row[0]})

    def parse(self, response):
        meta = response.meta['items']
        questionDiv = response.xpath("//div[@class='p-results']/div[@class='i-timu']")

        for i in questionDiv:
            arr = {}
            arr['chapter_id'] = meta
            arr['question_title'] = i.xpath("div[@class='content']/div/div[@class='js-content']/p/span/text()").extract()[0].strip()
            arr['question_option'] = i.xpath("div[@class='content']/div/ul[@class='single-choice']/li/div[@class='r']/p/span/text()").extract()
            arr['question_type'] =  i.xpath("div[@class='footer']/label/span[2]/text()").extract()[0].strip()
            questionanalyUrl = i.xpath("div[@class='footer']/a/@href").extract()[0]
            yield scrapy.Request('https://' + self.allowed_domains[0] + questionanalyUrl, callback=self.questionAnaly, meta={'items': arr})

        #继续抓取下一页
        next_page = response.xpath("//div[@class='i-pager']/a[@class='next']/@href").extract()
        if next_page and next_page[0]:
            yield scrapy.Request('https://' + self.allowed_domains[0] + next_page[0], callback=self.parse, meta={'items': meta})

    def questionAnaly(self, response):
            arr = response.meta['items']
            item = QuestionItem();
            item['chapter_id'] = arr['chapter_id']
            item['question_title'] = arr['question_title']
            item['question_option'] = arr['question_option']
            item['question_type'] = arr['question_type']
            item['question_answer'] = ''
            item['question_analysis'] = ''
            questionAnswer = response.xpath("//div[@id='i-tab-content']/text()").extract()
            if questionAnswer:
                item['question_answer'] = questionAnswer[0].strip()

            questionAnalysis = response.xpath("//div[@id='i-tab-content2']/p/text()").extract()
            if questionAnalysis:
                item['question_analysis'] = questionAnalysis[0].strip()

            yield item