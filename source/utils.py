import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
BOT_WELCOME = os.path.join(DIR_PATH, "images", "bot-images", "robot_welcome.jpg")
BOT_IMAGE_SEND = os.path.join(DIR_PATH, "images", "bot-images", "robot_image_send.jpg")
BOT_GOODBYE = os.path.join(DIR_PATH, "images", "bot-images", "robot_goodbye.jpg")

def create_user_image_dir(user_id):
    user_image_dir = os.path.join(DIR_PATH, 'images', 'user-images', str(user_id))

    if not os.path.exists(user_image_dir):
        os.mkdir(user_image_dir)