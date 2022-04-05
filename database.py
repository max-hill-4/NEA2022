import mariadb

# Connect to MariaDB Platform

conn = mariadb.connect(
    user="user",
    password="temp",
    host="nidalee.maxh.cc",
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

def fetch_data():
    TEXT = ("SELECT username, score FROM scores ORDER BY score DESC LIMIT 10")
    mycursor.execute(TEXT)
    table_data = mycursor.fetchall()
    return table_data

def add_data(data):

    TEXT = (f"INSERT INTO scores (username, score) VALUES ('{data}', 0)")
    mycursor.execute(TEXT)
    conn.commit()


if __name__ == '__main__':
    print(fetch_data())
