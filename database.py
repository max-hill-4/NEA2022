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

    def get_data(self):

        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM accounts")        
        return mycursor.fetchall()
        


    def check_data(self,data):
        for row in self.get_data():
            for record in row:
                if record == data:
                    print(f'{data} was found in the database on row {row[0]}')
                    return True 


print(Database().get_data())