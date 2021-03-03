import os

from telegram import Update, Bot, File
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
import image_classifier

TOKEN = "1634959001:AAHUMcz1JFSeQExcsRm_gb_RB3CSKA_SclI"
MENU, CHOOSING, THERAPY, CLASSIFIER = range(4)
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROFILE_PICTURE = os.path.join(DIR_PATH, "data", "bot-images", "bot-image.jpeg")
FORCE_LANGUAGE = 'es'

def start(update: Update, context: CallbackContext) -> int:
    user_name = update.message.from_user.first_name
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    context.bot.sendPhoto(chat_id=update.message.chat_id,
        photo=open(PROFILE_PICTURE, 'rb'))

    update.message.reply_text(translate.welcome_message(user_language).format(user_name),
        reply_markup=translate.menu_keyboard(user_language))

    return MENU

def therapy_choice(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(translate.therapy_choice_message(user_language))

    context.bot.sendPhoto(chat_id=update.message.chat_id,
        photo=open(PROFILE_PICTURE, 'rb'))

    update.message.reply_text(translate.therapy_ask_to_change_message(user_language),
        reply_markup=translate.therapy_choosing_keyboard(user_language))

    return CHOOSING

def new_therapy_choice(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(translate.therapy_change_photo_message(user_language))

    context.bot.sendPhoto(chat_id=update.message.chat_id,
        photo=open(PROFILE_PICTURE, 'rb'))

    update.message.reply_text(translate.therapy_ask_to_change_message(user_language),
        reply_markup=translate.therapy_choosing_keyboard(user_language))

    return CHOOSING

def begin_therapy(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)
    
    update.message.reply_text(translate.therapy_begin_first_message(user_language))

    update.message.reply_text(translate.therapy_begin_second_message(user_language),
        reply_markup=translate.therapy_keyboard(user_language))

    return THERAPY

def answer_therapy(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(f'Answer: {text.lower()}',
        reply_markup=translate.therapy_keyboard(user_language))

    return THERAPY

def change_question_therapy(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text("Change question",
        reply_markup=translate.therapy_keyboard(user_language))

    return THERAPY

def change_photo_therapy(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text("Change photo", reply_markup=translate.therapy_keyboard(user_language))

    return THERAPY

def finish_therapy(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(translate.menu_ask_what_to_do(user_language),
        reply_markup=translate.menu_keyboard(user_language))

    return MENU

def upload_images_choice(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text("Por favor, sube la imágen que quieras clasificar...", 
        reply_markup=translate.menu_keyboard(user_language)
    )

    return CLASSIFIER

def read_stories_choice(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(translate.error_message(user_language), 
        reply_markup=translate.menu_keyboard(user_language)
    )

    return MENU

def download_stories_choice(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(translate.error_message(user_language), 
        reply_markup=translate.menu_keyboard(user_language)
    )

    return MENU

def classify_image(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text("mmm....", 
        reply_markup=translate.menu_keyboard(user_language)
    )
    
    img_name = 'tmp_' + str(update.message.from_user.id) + '.jpg'
    file = context.bot.getFile(update.message.photo[-1].file_id)
    file.download(os.path.join(DIR_PATH, 'data', 'user-images', img_name))
    prediction = image_classifier.predict(img_name)

    update.message.reply_text("Me parece que eso es un " + prediction, 
        reply_markup=translate.menu_keyboard(user_language)
    )

    return MENU

def exit(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        translate.goodby_message(user_language)
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
                MessageHandler(Filters.regex(translate.menu_regex(0, 0)), therapy_choice),
                MessageHandler(Filters.regex(translate.menu_regex(0, 1)), upload_images_choice),
                MessageHandler(Filters.regex(translate.menu_regex(1, 0)), read_stories_choice),
                MessageHandler(Filters.regex(translate.menu_regex(1, 1)), download_stories_choice),
            ],
            CHOOSING: [
                MessageHandler(Filters.regex(translate.therapy_choosing_regex(0, 0)), begin_therapy),
                MessageHandler(Filters.regex(translate.therapy_choosing_regex(0, 1)), new_therapy_choice),
                MessageHandler(Filters.regex(translate.therapy_regex(1, 0)), finish_therapy),
            ],
            THERAPY: [
                MessageHandler(Filters.regex(translate.therapy_regex(0, 0)), change_question_therapy),
                MessageHandler(Filters.regex(translate.therapy_regex(0, 1)), change_photo_therapy),
                MessageHandler(Filters.regex(translate.therapy_regex(1, 0)), finish_therapy),
                MessageHandler(Filters.text, answer_therapy),
            ],
            CLASSIFIER: [
                MessageHandler(Filters.photo, classify_image)
            ],
        },

        fallbacks=[MessageHandler(Filters.regex(translate.menu_regex(2, 0)), exit)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()