#searchFunctions are used to search specific movies/actors/etc
import pymysql.cursors

def searchActors(values, cur):

    #This line checks if the person's name is in the person list in the database (need to change to just actor index)
    cur.execute("select * from person where person_name = (%s)", (values[0]))
    #It takes the first row, if the row is empty ( == None) then it moves on, if the person's name is in the database
    #it does the stored procedure
    row = cur.fetchone()
    if (row != None):
        values[0] = "CALL SearchActors('" + values[0] + "');"
   
    #How to I created the stored procedure in gcp:
    #Use this link for reference its super good https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html
    #My stored procedure for SearchActors:
    #    mysql> delimiter //
    #    mysql> CREATE PROCEDURE SearchActors (IN Name varchar(40))
    #    BEGIN
    #        select person_name, title, character_name, overview, runtime, popularity from movie as c join
    #        (select person_name, movie_id, character_name from movie_cast as a join person as b on a.person_id = b.person_id where person_name = Name)
    #        as d on c.movie_id = d.movie_id;
    #    END//
    #    mysql> delimiter ;



    #Command use to check if your stored procedure was created:
    #    mysql> select routine_name, routine_type,definer,created,security_type,SQL_Data_Access from information_schema.routines where routine_type='PROCEDURE' and routine_schema='movies';

    return values

    def searchTitle(values, cur):
        cur.execute("select * from movie where title = (%s)", (values[0]))
        row = cur.fetchone()
        if (row != None):
        values[0] = "CALL SearchTitle('" + values[0] + "');"
        
        # Stored procedure for SearchTitle:
        # 
        #   mysql> CREATE PROCEDURE SearchTitle (IN Name varchar(1000))
        #   BEGIN
        #   select title, release_date, popularity, runtime, budget, movie_status from movie where title = Name;
        #   END
        #

        return values