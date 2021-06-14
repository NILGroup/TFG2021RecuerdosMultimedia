import sqlite3
import os

DATABASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tfg.sqlite3")

# Función que establece el permiso dado por el usuario
def set_permission(user_id, permission):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    user_exist = cursor.execute("SELECT COUNT(*) FROM Permission WHERE id = ?", (user_id, ))

    if user_exist.fetchone()[0] != 0:
        cursor.execute("UPDATE permission SET permission = ? WHERE id = ?", (permission, user_id))
    else:
        cursor.execute("INSERT INTO Permission VALUES (?,?)", (user_id, permission))

    cursor.close()
    conn.commit()


# Función que comprueba si el usuario ha dado ya permiso o no y devulve el permiso
def get_user_permission(user_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()
    permission = None

    user_exist = cursor.execute("SELECT COUNT(*) FROM Permission WHERE id = ?", (user_id, ))
    
    if user_exist.fetchone()[0] != 0:
        cursor.execute("SELECT permission FROM Permission WHERE id = ?", (user_id, ))
    
        permission = cursor.fetchone()[0]

    cursor.close()
    conn.commit()
    
    return permission

def deleteUserPermission(user_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Permission WHERE id = ?", (user_id, ))

    cursor.close()
    conn.commit()
