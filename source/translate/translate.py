from telegram import ReplyKeyboardMarkup

from . import keyboards, messages

def get_language(user_language, force_language):
    if force_language != None:
        return force_language
    
    return user_language

# KEYBOARDS
def therapy_choosing_keyboard(language):
    if language == "es":
        return ReplyKeyboardMarkup(keyboards.THERAPY_CHOOSING_KEYBOARD_ES, resize_keyboard=True)
    elif language == "en":
        return ReplyKeyboardMarkup(keyboards.THERAPY_CHOOSING_KEYBOARD_EN, resize_keyboard=True)
    else:
        return ReplyKeyboardMarkup(keyboards.THERAPY_CHOOSING_KEYBOARD_EN, resize_keyboard=True)

def therapy_keyboard(language):
    if language == "es":
        return ReplyKeyboardMarkup(keyboards.THERAPY_KEYBOARD_ES, resize_keyboard=True)
    elif language == "en":
        return ReplyKeyboardMarkup(keyboards.THERAPY_KEYBOARD_EN, resize_keyboard=True)
    else:
        return ReplyKeyboardMarkup(keyboards.THERAPY_KEYBOARD_EN, resize_keyboard=True)

def menu_keyboard(language):
    if language == "es":
        return ReplyKeyboardMarkup(keyboards.MENU_KEYBOARD_ES, resize_keyboard=True)
    elif language == "en":
        return ReplyKeyboardMarkup(keyboards.MENU_KEYBOARD_EN, resize_keyboard=True)
    else:
        return ReplyKeyboardMarkup(keyboards.MENU_KEYBOARD_EN, resize_keyboard=True)


# KEYBOARD_OUTPUT_REGEX
def therapy_choosing_regex(row, column):
    regex = keyboards.get_therapy_choosing_keyboards()[0][row][column]

    for keyboard in keyboards.get_therapy_choosing_keyboards():
        if regex == keyboard[row][column]:
            continue

        regex += ('|' + keyboard[row][column])
    
    return regex

def therapy_regex(row, column):
    regex = keyboards.get_therapy_keyboards()[0][row][column]

    for keyboard in keyboards.get_therapy_keyboards():
        if regex == keyboard[row][column]:
            continue

        regex += ('|' + keyboard[row][column])
    
    return regex

def menu_regex(row, column):
    regex = keyboards.get_menu_keyboards()[0][row][column]

    for keyboard in keyboards.get_menu_keyboards():
        if regex == keyboard[row][column]:
            continue
        
        regex += ('|' + keyboard[row][column])
    
    return regex

# MESSAGES
def welcome_message(language):
    if language == "es":
        return messages.WELCOME_MESSAGE_ES
    elif language == "en":
        return messages.WELCOME_MESSAGE_EN
    else:
        return messages.WELCOME_MESSAGE_EN

def therapy_choice_message(language):
    if language == "es":
        return messages.THERAPY_CHOICE_MESSAGE_ES
    elif language == "en":
        return messages.THERAPY_CHOICE_MESSAGE_EN
    else:
        return messages.THERAPY_CHOICE_MESSAGE_EN

def therapy_ask_to_change_message(language):
    if language == "es":
        return messages.THERAPY_ASK_TO_CHANGE_MESSAGE_ES
    elif language == "en":
        return messages.THERAPY_ASK_TO_CHANGE_MESSAGE_EN
    else:
        return messages.THERAPY_ASK_TO_CHANGE_MESSAGE_EN

def therapy_change_photo_message(language):
    if language == "es":
        return messages.THERAPY_CHANGE_PHOTO_MESSAGE_ES
    elif language == "en":
        return messages.THERAPY_CHANGE_PHOTO_MESSAGE_EN
    else:
        return messages.THERAPY_CHANGE_PHOTO_MESSAGE_EN

def therapy_begin_first_message(language):
    if language == "es":
        return messages.THERAPY_BEGIN_FIRST_MESSAGE_ES
    elif language == "en":
        return messages.THERAPY_BEGIN_FIRST_MESSAGE_EN
    else:
        return messages.THERAPY_BEGIN_FIRST_MESSAGE_EN

def therapy_begin_second_message(language):
    if language == "es":
        return messages.THERAPY_BEGIN_SECOND_MESSAGE_ES
    elif language == "en":
        return messages.THERAPY_BEGIN_SECOND_MESSAGE_EN
    else:
        return messages.THERAPY_BEGIN_SECOND_MESSAGE_EN

def menu_ask_what_to_do(language):
    if language == "es":
        return messages.MENU_ASK_WHAT_TO_DO_ES
    elif language == "en":
        return messages.MENU_ASK_WHAT_TO_DO_EN
    else:
        return messages.MENU_ASK_WHAT_TO_DO_EN

def error_message(language):
    if language == "es":
        return messages.ERROR_MESSAGE_ES
    elif language == "en":
        return messages.ERROR_MESSAGE_EN
    else:
        return messages.ERROR_MESSAGE_EN

def goodby_message(language):
    if language == "es":
        return messages.GOODBY_MESSAGE_ES
    elif language == "en":
        return messages.GOODBY_MESSAGE_EN
    else:
        return messages.GOODBY_MESSAGE_EN