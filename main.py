import pymysql.cursors

def mysqlconnect():
    conn = pymysql.connect(
        host='35.232.219.225',
        user='root',
        password='password123',
        db='movies',
    )

    cur = conn.cursor()
    while (True):
        sqlquery = input ("Input sql query: ")
        cur.execute(sqlquery)
        output = cur.fetchall()
        print(output)

if __name__ == "__main__" :
    mysqlconnect()
