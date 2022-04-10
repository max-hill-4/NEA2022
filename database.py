import mysql.connector
import random as rnd
import string
import config as cfg


mydb = mysql.connector.connect(
        user="user",
        password="temp",
        host="nidalee.maxh.cc",
        port=3306,
        database="scores"

)
mycursor = mydb.cursor()


def get_data(table, field, record, data):
    mycursor.execute(f"SELECT {field} FROM {table} WHERE {record} = '{data}'")
    return mycursor.fetchall()


def check_data(table, data):
    mycursor.execute(f"SELECT * FROM {table}")
    table_data = mycursor.fetchall()

    for row in table_data:
        for record in row:
            if record == data:
                return True


def del_data(table, field, data):
    sql = (f"DELETE FROM {table} WHERE {field} = '{data}'")
    mycursor.execute(sql)
    mydb.commit()
    print(f'{data} deleted')


def add_data(table, first, second):

    sql = f"INSERT INTO {table} VALUES (%s, %s)"
    val = (first, second)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f" '{first}' and '{second}' have been added")


def create_gamelobby():
    id = ''.join(rnd.choices(string.ascii_uppercase + string.digits, k=4))

    if not check_data('Gamelobby', id):
        add_data('Gamelobby', id, cfg.ip)
        return id
    else:
        # display error
        pass


if __name__ == '__main__':
    get_data()
