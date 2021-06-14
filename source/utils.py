from operator import truediv
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
BOT_FIRST_WELCOME = os.path.join(DIR_PATH, "images", "bot-images", "remi_first_welcome.png")
BOT_WELCOME = os.path.join(DIR_PATH, "images", "bot-images", "robot_welcome.jpg")
BOT_IMAGE_SEND = os.path.join(DIR_PATH, "images", "bot-images", "robot_image_send.jpg")
BOT_GOODBYE = os.path.join(DIR_PATH, "images", "bot-images", "robot_goodbye.jpg")
BOT_PDF = os.path.join(DIR_PATH, "images", "bot-images", "robot_image_pdf.png")
BOT_TUTORIAL_1_EN = os.path.join(DIR_PATH, "images", "bot-images", "tutorial_1_en.png")
BOT_TUTORIAL_1_ES = os.path.join(DIR_PATH, "images", "bot-images", "tutorial_1_es.png")
BOT_TUTORIAL_1_FR = os.path.join(DIR_PATH, "images", "bot-images", "tutorial_1_fr.png")
BOT_TUTORIAL_2_EN = os.path.join(DIR_PATH, "images", "bot-images", "tutorial_2_en.png")
BOT_TUTORIAL_2_ES = os.path.join(DIR_PATH, "images", "bot-images", "tutorial_2_es.png")
BOT_TUTORIAL_2_FR = os.path.join(DIR_PATH, "images", "bot-images", "tutorial_2_fr.png")
BOT_TUTORIAL_3 = os.path.join(DIR_PATH, "images", "bot-images", "tutorial_3.png")
BOT_TUTORIAL_4_EN = os.path.join(DIR_PATH, "images", "bot-images", "tutorial_4_en.png")
BOT_TUTORIAL_4_ES = os.path.join(DIR_PATH, "images", "bot-images", "tutorial_4_es.png")
BOT_TUTORIAL_4_FR = os.path.join(DIR_PATH, "images", "bot-images", "tutorial_4_fr.png")

def create_user_image_dir(user_id):
    user_image_dir = os.path.join(DIR_PATH, 'images', 'user-images', str(user_id))

    if not os.path.exists(user_image_dir):
        os.mkdir(user_image_dir)

def check_if_new_user(user_id):
    user_image_dir = os.path.join(DIR_PATH, 'images', 'user-images', str(user_id))

    if not os.path.exists(user_image_dir):
        return True

    return False

def get_tutorial_title(language):
    if language == "en":
        return BOT_TUTORIAL_1_EN
    elif language == "es":
        return BOT_TUTORIAL_1_ES
    elif language == "fr":
        return BOT_TUTORIAL_1_FR
    
    return BOT_TUTORIAL_2_EN

def get_button_image(language):
    if language == "en":
        return BOT_TUTORIAL_2_EN
    elif language == "es":
        return BOT_TUTORIAL_2_ES
    elif language == "fr":
        return BOT_TUTORIAL_2_FR
    
    return BOT_TUTORIAL_2_EN

def get_tutorial_permission(language):
    if language == "en":
        return BOT_TUTORIAL_4_EN
    elif language == "es":
        return BOT_TUTORIAL_4_ES
    elif language == "fr":
        return BOT_TUTORIAL_4_FR
    
    return BOT_TUTORIAL_4_EN