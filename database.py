import mariadb

# Connect to MariaDB Platform

conn = mariadb.connect(
    user="user",
    password="temp",
    host="141.147.118.101",
    port=3306,
    database="scores"

)

mycursor = conn.cursor()


def check_data(data):

    TEXT = (f"SELECT score FROM scores WHERE username='{data}'")
    mycursor.execute(TEXT)
    table_data = mycursor.fetchall()

    if table_data:
        return True


def add_data(data):

    TEXT = (f"INSERT INTO scores (username, score) VALUES ('{data}', 0)")
    mycursor.execute(TEXT)
    conn.commit()


if __name__ == '__main__':
    print(add_data('whaat'))
