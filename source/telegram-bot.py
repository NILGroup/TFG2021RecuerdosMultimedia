import os
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)


# TODO: Mover todos los mensajes a un archivo para poder en un futuro tener el bot en varios idiomas.
# TODO: Añadir persistencia de daots, que un usuario mantenga sus historias, fotos, etc.
# TODO: Añadir un mensaje en caso de que el usuario no haya subido ninguna imagen antes.
# TODO: Tener un banco de expresiones en cada punto de la aplicación para que no diga siempre lo mismo.

MENU, CHOOSING, THERAPY = range(3)
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROFILE_PICTURE = os.path.join(DIR_PATH, "data", "bot-images", "bot-image.jpeg")

therapy_chooseing_keyboard = [
    ['Si', 'Siguiente'],
    ['Salir'],
]

therapy_keyboard = [
    ['Cambiar pregunta', 'Cambiar fotografía'],
    ['Terminar'],
]

menu_keyboard = [
    ['Comenzar terapia', 'Subir imágenes'],
    ['Leer mis historias', 'Descargar mis historias'],
    ['Salir'],
]

therapy_choosing_markup = ReplyKeyboardMarkup(therapy_chooseing_keyboard, resize_keyboard=True)
therapy_markup = ReplyKeyboardMarkup(therapy_keyboard, resize_keyboard=True)
menu_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)

def start(update: Update, context: CallbackContext) -> int:
    context.bot.sendPhoto(chat_id=update.message.chat_id,
        photo=open(PROFILE_PICTURE, 'rb'))
    #"/Users/alejandroaizel/Documents/GitHub/TelegramBot-test/data/bot-images/bot-image.jpeg"
    update.message.reply_text(
        "¡Hola y bienvenido a terapia! Mi nombre es Remi y estoy aqui para ayudarte. ¿Qué te gustaría hacer ahora?",
        reply_markup=menu_markup,
    )

    return MENU

def therapy_choice(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "¡Genial! Voy a comenzar eligiendo una fotografía para comenzar."
    )

    context.bot.sendPhoto(chat_id=update.message.chat_id,
        photo=open(PROFILE_PICTURE, 'rb'))

    update.message.reply_text(
        "¿te gustaría hablar sobre esta foto o prefieres cambiarla?",
        reply_markup=therapy_choosing_markup,
    )

    return CHOOSING

def new_therapy_choice(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Vamos a probar con esta otra..."
    )

    context.bot.sendPhoto(chat_id=update.message.chat_id,
        photo=open(PROFILE_PICTURE, 'rb'))

    update.message.reply_text(
        "¿te gustaría hablar sobre esta foto o prefieres cambiarla?",
        reply_markup=therapy_choosing_markup,
    )

    return CHOOSING

def begin_therapy(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Mira la fotografía e intenta recordar todo lo que puedas."
    )

    update.message.reply_text(
        "¿Recuerdas cuando fue tomada esta foto?",
        reply_markup=therapy_markup,
    )

    return THERAPY

def answer_therapy(update: Update, context: CallbackContext) -> int:
    text = update.message.text

    update.message.reply_text(
        f'Me has respondido: {text.lower()}',
        reply_markup=therapy_markup,
    )

    return THERAPY

def change_question_therapy(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Has elegido cambiar de pregunta",
        reply_markup=therapy_markup
    )

    return THERAPY

def change_photo_therapy(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Has elegido cambiar de foto",
        reply_markup=therapy_markup
    )

    return THERAPY

def finish_therapy(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "¿Qué quieres hacer ahora?",
        reply_markup=menu_markup
    )

    return MENU

def upload_images_choice(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Vaya, parece que todavía no puedo hacer esto 😕. Prueba con otra cosa."
    )

    return MENU

def read_stories_choice(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Vaya, parece que todavía no puedo hacer esto 😕. Prueba con otra cosa.",
        reply_markup=menu_markup,
    )

    return MENU

def download_stories_choice(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Vaya, parece que todavía no puedo hacer esto 😕. Prueba con otra cosa.",
        reply_markup=menu_markup,
    )

    return MENU

def exit(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Me ha encantado hablar contigo. ¡Vueve cuando quieras! 👋"
    )

    return ConversationHandler.END

def main() -> None:
    updater = Updater("1634959001:AAHUMcz1JFSeQExcsRm_gb_RB3CSKA_SclI")

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(

        entry_points=[CommandHandler('start', start)],

        states = {
            MENU: [
                MessageHandler(Filters.regex('^Comenzar terapia$'), therapy_choice),
                MessageHandler(Filters.regex('^Subir imágenes$'), upload_images_choice),
                MessageHandler(Filters.regex('^Leer mis historias$'), read_stories_choice),
                MessageHandler(Filters.regex('^Descargar mis historias$'), download_stories_choice),
            ],
            CHOOSING: [
                MessageHandler(Filters.regex('^Si$'), begin_therapy),
                MessageHandler(Filters.regex('^Siguiente$'), new_therapy_choice),
            ],
            THERAPY: [
                MessageHandler(Filters.regex('^Cambiar pregunta$'), change_question_therapy),
                MessageHandler(Filters.regex('^Cambiar fotografía$'), change_photo_therapy),
                MessageHandler(Filters.regex('^Terminar$'), finish_therapy),
                MessageHandler(Filters.text, answer_therapy),
            ],
        },

        fallbacks=[MessageHandler(Filters.regex('^Salir$'), exit)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()