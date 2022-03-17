import mysql.connector
import random as rnd
import string
import config as cfg


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

    def add_data(self, table, first, second):

        sql = f"INSERT INTO {table} VALUES (%s, %s)"
        val = (first, second)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(f" '{first}' and '{second}' have been added")


def create_gamelobby():
    id = ''.join(rnd.choices(string.ascii_uppercase + string.digits, k=4))

    if not Database().check_data(id):
        Database().add_data('Gamelobby', id, cfg.ip)
    else:
        pass


if __name__ == '__main__':
    create_gamelobby()
