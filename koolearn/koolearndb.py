# -*- coding: utf-8 -*-
import json
from db import Db


class KoolearnDb(object):
    """
    这里配置表名
    """
    cate_table = 'koolearn_cate'
    chapter_table = 'koolearn_chapter'
    question_table = 'koolearn_question'

    dbObject = None

    cursor = None

    def __init__(self):
        self.dbObject = Db()
        self.cursor = self.dbObject._con.cursor()
        self.cursor.execute("USE tiku_spider")

    def insertKoolearnCate(self, item):
        try:
            sql = "INSERT INTO " + self.cate_table + "(exam_type, cate, url) VALUES(%s,%s,%s)"
            self.cursor.execute(sql, (
                item['exam_type'],
                item['cate'],
                item['url']))
            self.cursor.connection.commit()
            return item

        except BaseException as e:
            print("insertKoolearnCate has error>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
            self.dbObject._con.rollback()

    def insertKoolearnChapter(self, item):
        try:
            sql = "INSERT INTO " + self.chapter_table + "(exam_type, cate, second_cate, chapter_name, url) VALUES(%s,%s,%s,%s,%s)"
            self.cursor.execute(sql, (
                item['exam_type'],
                item['cate'],
                item['second_cate'],
                item['chapter_name'],
                item['url']
            ))
            self.cursor.connection.commit()
            return item

        except BaseException as e:
            print("insertKoolearnChapter has error>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
            self.dbObject._con.rollback()

    def insertKoolearnQuestion(self, item):
        try:
            sql = "INSERT INTO " + self.question_table + "(chapter_id, question_title, question_option, question_answer, question_type, question_analysis) VALUES(%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(sql, (
                item['chapter_id'],
                item['question_title'],
                json.dumps(item['question_option'], ensure_ascii=False),
                item['question_answer'],
                item['question_type'],
                item['question_analysis'],
            ))
            self.cursor.connection.commit()
            return item

        except BaseException as e:
            print("insertKoolearnQuestion has error>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
            self.dbObject._con.rollback()

