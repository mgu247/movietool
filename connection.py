# getConnection returns cursor to a new database connection
import pymysql.cursors

def getConnection():
    conn = pymysql.connect(
        host='35.232.219.225',
        user='root',
        password='password123',
        db='movies',
    )
    cur = conn.cursor()
    return cur
