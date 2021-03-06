# WELCOME_MESSAGE

def get_welcome_message():
    return [
        WELCOME_MESSAGE_EN, 
        WELCOME_MESSAGE_ES
    ]
    
WELCOME_MESSAGE_EN = "Hi {0} and welcome to therapy! My name is Remi and I'm here to help you. ¿What would you like to do now"
WELCOME_MESSAGE_ES = "¡Hola {0} y bienvenido a terapia! Mi nombre es Remi y estoy aqui para ayudarte. ¿Qué te gustaría hacer ahora?"


# THERAPY_CHOICE_MESSAGE

def get_therapy_choice_message():
    return [
        THERAPY_CHOICE_MESSAGE_EN, 
        THERAPY_CHOICE_MESSAGE_ES
    ]

THERAPY_CHOICE_MESSAGE_EN = "Great! Let me choose an image for you."
THERAPY_CHOICE_MESSAGE_ES = "¡Genial! Voy a comenzar eligiendo una fotografía para comenzar."


# THERAPY_ASK_TO_CHANGE_MESSAGE

def get_therapy_ask_to_change_message():
    return [
        THERAPY_ASK_TO_CHANGE_MESSAGE_EN, 
        THERAPY_ASK_TO_CHANGE_MESSAGE_ES
    ]

THERAPY_ASK_TO_CHANGE_MESSAGE_EN = "Would you like to talk about this photo or do you prefer to change it?"
THERAPY_ASK_TO_CHANGE_MESSAGE_ES = "¿Te gustaría hablar sobre esta foto o prefieres cambiarla?"


# THERAPY_CHANGE_PHOTO_MESSAGE

def get_therapy_change_photo_message():
    return [
        THERAPY_CHANGE_PHOTO_MESSAGE_EN, 
        THERAPY_CHANGE_PHOTO_MESSAGE_ES
    ]

THERAPY_CHANGE_PHOTO_MESSAGE_EN = "Lets try with this one..."
THERAPY_CHANGE_PHOTO_MESSAGE_ES = "Vamos a probar con esta otra..."


# THERAPY_BEGIN_FIRST_MESSAGE

def get_therapy_begin_first_message():
    return [
        THERAPY_BEGIN_FIRST_MESSAGE_EN, 
        THERAPY_BEGIN_FIRST_MESSAGE_ES
    ]

THERAPY_BEGIN_FIRST_MESSAGE_EN = "Look at the image and try to remember everything you can."
THERAPY_BEGIN_FIRST_MESSAGE_ES = "Mira la fotografía e intenta recordar todo lo que puedas."


# THERAPY_BEGIN_SECOND_MESSAGE

def get_therapy_begin_second_message():
    return [
        THERAPY_BEGIN_SECOND_MESSAGE_EN,
        THERAPY_BEGIN_SECOND_MESSAGE_ES
    ]

THERAPY_BEGIN_SECOND_MESSAGE_EN = "Do you remember when this photo was taken?"
THERAPY_BEGIN_SECOND_MESSAGE_ES = "¿Recuerdas cuando fue tomada esta foto?"


# ASK_WHAT_TO_DO

def get_ask_what_to_do_message():
    return [
        ASK_WHAT_TO_DO_EN, 
        ASK_WHAT_TO_DO_ES
    ]

ASK_WHAT_TO_DO_EN = "What would you like to do now?"
ASK_WHAT_TO_DO_ES = "¿Qué te gustaría hacer ahora?"


# ERROR_MESSAGE

def get_error_message():
    return [
        ERROR_MESSAGE_EN, 
        ERROR_MESSAGE_ES
    ]

ERROR_MESSAGE_EN = "Sorry, It seems I can't do this yet 😕. Try something else."
ERROR_MESSAGE_ES = "Vaya, parece que todavía no puedo hacer esto 😕. Prueba con otra cosa."


# GOODBYE_MESSAGE

def get_goodbye_message():
    return [
        GOODBYE_MESSAGE_EN, 
        GOODBYE_MESSAGE_ES
    ]

GOODBYE_MESSAGE_EN = "I've enjoyed talking with you. Come back whenever you want! 👋"
GOODBYE_MESSAGE_ES = "Me ha encantado hablar contigo. ¡Vueve cuando quieras! 👋"


# UPLOAD_IMAGE_MESSAGE

def get_upload_image_message():
    return [
        UPLOAD_IMAGE_MESSAGE_EN, 
        UPLOAD_IMAGE_MESSAGE_ES
    ]

UPLOAD_IMAGE_MESSAGE_EN = "Upload the images that you want to use for the therapy. Press the finish button when you are done."
UPLOAD_IMAGE_MESSAGE_ES = "Sube las imágenes que quieras utilizar para realizar la terapia. Cuando hayas terminado pulsa el botón terminar"


# FINISH_UPLOAD_IMAGE_MESSAGE

def get_finish_upload_image_message():
    return [
        FINISH_UPLOAD_IMAGE_MESSAGE_EN, 
        FINISH_UPLOAD_IMAGE_MESSAGE_ES
    ]

FINISH_UPLOAD_IMAGE_MESSAGE_EN = "Thanks for uploading your images! 😄"
FINISH_UPLOAD_IMAGE_MESSAGE_ES = "¡Gracias por subir tus imágenes! 😄"



def get_message(name):
    if (name == "WELCOME_MESSAGE"):
        return  get_welcome_message()
    elif (name == "THERAPY_CHOICE_MESSAGE"):
        return get_therapy_choice_message()
    elif (name == "THERAPY_ASK_TO_CHANGE_MESSAGE"):
        return get_therapy_ask_to_change_message()
    elif (name == "THERAPY_CHANGE_PHOTO_MESSAGE"):
        return get_therapy_change_photo_message()
    elif (name == "THERAPY_BEGIN_FIRST_MESSAGE"):
        return get_therapy_begin_first_message()
    elif (name == "THERAPY_BEGIN_SECOND_MESSAGE"):
        return get_therapy_begin_second_message()
    elif (name == "ASK_WHAT_TO_DO"):
        return get_ask_what_to_do_message()
    elif (name == "ERROR_MESSAGE"):
        return get_error_message()
    elif (name == "GOODBYE_MESSAGE"):
        return get_goodbye_message()
    elif (name == "UPLOAD_IMAGE_MESSAGE"):
        return get_upload_image_message()
    elif (name == "FINISH_UPLOAD_IMAGE_MESSAGE"):
        return get_finish_upload_image_message()
        