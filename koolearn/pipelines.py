# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from koolearndb import KoolearnDb

class KoolearnPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'koolearn_tiku_cate':
            db = KoolearnDb()
            item = db.insertKoolearnCate(item)
        elif spider.name == 'koolearn_tiku_chpater':
            db = KoolearnDb()
            item = db.insertKoolearnChapter(item)
        elif spider.name == 'koolearn_tiku_question':
            db = KoolearnDb()
            item = db.insertKoolearnQuestion(item)
        return item
