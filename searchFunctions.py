import pymysql.cursors

def searchActors(values, cur):
    # server connect

    cur.execute("select * from person where person_name = (%s)", (values[0]))
    row = cur.fetchone()
    if (row != None):
        values[0] = """select person_name, title from
          movie as c join
          (select person_name, movie_id from movie_cast as a join person as b on a.person_id = b.person_id where person_name = \"""" + values[0] + """\")
          as d on c.movie_id = d.movie_id;"""
    return values
