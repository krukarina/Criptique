import sqlite3
# noinspection PyUnresolvedReferences
from multiprocessing import connection
# noinspection PyUnresolvedReferences
from kivy.modules import cursor


def create_table():
    try:
        conn = connect()
        cur = conn.cursor()
        sqlite_create_table_query = """ CREATE TABLE IF NOT EXISTS data_storage (
                                        id INTEGER PRIMARY KEY,
                                        app_name VARCHAR(255) NOT NULL,
                                        email VARCHAR(255) NOT NULL,
                                        password VARCHAR(255) NOT NULL,
                                        key_pass VARCHAR(255) NOT NULL
                                    );"""
        cur.execute(sqlite_create_table_query)
        conn.commit()
    except sqlite3.Error as error:
        print(error)


def add_data(app_name, email, password, key_pass):
    try:
        conn = connect()
        cur = conn.cursor()
        sqlite_insert_query = """ INSERT INTO data_storage (app_name, email, password, key_pass) VALUES (?, ?, ?, ?)"""
        record_to_insert = (app_name, email, password, key_pass)
        cur.execute(sqlite_insert_query, record_to_insert)
        conn.commit()
    except sqlite3.Error as error:
        print(error)


def delete_data(app_name):
    try:
        conn = connect()
        cur = conn.cursor()
        sqlite_delete_query = """ DELETE FROM data_storage WHERE app_name = ?"""
        cur.execute(sqlite_delete_query, (app_name,))
        conn.commit()
    except sqlite3.Error as error:
        print(error)


def app_exists(app_name):
    # Implement logic to check if the app name exists in the database
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM data_storage WHERE app_name = ?", (app_name,))
    count = cur.fetchone()[0]
    conn.close()
    return count > 0


def connect():
    try:
        conn = sqlite3.connect('user_input.db')
        return conn
    except sqlite3.Error as error:
        print(error)


def get_password(app_name):
    try:
        conn = connect()
        cur = conn.cursor()
        sqlite_select_query = """ SELECT password FROM data_storage WHERE app_name = ?"""
        cur.execute(sqlite_select_query, (app_name,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            return None
    except sqlite3.Error as error:
        print(error)

def get_key(app_name):
    try:
        conn = connect()
        cur = conn.cursor()
        sqlite_select_query = """ SELECT key_pass FROM data_storage WHERE app_name = ?"""
        cur.execute(sqlite_select_query, (app_name,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            return None
    except sqlite3.Error as error:
        print(error)

# Call create_table() to ensure the table is created before performing operations
create_table()
