import mysql.connector


mydb = mysql.connector.connect(
        host='database-1.c1ajdf2akg8w.eu-west-2.rds.amazonaws.com',
        user='admin',
        password="qwertyui",
        database="test"
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


if __name__ == '__main__':
    get_data()
