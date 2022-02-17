import mysql.connector
from mysql.connector import errorcode


mydb = mysql.connector.connect(
        host='database-1.c1ajdf2akg8w.eu-west-2.rds.amazonaws.com',
        user='admin', 
        password = "eTWgAS3ZvDzSpA2",
        database = "test"
        )


mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM accounts")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)