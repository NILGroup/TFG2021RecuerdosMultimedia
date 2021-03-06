import sqlite3
import os

DATABASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tfg.sqlite3")

def set_user(id, name):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    user_exist = cursor.execute("SELECT COUNT(*) FROM Users WHERE id = ?", (id, ))
    
    if user_exist.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Users VALUES (?, ?)", (id, name))

    cursor.close()
    conn.commit()

def get_user(id):
    conn = sqlite3.connect(DATABASE_DIR)
    cur = conn.cursor()

    cur.execute("SELECT name FROM Users WHERE id = ?", (id, ))
    
    name = cur.fetchone()[0]

    cur.close()
    conn.commit()

    return name