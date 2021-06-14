import os, random

from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

import shutil

from translate import translate
from database import daoImage, daoUser, daoQuestion, daoCurrentQuestions, daoPermission
import utils, get_history
from image_question import encode, beam_search_predict, encoder_model, decoder_model
from google_trans_new import google_translator

TOKEN = ""
MENU, CHOOSING, THERAPY, UPLOAD_IMAGES, END_CONVERSATION, DELETE, PERMISSION = range(7)
FORCE_LANGUAGE = None

def start(update: Update, context: CallbackContext) -> int:
    user_name = update.message.from_user.first_name
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    if daoPermission.get_user_permission(update.message.from_user.id) == None:
        welcome_new_user(update, context)

        utils.create_user_image_dir(update.message.from_user.id)

        daoUser.set_user(update.message.from_user.id, user_name, update.message.from_user.language_code)

        return PERMISSION

    utils.create_user_image_dir(update.message.from_user.id)

    daoCurrentQuestions.delete_all_current_questions()
    daoImage.delete_all_selection()
    daoUser.set_user(update.message.from_user.id, user_name, update.message.from_user.language_code)

    context.bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=open(utils.BOT_WELCOME, 'rb')
    )

    update.message.reply_text(
        translate.get_message(user_language, "WELCOME_MESSAGE").format(user_name),
        reply_markup=translate.get_keyboard(user_language, "MENU_KEYBOARD")
    )

    return MENU

def welcome_new_user(update: Update, context: CallbackContext):
    welcome_messages(update, context)
    tutorial_messages(update, context)

    context.job_queue.run_once(ask_for_permission, 49, context=update.message.chat_id)

def callback_info_message_1(context: CallbackContext):
    user_info = daoUser.get_user(context.job.context)
    user_language = translate.get_language(user_info[1], FORCE_LANGUAGE)

    context.bot.send_message(chat_id=context.job.context, text=translate.get_message(user_language, "INFO_MESSAGE").format(user_info[0]))

def callback_info_message_2(context: CallbackContext):
    user_info = daoUser.get_user(context.job.context)
    user_language = translate.get_language(user_info[1], FORCE_LANGUAGE)

    context.bot.send_message(chat_id=context.job.context, text=translate.get_message(user_language, "INFO_MESSAGE_2"))

def callback_info_message_3(context: CallbackContext):
    user_info = daoUser.get_user(context.job.context)
    user_language = translate.get_language(user_info[1], FORCE_LANGUAGE)

    context.bot.send_message(chat_id=context.job.context, text=translate.get_message(user_language, "INFO_MESSAGE_3"))

def welcome_messages(update: Update, context: CallbackContext):
    context.bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=open(utils.BOT_FIRST_WELCOME, 'rb')
    )

    context.job_queue.run_once(callback_info_message_1, 0, context=update.message.chat_id)
    context.job_queue.run_once(callback_info_message_2, 7, context=update.message.chat_id)
    context.job_queue.run_once(callback_info_message_3, 12, context=update.message.chat_id)

def callback_tutorial_message_1(context: CallbackContext):
    user_info = daoUser.get_user(context.job.context)
    user_language = translate.get_language(user_info[1], FORCE_LANGUAGE)

    context.bot.send_message(chat_id=context.job.context, text=translate.get_message(user_language, "TUTORIAL_MESSAGE").format(user_info[0]))

def callback_tutorial_message_2(context: CallbackContext):
    user_info = daoUser.get_user(context.job.context)
    user_language = translate.get_language(user_info[1], FORCE_LANGUAGE)

    context.bot.send_message(chat_id=context.job.context, text=translate.get_message(user_language, "TUTORIAL_MESSAGE_2").format(user_info[0]))

def callback_tutorial_message_3(context: CallbackContext):
    user_info = daoUser.get_user(context.job.context)
    user_language = translate.get_language(user_info[1], FORCE_LANGUAGE)

    context.bot.send_message(chat_id=context.job.context, text=translate.get_message(user_language, "TUTORIAL_MESSAGE_3").format(user_info[0]))

def callback_tutorial_message_4(context: CallbackContext):
    user_info = daoUser.get_user(context.job.context)
    user_language = translate.get_language(user_info[1], FORCE_LANGUAGE)

    context.bot.send_message(chat_id=context.job.context, text=translate.get_message(user_language, "TUTORIAL_MESSAGE_4").format(user_info[0]))

def callback_tutorial_message_5(context: CallbackContext):
    user_info = daoUser.get_user(context.job.context)
    user_language = translate.get_language(user_info[1], FORCE_LANGUAGE)

    context.bot.send_message(chat_id=context.job.context, text=translate.get_message(user_language, "TUTORIAL_MESSAGE_5").format(user_info[0]))

def callback_tutorial_image_1(context: CallbackContext):
    user_info = daoUser.get_user(context.job.context)
    user_language = translate.get_language(user_info[1], FORCE_LANGUAGE)

    context.bot.sendPhoto(
        chat_id=context.job.context,
        photo=open(utils.get_tutorial_title(user_language), 'rb')
    )

def callback_tutorial_image_2(context: CallbackContext):
    user_info = daoUser.get_user(context.job.context)
    user_language = translate.get_language(user_info[1], FORCE_LANGUAGE)

    context.bot.sendPhoto(
        chat_id=context.job.context,
        photo=open(utils.get_button_image(user_language), 'rb')
    )

def callback_tutorial_image_3(context: CallbackContext):
    context.bot.sendPhoto(
        chat_id=context.job.context,
        photo=open(utils.BOT_TUTORIAL_3, 'rb')
    )

def tutorial_messages(update: Update, context: CallbackContext):
    context.job_queue.run_once(callback_tutorial_image_1, 15, context=update.message.chat_id)
    context.job_queue.run_once(callback_tutorial_message_1, 16, context=update.message.chat_id)
    context.job_queue.run_once(callback_tutorial_image_2, 24, context=update.message.chat_id)
    context.job_queue.run_once(callback_tutorial_message_2, 25, context=update.message.chat_id)
    context.job_queue.run_once(callback_tutorial_message_3, 29, context=update.message.chat_id)
    context.job_queue.run_once(callback_tutorial_image_3, 37, context=update.message.chat_id)
    context.job_queue.run_once(callback_tutorial_message_4, 38, context=update.message.chat_id)
    context.job_queue.run_once(callback_tutorial_message_5, 43, context=update.message.chat_id)

def ask_for_permission(context: CallbackContext):
    user_info = daoUser.get_user(context.job.context)
    user_language = translate.get_language(user_info[1], FORCE_LANGUAGE)

    context.bot.sendPhoto(
        chat_id=context.job.context,
        photo=open(utils.get_tutorial_permission(user_language), 'rb')
    )

    context.bot.send_message(chat_id=context.job.context, text=translate.get_message(user_language, "QUESTION_MESSAGE"), reply_markup=translate.get_keyboard(user_language, "PERMISSION_KEYBOARD"))

def ask_again_for_permission(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)
    user_permission = daoPermission.get_user_permission(update.message.from_user.id)

    if user_permission != None:
        context.bot.sendPhoto(
            chat_id=update.message.chat_id,
            photo=open(utils.BOT_GOODBYE, 'rb')
        )

        update.message.reply_text(
            translate.get_message(user_language, "SORRY_MESSAGE"),
            reply_markup=translate.get_keyboard(user_language, "END_CONVERSATION_KEYBOARD")
        )

        daoPermission.deleteUserPermission(update.message.from_user.id)

        return END_CONVERSATION

    daoPermission.set_permission(update.message.from_user.id, 0)

    update.message.reply_text(
        translate.get_message(user_language, "QUESTION_MESSAGE_2"),
        reply_markup=translate.get_keyboard(user_language, "PERMISSION_KEYBOARD")
    )

    return PERMISSION

def permission_given(update: Update, context: CallbackContext) -> int:
    user_name = update.message.from_user.first_name
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)
    
    daoPermission.set_permission(update.message.from_user.id, 1)

    context.bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=open(utils.BOT_WELCOME, 'rb')
    )

    update.message.reply_text(
        translate.get_message(user_language, "WELCOME_MESSAGE").format(user_name),
        reply_markup=translate.get_keyboard(user_language, "MENU_KEYBOARD")
    )
    
    return MENU

def therapy_choice(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    user_images = daoImage.get_user_images(update.message.from_user.id)

    if user_images == []:
        update.message.reply_text(
            translate.get_message(user_language, "NO_IMAGES_MESSAGE"),
            reply_markup=translate.get_keyboard(user_language, "MENU_KEYBOARD")
        )

        return MENU

    update.message.reply_text(
        translate.get_message(user_language, "THERAPY_CHOICE_MESSAGE")
    )

    random_image = user_images[random.randint(0, len(user_images) - 1)]

    daoImage.set_selected_image(update.message.from_user.id, random_image)

    context.bot.sendPhoto(chat_id=update.message.chat_id,
        photo=open(os.path.join(utils.DIR_PATH, "images", "user-images", str(update.message.from_user.id), str(random_image) + ".jpg"), 'rb'))

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

    user_images = daoImage.get_user_images(update.message.from_user.id)
    random_image = user_images[random.randint(0, len(user_images) - 1)]

    daoImage.set_selected_image(update.message.from_user.id, random_image)

    context.bot.sendPhoto(chat_id=update.message.chat_id,
        photo=open(os.path.join(utils.DIR_PATH, "images", "user-images", str(update.message.from_user.id), str(random_image) + ".jpg"), 'rb'))

    update.message.reply_text(
        translate.get_message(user_language, "THERAPY_ASK_TO_CHANGE_MESSAGE"),
        reply_markup=translate.get_keyboard(user_language, "THERAPY_CHOOSING_KEYBOARD")
    )

    return CHOOSING

def begin_therapy(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)
    
    update.message.reply_text(
        translate.get_message(user_language, "THERAPY_BEGIN_FIRST_MESSAGE")
    )

    image = daoImage.get_selected_image(update.message.from_user.id)

    encoded_image = encode(os.path.join(utils.DIR_PATH, "images", "user-images", str(update.message.from_user.id), str(image) + ".jpg"))
    
    q = ['When was this picture taken?', 'How long ago was this picture taken?', 'What year was this photo taken?', 'How old were you when this picture was taken?']    
    question = random.choice(q)

    translator = google_translator()

    update.message.reply_text(
        translator.translate(question, lang_tgt=user_language),
        reply_markup=translate.get_keyboard(user_language, "THERAPY_KEYBOARD")
    )

    daoCurrentQuestions.set_user_current_questions(update.message.from_user.id, [question], 0)

    questions = beam_search_predict(encoded_image)
    final_questions = []

    for i in range(4):
        selected_question = random.choice(questions)
        final_questions.append(selected_question)
        questions.remove(selected_question)

    daoCurrentQuestions.set_user_current_questions(update.message.from_user.id, final_questions, 1)

    return THERAPY

def answer_therapy(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        translate.get_message(user_language, "BOT_ANSWER"),
        reply_markup=translate.get_keyboard(user_language, "THERAPY_KEYBOARD")
    )

    image = daoImage.get_selected_image(update.message.from_user.id)
    questions = daoCurrentQuestions.get_user_current_questions(update.message.from_user.id)
    
    translator = google_translator()

    daoQuestion.set_question(image, translator.translate(questions[0], lang_tgt=user_language), update.message.text, update.message.from_user.id)
    
    daoCurrentQuestions.delete_user_current_question(update.message.from_user.id, questions[0])

    if daoCurrentQuestions.user_has_current_questions(update.message.from_user.id):
        update.message.reply_text(
            translator.translate(questions[1], lang_tgt=user_language),
            reply_markup=translate.get_keyboard(user_language, "THERAPY_KEYBOARD")
        )

        return THERAPY
    else:
        update.message.reply_text(
            translate.get_message(user_language, "THERAPY_NO_MORE_QUESTIONS_MESSAGE"),
            reply_markup=translate.get_keyboard(user_language, "THERAPY_CHOOSING_KEYBOARD")
        )

        user_images = daoImage.get_user_images(update.message.from_user.id)
        random_image = user_images[random.randint(0, len(user_images) - 1)]

        daoImage.set_selected_image(update.message.from_user.id, random_image)

        context.bot.sendPhoto(chat_id=update.message.chat_id,
            photo=open(os.path.join(utils.DIR_PATH, "images", "user-images", str(update.message.from_user.id), str(random_image) + ".jpg"), 'rb'))

        update.message.reply_text(
            translate.get_message(user_language, "THERAPY_ASK_TO_CHANGE_MESSAGE"),
            reply_markup=translate.get_keyboard(user_language, "THERAPY_CHOOSING_KEYBOARD")
        )

        return CHOOSING

def change_question_therapy(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    if daoCurrentQuestions.user_has_current_questions(update.message.from_user.id):
        questions = daoCurrentQuestions.get_user_current_questions(update.message.from_user.id)
        daoCurrentQuestions.delete_user_current_question(update.message.from_user.id, questions[0])

        translator = google_translator()

        update.message.reply_text(
            translator.translate(questions[0], lang_tgt=user_language),
            reply_markup=translate.get_keyboard(user_language, "THERAPY_KEYBOARD")
        )

        return THERAPY
    else:
        update.message.reply_text(
            translate.get_message(user_language, "THERAPY_NO_MORE_QUESTIONS_MESSAGE"),
            reply_markup=translate.get_keyboard(user_language, "THERAPY_CHOOSING_KEYBOARD")
        )

        user_images = daoImage.get_user_images(update.message.from_user.id)
        random_image = user_images[random.randint(0, len(user_images) - 1)]

        daoImage.set_selected_image(update.message.from_user.id, random_image)

        context.bot.sendPhoto(chat_id=update.message.chat_id,
            photo=open(os.path.join(utils.DIR_PATH, "images", "user-images", str(update.message.from_user.id), str(random_image) + ".jpg"), 'rb'))

        update.message.reply_text(
            translate.get_message(user_language, "THERAPY_ASK_TO_CHANGE_MESSAGE"),
            reply_markup=translate.get_keyboard(user_language, "THERAPY_CHOOSING_KEYBOARD")
        )

        return CHOOSING

def change_photo_therapy(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    user_images = daoImage.get_user_images(update.message.from_user.id)
    random_image = user_images[random.randint(0, len(user_images) - 1)]

    daoImage.set_selected_image(update.message.from_user.id, random_image)

    daoCurrentQuestions.delete_user_current_questions(update.message.from_user.id)

    context.bot.sendPhoto(chat_id=update.message.chat_id,
        photo=open(os.path.join(utils.DIR_PATH, "images", "user-images", str(update.message.from_user.id), str(random_image) + ".jpg"), 'rb'))

    update.message.reply_text(
        translate.get_message(user_language, "THERAPY_ASK_TO_CHANGE_MESSAGE"),
        reply_markup=translate.get_keyboard(user_language, "THERAPY_CHOOSING_KEYBOARD")
    )

    return CHOOSING

def finish_therapy(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    daoCurrentQuestions.delete_user_current_questions(update.message.from_user.id)
    daoImage.delete_selected_image(update.message.from_user.id)

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

def download_history(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    user_questions = daoQuestion.get_all_question(update.message.from_user.id)

    if user_questions == None:
        update.message.reply_text(
            translate.get_message(user_language, "NO_IMAGES_DOWNLOAD_MESSAGE"),
            reply_markup=translate.get_keyboard(user_language, "MENU_KEYBOARD")
        )

        return MENU

    context.bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=open(utils.BOT_PDF, 'rb')
    )

    update.message.reply_text(
        translate.get_message(user_language, "SENDING_PDF_MESSAGE")
    )

    get_history.generate_pdf(update.message.from_user.id, update.message.from_user.name, update.message.from_user.language_code)

    document_directory = os.path.join(utils.DIR_PATH, "images", "user-images", str(update.message.from_user.id), "history.pdf")

    with open(document_directory, "rb") as file:
        context.bot.send_document(chat_id=update.message.from_user.id, document=file,  
            filename='history.pdf')

    update.message.reply_text(
        translate.get_message(user_language, "ASK_WHAT_TO_DO"), 
        reply_markup=translate.get_keyboard(user_language, "MENU_KEYBOARD")
    )

    return MENU

def delete_data(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        translate.get_message(user_language, "DELETE_DATA_MESSAGE"), 
        reply_markup=translate.get_keyboard(user_language, "DELETE_DATA_KEYBOARD")
    )

    return DELETE

def confirm_delete_data(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    daoQuestion.delete_all_questions(update.message.from_user.id)
    daoImage.delete_all_images(update.message.from_user.id)
    daoUser.delete_user(update.message.from_user.id)

    user_image_dir = os.path.join(utils.DIR_PATH, "images", "user-images", str(update.message.from_user.id))

    if os.path.exists(user_image_dir):
        shutil.rmtree(user_image_dir)

    update.message.reply_text(
        translate.get_message(user_language, "CONFIRM_DELETE_DATA_MESSAGE"), 
        reply_markup=translate.get_keyboard(user_language, "MENU_KEYBOARD")
    )

    return MENU

def confirm_keep_data(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    update.message.reply_text(
        translate.get_message(user_language, "ASK_WHAT_TO_DO"),
        reply_markup=translate.get_keyboard(user_language, "MENU_KEYBOARD")
    )

    return MENU

def uploading_images(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    utils.create_user_image_dir(update.message.from_user.id)

    new_image_id = daoImage.get_num_images(update.message.from_user.id)
    daoImage.set_user_image(update.message.from_user.id, new_image_id)

    file = context.bot.getFile(update.message.photo[-1].file_id)
    file.download(os.path.join(utils.DIR_PATH, 'images', 'user-images', str(update.message.from_user.id), 
        str(new_image_id) + '.jpg'))

    return UPLOAD_IMAGES

def finish_uploading(update: Update, context: CallbackContext) -> int:
    user_language = translate.get_language(update.message.from_user.language_code, FORCE_LANGUAGE)

    context.bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=open(utils.BOT_IMAGE_SEND, 'rb')
    )

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

    context.bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=open(utils.BOT_GOODBYE, 'rb')
    )

    update.message.reply_text(
        translate.get_message(user_language, "GOODBYE_MESSAGE"),
        reply_markup=translate.get_keyboard(user_language, "END_CONVERSATION_KEYBOARD")
    )

    return END_CONVERSATION

def main() -> None:
    encoder_model()
    decoder_model()

    print("Bot is running.")

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states = {
            MENU: [
                MessageHandler(Filters.regex(translate.get_regex(0, 0, "MENU_KEYBOARD")), therapy_choice),
                MessageHandler(Filters.regex(translate.get_regex(0, 1, "MENU_KEYBOARD")), upload_images_choice),
                MessageHandler(Filters.regex(translate.get_regex(1, 0, "MENU_KEYBOARD")), download_history),
                MessageHandler(Filters.regex(translate.get_regex(1, 1, "MENU_KEYBOARD")), delete_data),
            ],
            PERMISSION: [
                MessageHandler(Filters.regex(translate.get_regex(0, 0, "PERMISSION_KEYBOARD")), permission_given),
                MessageHandler(Filters.regex(translate.get_regex(0, 1, "PERMISSION_KEYBOARD")), ask_again_for_permission),
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
            END_CONVERSATION: [
                MessageHandler(Filters.regex(translate.get_regex(0, 0, "END_CONVERSATION_KEYBOARD")), start)
            ],
            DELETE: [
                MessageHandler(Filters.regex(translate.get_regex(0, 0, "DELETE_DATA_KEYBOARD")), confirm_delete_data),
                MessageHandler(Filters.regex(translate.get_regex(0, 1, "DELETE_DATA_KEYBOARD")), confirm_keep_data),
            ],
        },
        fallbacks=[MessageHandler(Filters.regex(translate.get_regex(2, 0, "MENU_KEYBOARD")), exit)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()