import pymysql

class Db(object):

    _con = None

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Db, cls).__new__(cls)
            cls._instance._con = cls.connect()
        return cls._instance

    @staticmethod
    def connect():
        return pymysql.connect(
            host="192.168.8.98",
            user="root",
            passwd="123456",
            charset="utf8",
            use_unicode=False
        )

    def readKoolearnCates(self):
        cursor = self._con.cursor()
        cursor.execute("USE tiku_spider")
        try:
            sql = "SELECT id,exam_type,cate,url FROM koolearn_cate"
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except:
            print ("Error: unable to fetch data")
            self._con.close()

    def readKoolearnChapter(self):
        cursor = self._con.cursor()
        cursor.execute("USE tiku_spider")
        try:
            sql = "SELECT id,url FROM koolearn_chapter"
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except:
            print ("Error: unable to fetch data")
            self._con.close()