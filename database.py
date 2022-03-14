import mysql.connector


class Database:
    def __init__(self):

        self.mydb = mysql.connector.connect(

            host='sql4.freemysqlhosting.net',
            user='sql4478135',
            password = "JwZZIa2hhe",
            database = "sql4478135"
            )
        self.mycursor = self.mydb.cursor()

    def get_data(self):
        self.mycursor.execute("SELECT * FROM highscores")
        return self.mycursor.fetchall()

    def check_data(self,data):
        for row in self.get_data():
            for record in row:
                if record == data:
                    return True

    def del_data(self,username):
        sql = (f"DELETE FROM highscores WHERE username = '{username}' ")
        self.mycursor.execute(sql)
        self.mydb.commit()
        print(f'{username} deleted')

    def add_data(self,username,password):

        if self.check_data(username):
            print("Username Taken")
            return
        sql = "INSERT INTO highscores (name, score) VALUES (%s, %s)"
        val = (username,password)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(f" '{username}' and '{password}' have been added")

if __name__ == '__main__':
    print(Database().get_data())
