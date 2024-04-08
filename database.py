import sqlite3
# noinspection PyUnresolvedReferences
from multiprocessing import connection
# noinspection PyUnresolvedReferences
from kivy.modules import cursor

def create_table():
    try:
        conn = connect()
        cur = conn.cursor()
        sqlite_create_table_query = """ CREATE TABLE IF NOT EXISTS user_input (
                                        id INTEGER PRIMARY KEY,
                                        password VARCHAR(255) NOT NULL,
                                        login VARCHAR(255) NOT NULL,
                                        app_name VARCHAR(255) NOT NULL
                                    );"""
        cur.execute(sqlite_create_table_query)
        conn.commit()
    except sqlite3.Error as error:
        print(error)
def add_data(password, login, app_name):
    try:
        conn = connect()
        cur = conn.cursor()
        sqlite_insert_query = """ INSERT INTO user_input (password, login, app_name) VALUES (?, ?, ?)"""
        record_to_insert = (password, login, app_name)
        cur.execute(sqlite_insert_query, record_to_insert)
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def delete_data(app_name):
    try:
        conn = connect()
        cur = conn.cursor()
        sqlite_delete_query = """ DELETE FROM user_input WHERE app_name = ?"""
        cur.execute(sqlite_delete_query, (app_name,))
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def connect():
    try:
        conn = sqlite3.connect('user_input.db')
        return conn
    except sqlite3.Error as error:
        print(error)
def find_password(app_name):
    try:
        conn = connect()
        cur = conn.cursor()
        sqlite_select_query = """ SELECT password FROM user_input WHERE app_name = ?"""
        cur.execute(sqlite_select_query, (app_name,))
        result = cur.fetchone()
        if result:
            print('Password is:', result[0])
        else:
            print('No password found for the given app name.')
    except sqlite3.Error as error:
        print(error)

def find_users(user_email):
    data = ('Password: ', 'Email: ', 'Username: ', 'App/Site name: ')
    try:
        conn = connect()
        cur = conn.cursor()
        sqlite_select_query = """ SELECT * FROM user_input WHERE email = ?"""
        cur.execute(sqlite_select_query, (user_email,))
        result = cur.fetchall()
        print('')
        print('RESULT')
        print('')
        for row in result:
            for i in range(len(row)-1):
                print(data[i] + str(row[i]))
        print('')
        print('-'*30)
    except sqlite3.Error as error:
        print(error)

# Call create_table() to ensure the table is created before performing operations
create_table()
