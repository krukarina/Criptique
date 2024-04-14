import sqlite3
# noinspection PyUnresolvedReferences
from multiprocessing import connection
# noinspection PyUnresolvedReferences
from kivy.modules import cursor


def create_table():
    try:
        conn2 = connect()
        cur2 = conn2.cursor()
        sqlite_create_table_query = """ CREATE TABLE IF NOT EXISTS login_masterpwd (
                                        id INTEGER PRIMARY KEY,
                                        email VARCHAR(255) NOT NULL,
                                        masterpassword VARCHAR(255) NOT NULL,
                                        salt VARCHAR(255) NOT NULL
                                    );"""
        cur2.execute(sqlite_create_table_query)
        conn2.commit()
    except sqlite3.Error as error:
        print(error)


def signup(email, masterpassword, salt):
    try:
        conn2 = connect()
        cur2 = conn2.cursor()
        sqlite_insert_query = """ INSERT INTO login_masterpwd (email, masterpassword, salt) VALUES (?, ?, ?)"""
        record_to_insert = (email, masterpassword, salt)
        cur2.execute(sqlite_insert_query, record_to_insert)
        conn2.commit()
    except sqlite3.Error as error:
        print(error)


def get_masterhash(email):
    conn2 = connect()
    cur2 = conn2.cursor()
    cur2.execute("SELECT masterpassword FROM login_masterpwd WHERE email = ?", (email,))
    result = cur2.fetchone()
    conn2.close()
    return result[0] if result else None

def email_exists(email):
    conn2 = connect()
    cur2 = conn2.cursor()
    cur2.execute("SELECT COUNT(*) FROM login_masterpwd WHERE email = ?", (email,))
    count = cur2.fetchone()[0]
    conn2.close()
    return count > 0

def connect():
    try:
        conn2 = sqlite3.connect('user_input.db')
        return conn2
    except sqlite3.Error as error:
        print(error)


create_table()
