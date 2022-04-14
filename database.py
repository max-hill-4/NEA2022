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
    # 'data' = username searching for
    TEXT = (f"SELECT score FROM scores WHERE username='{data}';")
    mycursor.execute(TEXT)
    table_data = mycursor.fetchall()
    # If anything apart from None then True
    if table_data:
        return True

def fetch_data():
    # Get the top 10 scrores from the database
    TEXT = ("SELECT username, score FROM scores ORDER BY score DESC LIMIT 10;")
    mycursor.execute(TEXT)
    table_data = mycursor.fetchall()
    return table_data

def add_username(data):
    # insert 'data = username with a score of 0
    TEXT = (f"INSERT INTO scores (username, score) VALUES ('{data}', 0);")
    mycursor.execute(TEXT)
    conn.commit()

def add_score(data):
    # add one to 'data' = username in score field
    TEXT = (f"UPDATE scores SET score = score + 1 WHERE username = '{data}';")
    print("added ot the score!")
    mycursor.execute(TEXT)
    conn.commit()

if __name__ == '__main__':
    add_score('what')
    print(fetch_data())

