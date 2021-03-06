from telegram import ReplyKeyboardMarkup

from . import keyboards, messages

ENGLISH, SPANISH = range(2)

def get_language(user_language, force_language):
    if force_language != None:
        return force_language
    
    return user_language

# KEYBOARDS

def get_keyboard(language, keyboard_name):
    if language == "en":
        return ReplyKeyboardMarkup(keyboards.get_keyboard(keyboard_name)[ENGLISH], resize_keyboard=True)
    elif language == "es":
        return ReplyKeyboardMarkup(keyboards.get_keyboard(keyboard_name)[SPANISH], resize_keyboard=True)
    else:
        return ReplyKeyboardMarkup(keyboards.get_keyboard(keyboard_name)[ENGLISH], resize_keyboard=True)


# KEYBOARD_OUTPUT_REGEX

def get_regex(row, column, keyboard_name):
    regex = keyboards.get_keyboard(keyboard_name)[0][row][column]

    for keyboard in keyboards.get_keyboard(keyboard_name):
        if regex == keyboard[row][column]:
            continue

        regex += ('|' + keyboard[row][column])
    
    return regex

# MESSAGES

def get_message(language, message_name):
    if language == "en":
        return messages.get_message(message_name)[ENGLISH]
    elif language == "es":
        return messages.get_message(message_name)[SPANISH]
    else:
        return messages.get_message(message_name)[ENGLISH]