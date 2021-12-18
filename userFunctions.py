# userFunctions handle all interaction with the user account and user movie list

def addUser(uname, pword, cur):
    cur.execute("insert into users(user_id, username, password) VALUES(NULL, '{}', '{}');".format(uname, pword))
    output = cur.fetchall()
    cur.execute("select user_id from users where username='{}';".format(uname))
    output = cur.fetchall()
    out = "usertable{}".format(output[0][0])
    cur.execute("update users set movie_table_name = '{}' where user_id={};". format(out, output[0][0]))
    createUserTable(out, cur)

def createUserTable(name, cur):
    cur.execute("create table if not exists {}(title varchar(1000), add_date date, status varchar(50), rating_out_of_10 varchar(10));".format(name))

def getUserTable(name, cur):
    return "select * from {};".format(name)

def addMovie(name, title, status, rating, cur):
    cur.execute("insert into {}(title, add_date, status, rating_out_of_10) values ('{}', CURDATE(), '{}', '{}');".format(name, title, status, rating))
    return cur.fetchall()
