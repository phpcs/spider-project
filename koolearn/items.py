# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class KoolearnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CateItem(scrapy.Item):
    exam_type = scrapy.Field()
    cate = scrapy.Field()
    url = scrapy.Field()


class ChapterItem(scrapy.Item):
    exam_type = scrapy.Field()
    cate = scrapy.Field()
    second_cate = scrapy.Field()
    chapter_name = scrapy.Field()
    url = scrapy.Field()


class QuestionItem(scrapy.Item):
    chapter_id = scrapy.Field()
    question_title = scrapy.Field()
    question_option = scrapy.Field()
    question_answer = scrapy.Field()
    question_type = scrapy.Field()
    question_analysis = scrapy.Field()
