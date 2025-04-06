from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_menu() -> ReplyKeyboardMarkup:
    """
    
    """
    buttons = [
        [KeyboardButton(text="Меню")],
        [KeyboardButton(text="Информация о боте")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
