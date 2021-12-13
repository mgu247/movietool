import pymysql.cursors

def mysqlconnect():
    conn = pymysql.connect(
        host='35.232.219.225',
        user='root',
        password='password123',
        db='movies',
    )

    cur = conn.cursor()
    cur.execute("select * from country;")
    output = cur.fetchall()
    print(output)

if __name__ == "__main__" :
    mysqlconnect()
