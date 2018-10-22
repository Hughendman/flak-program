import MySQLdb
from app.db import MYSQLDB_DATABASE_URI

class WRITE():

    def __init__(self):
        db = MySQLdb.connect(MYSQLDB_DATABASE_URI["host"], MYSQLDB_DATABASE_URI["user"], MYSQLDB_DATABASE_URI["pwd"], MYSQLDB_DATABASE_URI["db"], charset='utf8')
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
