import os, random

from telegram import Update, Bot, File, user
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

from PIL import Image

from translate import translate
from database import daoImage, daoUser, daoQuestion
import utils


TOKEN = "1634959001:AAHUMcz1JFSeQExcsRm_gb_RB3CSKA_SclI"
MENU, CHOOSING, THERAPY, UPLOAD_IMAGES = range(4)
FORCE_LANGUAGE = 'es'

def start(update: Update, context: CallbackContext) -> int:
    user_name = update.message.from_user.first_name
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    utils.create_user_image_dir(update.message.from_user.id)

    daoUser.set_user(update.message.from_user.id, user_name)

    context.bot.sendPhoto(chat_id=update.message.chat_id,
        photo=open(utils.PROFILE_PICTURE, 'rb'))

    update.message.reply_text(
        translate.get_message(user_language, "WELCOME_MESSAGE").format(user_name),
        reply_markup=translate.get_keyboard(user_language, "MENU_KEYBOARD")
    )

    return MENU

def therapy_choice(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        translate.get_message(user_language, "THERAPY_CHOICE_MESSAGE")
    )

    context.bot.sendPhoto(chat_id=update.message.chat_id,
        photo=open(utils.PROFILE_PICTURE, 'rb'))

    update.message.reply_text(
        translate.get_message(user_language, "THERAPY_ASK_TO_CHANGE_MESSAGE"),
        reply_markup=translate.get_keyboard(user_language, "THERAPY_CHOOSING_KEYBOARD")
    )

    return CHOOSING

def new_therapy_choice(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        translate.get_message(user_language, "THERAPY_CHANGE_PHOTO_MESSAGE")
    )

    context.bot.sendPhoto(chat_id=update.message.chat_id,
        photo=open(utils.PROFILE_PICTURE, 'rb'))

    update.message.reply_text(
        translate.therapy_ask_to_change_message(user_language),
        reply_markup=translate.get_keyboard(user_language, "THERAPY_CHOOSING_KEYBOARD")
    )

    return CHOOSING

def begin_therapy(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)
    
    update.message.reply_text(
        translate.get_message(user_language, "THERAPY_BEGIN_FIRST_MESSAGE")
    )

    update.message.reply_text(
        translate.get_message(user_language, "THERAPY_BEGIN_SECOND_MESSAGE"),
        reply_markup=translate.get_keyboard(user_language, "THERAPY_CHOOSING_KEYBOARD")
    )

    return CHOOSING

def answer_therapy(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        f'Answer: {text.lower()}', # todo: cambiar cuando se haga la función
        reply_markup=translate.get_keyboard(user_language, "THERAPY_KEYBOARD")
    )

    return THERAPY

def change_question_therapy(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        "Change question", # todo: cambiar cuando se haga la función
        reply_markup=translate.get_keyboard(user_language, "THERAPY_KEYBOARD")
    )

    return THERAPY

def change_photo_therapy(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        "Change photo",  # todo: cambiar cuando se haga la función
        reply_markup=translate.get_keyboard(user_language, "THERAPY_KEYBOARD")
    )

    return THERAPY

def finish_therapy(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        translate.get_message(user_language, "ASK_WHAT_TO_DO"),
        reply_markup=translate.get_keyboard(user_language, "MENU_KEYBOARD")
    )

    return MENU

def upload_images_choice(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        translate.get_message(user_language, "UPLOAD_IMAGE_MESSAGE"), 
        reply_markup=translate.get_keyboard(user_language, "UPLOAD_IMAGES_KEYBOARD")
    )

    return UPLOAD_IMAGES

def read_stories_choice(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        translate.get_message(user_language, "ERROR_MESSAGE"), 
        reply_markup=translate.get_keyboard(user_language, "MENU_KEYBOARD")
    )

    return MENU

def download_stories_choice(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        translate.get_message(user_language, "ERROR_MESSAGE"), 
        reply_markup=translate.get_keyboard(user_language, "MENU_KEYBOARD")
    )

    return MENU

def uploading_images(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    new_image_id = daoImage.get_num_images(update.message.from_user.id)
    daoImage.set_user_image(update.message.from_user.id, new_image_id)

    file = context.bot.getFile(update.message.photo[-1].file_id)
    file.download(os.path.join(utils.DIR_PATH, 'images', 'user-images', str(update.message.from_user.id), 
        str(new_image_id) + '.jpg'))

    return UPLOAD_IMAGES

def finish_uploading(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        translate.get_message(user_language, "FINISH_UPLOAD_IMAGE_MESSAGE")
    )

    update.message.reply_text(
        translate.get_message(user_language, "ASK_WHAT_TO_DO"), 
        reply_markup=translate.get_keyboard(user_language, "MENU_KEYBOARD")
    )

    return MENU

def exit(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        translate.get_message(user_language, "GOODBYE_MESSAGE")
    )

    return ConversationHandler.END

def main() -> None:
    print("Bot is running.")

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(


        entry_points=[CommandHandler('start', start)],

        states = {
            MENU: [
                MessageHandler(Filters.regex(translate.get_regex(0, 0, "MENU_KEYBOARD")), therapy_choice),
                MessageHandler(Filters.regex(translate.get_regex(0, 1, "MENU_KEYBOARD")), upload_images_choice),
                MessageHandler(Filters.regex(translate.get_regex(1, 0, "MENU_KEYBOARD")), read_stories_choice),
                MessageHandler(Filters.regex(translate.get_regex(1, 1, "MENU_KEYBOARD")), download_stories_choice),
            ],
            CHOOSING: [
                MessageHandler(Filters.regex(translate.get_regex(0, 0, "THERAPY_CHOOSING_KEYBOARD")), 
                    begin_therapy),
                MessageHandler(Filters.regex(translate.get_regex(0, 1, "THERAPY_CHOOSING_KEYBOARD")),
                    new_therapy_choice),
                MessageHandler(Filters.regex(translate.get_regex(1, 0, "THERAPY_KEYBOARD")), finish_therapy),
            ],
            THERAPY: [
                MessageHandler(Filters.regex(translate.get_regex(0, 0, "THERAPY_KEYBOARD")), change_question_therapy),
                MessageHandler(Filters.regex(translate.get_regex(0, 1, "THERAPY_KEYBOARD")), change_photo_therapy),
                MessageHandler(Filters.regex(translate.get_regex(1, 0, "THERAPY_KEYBOARD")), finish_therapy),
                MessageHandler(Filters.text, answer_therapy),
            ],
            UPLOAD_IMAGES: [
                MessageHandler(Filters.photo, uploading_images),
                MessageHandler(Filters.regex(translate.get_regex(0, 0, "UPLOAD_IMAGES_KEYBOARD")), finish_uploading)
            ],
        },

        fallbacks=[MessageHandler(Filters.regex(translate.get_regex(2, 0, "MENU_KEYBOARD")), exit)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()