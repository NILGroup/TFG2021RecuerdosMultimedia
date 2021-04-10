import sqlite3
import os

DATABASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tfg.sqlite3")

#funcion para incluir las questions en la base de datos
def set_user_curren_questions(user_id, questions):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    for question in questions:
        cursor.execute("INSERT INTO Current_Questions VALUES (?,?)", (user_id, question))

    cursor.close()
    conn.commit()


#funcion para obtener los ID's de todas las imagenes de un usuario
def get_user_current_questions(user_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    cursor.execute("SELECT question FROM Current_Questions WHERE user_id = ?", (user_id, ))

    questions = []
    
    for row in cursor.fetchall():
        questions.append(row[0])

    cursor.close()
    conn.commit()
    
    return questions

    
def delete_user_current_question(user_id, question):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Current_Questions WHERE user_id = ? AND question = ?", (user_id, question))

    cursor.close()
    conn.commit()

def delete_user_current_questions(user_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Current_Questions WHERE user_id = ?", (user_id, ))

    cursor.close()
    conn.commit()


def user_has_current_questions(user_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    has_questions = True

    cursor.execute("SELECT COUNT(*) FROM Current_Questions WHERE user_id = ?", (user_id, ))

    if (cursor.fetchone()[0] == 0):
        has_questions = False

    cursor.close()
    conn.commit()

    return has_questions