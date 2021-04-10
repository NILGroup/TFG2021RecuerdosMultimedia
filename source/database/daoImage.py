import sqlite3
import os

DATABASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tfg.sqlite3")

#funcion para incluir una imagen en la base de datos
def set_user_image(user_id, img_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Images VALUES (?,?)", (img_id, user_id))

    cursor.close()
    conn.commit()


#funcion para obtener los ID's de todas las imagenes de un usuario
def get_user_images(user_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Images WHERE user_id = ?", (user_id, ))

    images = []
    
    for row in cursor.fetchall():
        images.append(row[0])

    cursor.close()
    conn.commit()
    
    return images


#funcion para obtener el numero total de imagenes que tiene almacenadas un usuario
def get_num_images(user_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Images WHERE user_id = ?", (user_id, ))

    num_images = cursor.fetchone()[0]

    cursor.close()
    conn.commit()
    
    return num_images

def set_selected_image(user_id, image_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    selected = cursor.execute("SELECT COUNT(*) FROM Current_Selection WHERE user_id = ?", (user_id, ))
    
    if selected.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Current_Selection VALUES (?, ?)", (user_id, image_id))
    else:
        cursor.execute("UPDATE Current_Selection SET image_id = ? WHERE user_id = ?", (image_id, user_id))

    cursor.close()
    conn.commit()

def get_selected_image(user_id):
    conn = sqlite3.connect(DATABASE_DIR)
    cursor = conn.cursor()

    cursor.execute("SELECT image_id FROM Current_Selection WHERE user_id = ?", (user_id, ))

    image = cursor.fetchone()[0]

    cursor.close()
    conn.commit()
    
    return image



