import mysql.connector
import random as rnd
import string


class Database:
    def __init__(self):

        self.mydb = mysql.connector.connect(

            host='database-1.c1ajdf2akg8w.eu-west-2.rds.amazonaws.com',
            user='admin',
            password="qwertyui",
            database="test"
            )
        self.mycursor = self.mydb.cursor()

    def get_data(self):
        self.mycursor.execute("SELECT * FROM highscores")
        return self.mycursor.fetchall()

    def check_data(self, data):
        for row in self.get_data():
            for record in row:
                if record == data:
                    return True

    def del_data(self, username):
        sql = (f"DELETE FROM highscores WHERE username = '{username}' ")
        self.mycursor.execute(sql)
        self.mydb.commit()
        print(f'{username} deleted')

    def add_data(self, username, score):

        if self.check_data(username):
            print("Username Taken")
            return
        sql = "INSERT INTO highscores (name, score) VALUES (%s, %s)"
        val = (username, score)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(f" '{username}' and '{score}' have been added")


def create_gamelobby():
    id = ''.join(rnd.choices(string.ascii_uppercase + string.digits, k=4))

    if Database.check_data(id):
        Database.add_data(id)
        return id
    else:
        create_gamelobby()


if __name__ == '__main__':
    print(Database().get_data())
