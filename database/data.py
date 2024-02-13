# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:54:18 2024

Created for SDEV 220 Fall 2024

@author: c.s.francis

"""





import sqlite3 as sql


connection = sql.connect("in-class.db")
cursor = connection.cursor()

create_query = "CREATE TABLE IF NOT EXISTS People(name TEXT, age INTEGER, town TEXT);"
cursor.execute(create_query)

insert_query_1 = "INSERT INTO People(name, age, town) VALUES(\"sally\", 34, \"salem\");"
insert_query_2 = "INSERT INTO People(name, age, town) VALUES(\"charlie\", 87, \"charlestown\");"
insert_query_3 = "INSERT INTO People(name, age, town) VALUES(\"alan\", 14, \"new albany\");"

cursor.execute(insert_query_1)
cursor.execute(insert_query_2)
cursor.execute(insert_query_3)


select_query = "SELECT * FROM People WHERE age < 30;"

cursor.execute(select_query)

data = cursor.fetchall()


for d in data:
    print(d[0] + " is " + str(d[1]) + " years old and lives in " + d[2])



connection.close()






if __name__=="__main__":
    pass



