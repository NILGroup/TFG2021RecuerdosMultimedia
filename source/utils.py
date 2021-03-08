import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROFILE_PICTURE = os.path.join(DIR_PATH, "images", "bot-images", "bot-image.jpeg")

def create_user_image_dir(user_id):
    user_image_dir = os.path.join(DIR_PATH, 'images', 'user-images', str(user_id))

    if not os.path.exists(user_image_dir):
        os.mkdir(user_image_dir)