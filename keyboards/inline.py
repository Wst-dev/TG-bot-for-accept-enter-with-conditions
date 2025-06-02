from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import config

def create_subscribe_keyboard() -> InlineKeyboardMarkup:
    keyboard = []
    
    # Добавляем кнопки для каждого канала из списка
    for channel in config.channel_id:
        channel= channel[1:]
        keyboard.append([
            InlineKeyboardButton(
                text=f"Подписаться на канал {channel}",
                url=f"https://t.me/{channel}"
            )
        ])
    
    # Добавляем кнопку проверки подписки в конце
    keyboard.append([
        InlineKeyboardButton(
            text="Я подписался ✅",
            callback_data="check_subscription"
        )
    ])
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
