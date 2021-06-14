from hashlib import new
import sqlite3, random
import os

DATABASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tfg.sqlite3")

def set_question(image_id, question, answer, user_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    new_id = random.randint(0, 10e9)

    while True:
        cursor.execute("SELECT COUNT(*) FROM Questions WHERE id = ?", (new_id, ))

        if (cursor.fetchone()[0] == 0):
            break
        
        new_id = random.randint(0, 10e9)

    # todo: añadir límites
    cursor.execute("INSERT INTO Questions VALUES (?, ?, ?, ?, ?)", (new_id, image_id, question, answer, user_id))

    cursor.close
    conn.commit()

def get_question(user_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cur = conn.cursor()

    cur.execute("SELECT image_id, question, answer FROM Questions WHERE user_id = ?", (user_id, ))

    question = cur.fetchone()

    cur.close
    conn.commit()

    return question

def get_image_questions(image_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cur = conn.cursor()

    cur.execute("SELECT * FROM Questions WHERE image_id = ?", (image_id, ))

    questions = []

    for row in cur.fetchall():
        questions.append(row)

    cur.close
    conn.commit()

    return questions

def get_image_user_questions(image_id, user_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cur = conn.cursor()

    cur.execute("SELECT question, answer FROM Questions WHERE image_id = ? AND user_id = ?", (image_id, user_id))

    questions = []

    for row in cur.fetchall():
        questions.append(row)

    cur.close
    conn.commit()

    return questions

def get_all_question(user_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cur = conn.cursor()

    cur.execute("SELECT image_id, question, answer FROM Questions WHERE user_id = ?", (user_id, ))

    question = cur.fetchone()

    cur.close
    conn.commit()

    return question

def delete_all_questions(user_id):

    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Questions WHERE user_id = ?", (user_id, ))

    cursor.close()
    conn.commit()


