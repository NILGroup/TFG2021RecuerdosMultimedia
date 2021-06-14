import random

# INFO_MESSAGE

def get_info_message():
    return [
        INFO_MESSAGE_EN, 
        INFO_MESSAGE_ES,
        INFO_MESSAGE_FR
    ]
    
INFO_MESSAGE_EN = "Hi {0}! Mi name is Remi and I'm here to help you remember those important moments of your past..."

INFO_MESSAGE_ES = "¡Hola {0}! Mi nombre es Remi y estoy aqui para ayudarte a recordar aquellos momentos de tu pasado que tan importantes son para ti..."

INFO_MESSAGE_FR = "Bonjour {0}! Je m'appelle Rémi et je suis là pour vous aider à vous souvenir de ces moments de votre passé qui sont si importants pour vous..."


# INFO_MESSAGE_2

def get_info_message_2():
    return [
        INFO_MESSAGE_2_EN, 
        INFO_MESSAGE_2_ES,
        INFO_MESSAGE_2_FR
    ]
    
INFO_MESSAGE_2_EN = "To do so, I will show you some images about your life and you will have to answer me everything you remember."

INFO_MESSAGE_2_ES = "Para ello, voy a mostrarte fotografias sobre tu vida y tú tendrás que responderme con todo lo que recuerdes."

INFO_MESSAGE_2_FR = "Pour commencer, je vais vous montrer des photos de votre vie et vous devrez me répondre avec tout ce dont vous vous souvenez."


# INFO_MESSAGE_3

def get_info_message_3():
    return [
        INFO_MESSAGE_3_EN, 
        INFO_MESSAGE_3_ES,
        INFO_MESSAGE_3_FR
    ]
    
INFO_MESSAGE_3_EN = "Before we start, let's see how to interact with me."

INFO_MESSAGE_3_ES = "Antes de empezar te voy a enseñar como interactuar conmigo."

INFO_MESSAGE_3_FR = "Avant de commencer, je vais vous montrer comment interagir avec moi."


# TUTORIAL_MESSAGE

def get_tutorial_message():
    return[
        TUTORIAL_MESSAGE_EN,
        TUTORIAL_MESSAGE_ES,
        TUTORIAL_MESSAGE_FR
    ]

TUTORIAL_MESSAGE_EN = "In order to tell me what you want to do, I will show you some buttons that will appear at the bottom of the screem. Like these..."
                                
TUTORIAL_MESSAGE_ES = "Para poder decirme lo que quieres hacer te iré mostrando unos botones que aparecerán en la parte inferior de la pantalla. Unos botones como estos..."

TUTORIAL_MESSAGE_FR = "Afin de me dire ce que vous voulez faire, je vais vous montrer quelques boutons qui apparaîtront en bas de l'écran. Des boutons comme ceux-ci..."


# TUTORIAL_MESSAGE_2

def get_tutorial_message_2():
    return[
        TUTORIAL_MESSAGE_2_EN,
        TUTORIAL_MESSAGE_2_ES,
        TUTORIAL_MESSAGE_2_FR
    ]

TUTORIAL_MESSAGE_2_EN = "When you have to write me something, those buttons will disappear and in their place the keyboard will show up."
                    
TUTORIAL_MESSAGE_2_ES = "Cuando tengas que escribirme algo, estos botones desaparecerán y en su lugar aparecerá el teclado de siempre."

TUTORIAL_MESSAGE_2_FR = "Lorsque vous devez m'écrire quelque chose, ces boutons disparaîtront et le clavier habituel apparaîtra à leur place."


# TUTORIAL_MESSAGE_3

def get_tutorial_message_3():
    return[
        TUTORIAL_MESSAGE_3_EN,
        TUTORIAL_MESSAGE_3_ES,
        TUTORIAL_MESSAGE_3_FR
    ]

TUTORIAL_MESSAGE_3_EN = "If after answering me the buttons don't appear... Don't worry! In that case, you just have to press the icon that I show you below."
                    
TUTORIAL_MESSAGE_3_ES = "Si despues de responderme no aparecen los botones... ¡No te preocupes! En ese caso solo tienes que pulsar el icono que te muestro a continuación."

TUTORIAL_MESSAGE_3_FR = "Si après m'avoir répondu les boutons n'apparaissent pas... Ne vous inquiétez pas! Dans ce cas, il vous suffit d'appuyer sur l'icône que je vous montre ci-dessous."


# TUTORIAL_MESSAGE_4

def get_tutorial_message_4():
    return[
        TUTORIAL_MESSAGE_4_EN,
        TUTORIAL_MESSAGE_4_ES,
        TUTORIAL_MESSAGE_4_FR
    ]

TUTORIAL_MESSAGE_4_EN = "Once pressed, the buttons will appear again so you can tell me what to do next."
                    
TUTORIAL_MESSAGE_4_ES = "Una vez pulsado, te volverán a aparecer los botones y así podrás decirme qué es lo siguiente que quieres hacer."

TUTORIAL_MESSAGE_4_FR = "Une fois que vous appuyer, les boutons réapparaîtront et vous pourrez ainsi me dire ce que vous voulez faire ensuite."


# TUTORIAL_MESSAGE_5

def get_tutorial_message_5():
    return[
        TUTORIAL_MESSAGE_5_EN,
        TUTORIAL_MESSAGE_5_ES,
        TUTORIAL_MESSAGE_5_FR
    ]

TUTORIAL_MESSAGE_5_EN = "Before starting I need your permission to store your photos and your answers..."
                    
TUTORIAL_MESSAGE_5_ES = "Antes de comenzar necesito que me des permiso para poder almacenar tus fotografías y tus respuestas..."

TUTORIAL_MESSAGE_5_FR = "Avant de commencer j'ai besoin de votre autorisation pour stocker vos photos et vos réponses..."

# QUESTION_MESSAGE

def get_question_message():
    return [
        QUESTION_MESSAGE_EN,
        QUESTION_MESSAGE_ES,
        QUESTION_MESSAGE_FR
    ]

QUESTION_MESSAGE_EN = "Do you agree with me storing your data and images?"

QUESTION_MESSAGE_ES = "¿Estás de acuerdo con que almacene tus datos y fotografias?"

QUESTION_MESSAGE_FR = "Acceptez-vous que je stocke vos données et photographies?"


# QUESTION_MESSAGE_2

def get_question_message_2():
    return [
        QUESTION_MESSAGE_2_EN,
        QUESTION_MESSAGE_2_ES,
        QUESTION_MESSAGE_2_FR
    ]

QUESTION_MESSAGE_2_EN = "If you don't give me permission, I won't be able to help you... I'll ask you one more time! Do you agree that I store your data and photographs?"

QUESTION_MESSAGE_2_ES = "Si no me das permiso no te podré ayudar... ¡Te lo preguntaré una vez más! ¿Estás de acuerdo con que almacene tus datos y fotografias?"

QUESTION_MESSAGE_2_FR = "Si tu ne m'en donnes pas la autorisation, je ne pourrai pas t'aider... Je vais te demander encore une fois! Acceptez-vous que je stocke vos données et photographies?"


# SORRY_MESSAGE

def get_sorry_message():
    return [
        SORRY_MESSAGE_EN,
        SORRY_MESSAGE_ES,
        SORRY_MESSAGE_FR
    ]

SORRY_MESSAGE_EN = "It's ok, if you don't agree, we have to say goodbye. Anyway, I'll be here waiting for you in case you change your mind!"

SORRY_MESSAGE_ES = "Vaya, si no estás de acuerdo nos tenemos que despedir. De todos modos, ¡estaré aquí esperándote por si cambias de opinión!"

SORRY_MESSAGE_FR = "Wow, si vous n'êtes pas d'accord, nous devons dire au revoir. Quoi qu'il en soit, je serai là à vous attendre au cas où vous changeriez d'avis!"

# WELCOME_MESSAGE

def get_welcome_message():
    return [
        WELCOME_MESSAGE_EN, 
        WELCOME_MESSAGE_ES,
        WELCOME_MESSAGE_FR
    ]
    
WELCOME_MESSAGE_EN = "Hi {0}! My name is Remi and I'm here to help you to remember. What would you like to do now?"

WELCOME_MESSAGE_ES = "¡Hola {0}! Mi nombre es Remi y estoy aqui para ayudarte a recordar. ¿Qué te gustaría hacer ahora?"

WELCOME_MESSAGE_FR = "Salut {0}! Mon prénom est Rémi et je suis ici pour vous aider à se souvenir, Que vous plairait-il de faire maintenant?"

# THERAPY_CHOICE_MESSAGE

def get_therapy_choice_message():
    return [
        THERAPY_CHOICE_MESSAGE_EN, 
        THERAPY_CHOICE_MESSAGE_ES,
        THERAPY_CHOICE_MESSAGE_FR
    ]

THERAPY_CHOICE_MESSAGE_EN = "Great! Let me choose an image for you."

THERAPY_CHOICE_MESSAGE_ES = "¡Genial! Voy a comenzar eligiendo una fotografía."

THERAPY_CHOICE_MESSAGE_FR = "Génial! Je vais commencer à choisir une photographie."


# THERAPY_ASK_TO_CHANGE_MESSAGE

def get_therapy_ask_to_change_message():
    return [
        THERAPY_ASK_TO_CHANGE_MESSAGE_EN, 
        THERAPY_ASK_TO_CHANGE_MESSAGE_ES,
        THERAPY_ASK_TO_CHANGE_MESSAGE_FR
    ]

THERAPY_ASK_TO_CHANGE_MESSAGE_EN = "Would you like to talk about this photo?"

THERAPY_ASK_TO_CHANGE_MESSAGE_ES = "¿Te gustaría hablar sobre esta foto?"

THERAPY_ASK_TO_CHANGE_MESSAGE_FR = "Voudriez vous parler de cette photographie?"


# THERAPY_CHANGE_PHOTO_MESSAGE

def get_therapy_change_photo_message():
    return [
        THERAPY_CHANGE_PHOTO_MESSAGE_EN, 
        THERAPY_CHANGE_PHOTO_MESSAGE_ES,
        THERAPY_CHANGE_PHOTO_MESSAGE_FR
    ]

THERAPY_CHANGE_PHOTO_MESSAGE_EN = "Lets try with this one..."

THERAPY_CHANGE_PHOTO_MESSAGE_ES = "Vamos a probar con esta otra..."

THERAPY_CHANGE_PHOTO_MESSAGE_FR = "Nous allons essayer avec cette autre..."


# THERAPY_NO_MORE_QUESTIONS_MESSAGE

def get_therapy_no_more_questions_message():
    return [
        THERAPY_NO_MORE_QUESTIONS_MESSAGE_EN, 
        THERAPY_NO_MORE_QUESTIONS_MESSAGE_ES,
        THERAPY_NO_MORE_QUESTIONS_MESSAGE_FR
    ]

THERAPY_NO_MORE_QUESTIONS_MESSAGE_EN = "I think it's enough, let's try with another image!"

THERAPY_NO_MORE_QUESTIONS_MESSAGE_ES = "Creo que ya es suficiente, ¡vamos a probar con otra foto!"

THERAPY_NO_MORE_QUESTIONS_MESSAGE_FR = "Je pense que c’est déjà suffisant, nous allons essayer avec une autre photographie!"


# THERAPY_BEGIN_FIRST_MESSAGE

def get_therapy_begin_first_message():
    return [
        THERAPY_BEGIN_FIRST_MESSAGE_EN, 
        THERAPY_BEGIN_FIRST_MESSAGE_ES,
        THERAPY_BEGIN_FIRST_MESSAGE_FR
    ]

THERAPY_BEGIN_FIRST_MESSAGE_EN = "Look at the image and try to remember everything you can."

THERAPY_BEGIN_FIRST_MESSAGE_ES = "Mira la fotografía e intenta recordar todo lo que puedas."

THERAPY_BEGIN_FIRST_MESSAGE_FR = "Regardez la photographie et essayez de vous rappeler de tout ce que vous pouvez."


# ASK_WHAT_TO_DO

def get_ask_what_to_do_message():
    return [
        ASK_WHAT_TO_DO_EN, 
        ASK_WHAT_TO_DO_ES,
        ASK_WHAT_TO_DO_FR
    ]

ASK_WHAT_TO_DO_EN = "What would you like to do now?"

ASK_WHAT_TO_DO_ES = "¿Qué te gustaría hacer ahora?"

ASK_WHAT_TO_DO_FR = "Qu’est-ce que vous aimeriez faire maintenant?"


# ERROR_MESSAGE

def get_error_message():
    return [
        ERROR_MESSAGE_EN, 
        ERROR_MESSAGE_ES,
        ERROR_MESSAGE_FR
    ]

ERROR_MESSAGE_EN = "Sorry, It seems I can't do this yet 😕. Try something else."

ERROR_MESSAGE_ES = "Vaya, parece que todavía no puedo hacer esto 😕. Prueba con otra cosa."

ERROR_MESSAGE_FR = "Je ne peux pas faire ça maintenant 😕. Essayez autre chose."


# GOODBYE_MESSAGE

def get_goodbye_message():
    return [
        GOODBYE_MESSAGE_EN, 
        GOODBYE_MESSAGE_ES,
        GOODBYE_MESSAGE_FR
    ]

GOODBYE_MESSAGE_EN = "I've enjoyed talking with you. Come back whenever you want! 👋"

GOODBYE_MESSAGE_ES = "Me ha encantado hablar contigo. ¡Vueve cuando quieras! 👋"

GOODBYE_MESSAGE_FR = "J’ai apprécié notre discussion. Revenez quand vous voulez! 👋"


# UPLOAD_IMAGE_MESSAGE

def get_upload_image_message():
    return [
        UPLOAD_IMAGE_MESSAGE_EN, 
        UPLOAD_IMAGE_MESSAGE_ES,
        UPLOAD_IMAGE_MESSAGE_FR
    ]

UPLOAD_IMAGE_MESSAGE_EN = "Upload the images that you want to use. Press the finish button when you are done."

UPLOAD_IMAGE_MESSAGE_ES = "Sube las imágenes que quieras utilizar. Cuando hayas terminado pulsa el botón terminar."

UPLOAD_IMAGE_MESSAGE_FR = "Téléchargez toutes les images que vous voulez utiliser. Quand vous auriez finis appuyez sur le bouton finaliser."


# FINISH_UPLOAD_IMAGE_MESSAGE

def get_finish_upload_image_message():
    return [
        FINISH_UPLOAD_IMAGE_MESSAGE_EN, 
        FINISH_UPLOAD_IMAGE_MESSAGE_ES,
        FINISH_UPLOAD_IMAGE_MESSAGE_FR
    ]

FINISH_UPLOAD_IMAGE_MESSAGE_EN = "Thanks for uploading your images! 😄"

FINISH_UPLOAD_IMAGE_MESSAGE_ES = "¡Gracias por subir tus imágenes! 😄"

FINISH_UPLOAD_IMAGE_MESSAGE_FR = "Merci de télécharger vos images ! 😄"


# DELETE_DATA_MESSAGE

def get_delete_data_message():
    return [
        DELETE_DATA_MESSAGE_EN, 
        DELETE_DATA_MESSAGE_ES,
        DELETE_DATA_MESSAGE_FR
    ]

DELETE_DATA_MESSAGE_EN = "This action will delete all your images, questions and answers. Once deleted it cannot be recovered. Are you sure you want to delete all your data?"

DELETE_DATA_MESSAGE_ES = "Esta acción eliminará todas tus imágenes, preguntas y respuestas. Una vez eliminado no se puede recuperar. ¿Estás seguro que quieres eliminar todos tus datos?"

DELETE_DATA_MESSAGE_FR = "Cette action effacera toutes les images, questions et réponses. Une fois effacées il ne sera pas possible de les récupérer. Êtes-vous sûr de vouloir effacer toutes vos données?"


# CONFIRM_DELETE_DATA_MESSAGE

def get_confirm_delete_data_message():
    return [
        CONFIRM_DELETE_DATA_MESSAGE_EN, 
        CONFIRM_DELETE_DATA_MESSAGE_ES,
        CONFIRM_DELETE_DATA_MESSAGE_FR
    ]

CONFIRM_DELETE_DATA_MESSAGE_EN = "I've remove all your data."

CONFIRM_DELETE_DATA_MESSAGE_ES = "He eliminado todos tus datos."

CONFIRM_DELETE_DATA_MESSAGE_FR = "J’ai effacé toutes vos données."


# NO_IMAGES_MESSAGE

def get_no_images_message():
    return [
        NO_IMAGES_MESSAGE_EN, 
        NO_IMAGES_MESSAGE_ES,
        NO_IMAGES_MESSAGE_FR
    ]

NO_IMAGES_MESSAGE_EN = "To start you need to upload some images. To do that, select the \"Upload images\" button."

NO_IMAGES_MESSAGE_ES = "Para poder comenzar necesito que subas alguna imágen. Para ello selecciona el botón \"Subir imágenes\" del menú principal."

NO_IMAGES_MESSAGE_FR = "Pour pouvoir réaliser la thérapie c’est nécessaire télécharger quelques images. Pour cela sélectionnez le bouton \"Télécharger les images\" du menu principal."


# NO_IMAGES_DOWNLOAD_MESSAGE

def get_no_images_download_message():
    return [
        NO_IMAGES_DOWNLOAD_MESSAGE_EN, 
        NO_IMAGES_DOWNLOAD_MESSAGE_ES,
        NO_IMAGES_DOWNLOAD_MESSAGE_FR
    ]

NO_IMAGES_DOWNLOAD_MESSAGE_EN = "In order to download your history, you first need to upload images and ask at least a few questions."

NO_IMAGES_DOWNLOAD_MESSAGE_ES = "Para poder descargar tu historial primero es necesario que subas imágenes y realices al menos algunas preguntas conmigo."

NO_IMAGES_DOWNLOAD_MESSAGE_FR = "Pour télécharger votre historique, vous devez d'abord télécharger des images et poser au moins quelques questions." # TODO

# SENDING_PDF_MESSAGE

def get_sending_pdf_message_message():
    return [
        SENDING_PDF_MESSAGE_EN, 
        SENDING_PDF_MESSAGE_ES,
        SENDING_PDF_MESSAGE_FR
    ]

SENDING_PDF_MESSAGE_EN = "I'm collecting all your information to generate your history..."

SENDING_PDF_MESSAGE_ES = "Estoy recopilando todos tus datos para generar tu historial..."

SENDING_PDF_MESSAGE_FR = "Je collecte toutes vos données pour générer votre historique..."


# FINISH_UPLOAD_IMAGE_MESSAGE

def get_bot_answer():
    random_number = random.randint(0, len(BOT_ANSWER_EN) - 1)
    
    return [
        BOT_ANSWER_EN[random_number], 
        BOT_ANSWER_ES[random_number],
        BOT_ANSWER_FR[random_number]
    ]

BOT_ANSWER_EN = [
    "Okeey",
    "Amazing!",
    "Interesting...",
    "Perfect!",
    "That's cool!",
    "Really?",
]

BOT_ANSWER_ES = [
    "Okeey",
    "¡Genial!",
    "Interesante...",
    "¡Estupendo!",
    "Que guay",
    "¿Ah si?",
]

BOT_ANSWER_FR = [
    "Okeey",
    "Génial!",
    "Intéressant...",
    "Magnifique!",
    "C’est cool",
    "Vraiment?",
]


def get_message(name):
    if (name == "WELCOME_MESSAGE"):
        return  get_welcome_message()
    elif (name == "THERAPY_CHOICE_MESSAGE"):
        return get_therapy_choice_message()
    elif (name == "THERAPY_ASK_TO_CHANGE_MESSAGE"):
        return get_therapy_ask_to_change_message()
    elif (name == "THERAPY_CHANGE_PHOTO_MESSAGE"):
        return get_therapy_change_photo_message()
    elif (name == "THERAPY_NO_MORE_QUESTIONS_MESSAGE"):
        return get_therapy_no_more_questions_message()
    elif (name == "THERAPY_BEGIN_FIRST_MESSAGE"):
        return get_therapy_begin_first_message()
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
    elif (name == "DELETE_DATA_MESSAGE"):
        return get_delete_data_message()
    elif (name == "CONFIRM_DELETE_DATA_MESSAGE"):
        return get_confirm_delete_data_message()
    elif (name == "NO_IMAGES_MESSAGE"):
        return get_no_images_message()
    elif (name == "NO_IMAGES_DOWNLOAD_MESSAGE"):
        return get_no_images_download_message()
    elif (name == "BOT_ANSWER"):
        return get_bot_answer()
    elif (name == "SENDING_PDF_MESSAGE"):
        return get_sending_pdf_message_message()
    elif (name == "INFO_MESSAGE"):
        return get_info_message()
    elif (name == "INFO_MESSAGE_2"):
        return get_info_message_2()
    elif (name == "INFO_MESSAGE_3"):
        return get_info_message_3()
    elif (name == "TUTORIAL_MESSAGE"):
        return get_tutorial_message()
    elif (name == "TUTORIAL_MESSAGE_2"):
        return get_tutorial_message_2()
    elif (name == "TUTORIAL_MESSAGE_3"):
        return get_tutorial_message_3()
    elif (name == "TUTORIAL_MESSAGE_4"):
        return get_tutorial_message_4()
    elif (name == "TUTORIAL_MESSAGE_5"):
        return get_tutorial_message_5()
    elif (name == "QUESTION_MESSAGE_2"):
        return get_question_message_2()
    elif (name == "QUESTION_MESSAGE"):
        return get_question_message()
    elif (name == "SORRY_MESSAGE"):
        return get_sorry_message()

        