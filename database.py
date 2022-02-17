<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 59533fcc7056d16176b9db2907a0435f441330ac
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
<<<<<<< HEAD
#test
=======
#test
=======
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
>>>>>>> origin/main
>>>>>>> 59533fcc7056d16176b9db2907a0435f441330ac
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)