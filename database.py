import mysql.connector
from mysql.connector import errorcode

class Database:
    def __init__(self):


        self.mydb = mysql.connector.connect(

            host='database-1.c1ajdf2akg8w.eu-west-2.rds.amazonaws.com',
            user='admin', 
            password = "eTWgAS3ZvDzSpA2",
            database = "test"
            )


        self.mycursor = self.mydb.cursor()



    def get_all(self):

        self.mycursor.execute("SELECT * FROM accounts")

        self.myresult = self.mycursor.fetchall()

        for x in self.myresult:          
            print(x)


Database().get_all()