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
    
    def check_size(self):
        pass


    def get_data(self):
        self.mycursor.execute("SELECT * FROM accounts")        
        return self.mycursor.fetchall()
        
    def check_data(self,data):
        for row in self.get_data():
            for record in row:
                if record == data:
                    return True 
    
    def del_data(self,username):
        sql = (f"DELETE FROM accounts WHERE username = '{username}' ")
        self.mycursor.execute(sql)
        self.mydb.commit()
        print(f'{username} deleted')

    def add_data(self,username,password):

        sql = "INSERT INTO accounts (username, password) VALUES (%s, %s)"
        val = (username,password)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(f" '{username}' and '{password}' have been added")

if __name__ == '__main__':
    print(Database().get_data())