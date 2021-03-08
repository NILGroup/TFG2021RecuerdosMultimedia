def get_keyboard(name):
    if (name == "THERAPY_CHOOSING_KEYBOARD"):
        return get_therapy_choosing_keyboards()
    elif (name == "THERAPY_KEYBOARD"):
        return get_therapy_keyboards()
    elif (name == "MENU_KEYBOARD"):
        return get_menu_keyboards()
    elif (name == "UPLOAD_IMAGES_KEYBOARD"):
        return get_upload_images_keyboards()
    elif (name == "END_CONVERSATION_KEYBOARD"):
        return get_end_conversarion_keyboards()


# therapy_choosing_keyboard

def get_therapy_choosing_keyboards():
    return [THERAPY_CHOOSING_KEYBOARD_EN, THERAPY_CHOOSING_KEYBOARD_ES]

THERAPY_CHOOSING_KEYBOARD_EN = [
    ['Begin', 'Change'],
    ['End'],
]

THERAPY_CHOOSING_KEYBOARD_ES = [
    ['Comenzar', 'Cambiar'],
    ['Terminar'],
]


# therapy_keyboard

def get_therapy_keyboards():
    return [THERAPY_KEYBOARD_EN, THERAPY_KEYBOARD_ES]

THERAPY_KEYBOARD_EN = [
    ['Change question', 'Change image'],
    ['End'],
]

THERAPY_KEYBOARD_ES = [
    ['Cambiar pregunta', 'Cambiar fotografía'],
    ['Terminar'],
]


# menu_keyboard

def get_menu_keyboards():
    return [MENU_KEYBOARD_EN, MENU_KEYBOARD_ES]

MENU_KEYBOARD_EN = [
    ['Begin therapy', 'Upload Images'],
    ['Read my life stories', 'Download my life stories'],
    ['Exit'],
]

MENU_KEYBOARD_ES = [
    ['Comenzar terapia', 'Subir imágenes'],
    ['Leer mis historias', 'Descargar mis historias'],
    ['Salir'],
]


# upload_images_keyboard

def get_upload_images_keyboards():
    return [ UPLOAD_IMAGES_KEYBOARD_EN, UPLOAD_IMAGES_KEYBOARD_ES]

UPLOAD_IMAGES_KEYBOARD_EN = [['Finish']]

UPLOAD_IMAGES_KEYBOARD_ES = [['Terminar']]


# end_conversation_keyboard

def get_end_conversarion_keyboards():
    return [ END_CONVERSATION_KEYBOARD_EN, END_CONVERSATION_KEYBOARD_ES]

END_CONVERSATION_KEYBOARD_EN = [['Start']]

END_CONVERSATION_KEYBOARD_ES = [['Comenzar']]