import sqlite3
import os

DATABASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tfg.sqlite3")

def set_user(id, name, language):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    user_exist = cursor.execute("SELECT COUNT(*) FROM Users WHERE id = ?", (id, ))
    
    if user_exist.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Users VALUES (?, ?, ?)", (id, name, language))

    cursor.close()
    conn.commit()

def get_user(id):
    conn = sqlite3.connect(DATABASE_DIR)
    cur = conn.cursor()

    cur.execute("SELECT name, language FROM Users WHERE id = ?", (id, ))
    
    user_data = cur.fetchone()

    cur.close()
    conn.commit()

    return user_data

def delete_user(id):

    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Users WHERE id = ?", (id, ))

    cursor.close()
    conn.commit()