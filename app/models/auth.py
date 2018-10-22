import MySQLdb
from config import config

class WRITE():

    def __init__(self,):
        db = MySQLdb.connect("localhost", "root", "abcd234", "superset_board", charset='utf8')
        results = {}
        cursor = db.cursor()
        sql = "SELECT * FROM auth_permission"
        try:
            cursor.execute(sql)
            self.results = cursor.fetchall()
        except:
            db.close()
    def search(self):
        return  self.results
