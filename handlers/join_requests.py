from aiogram import Router, F, Bot
from aiogram.types import ChatJoinRequest, CallbackQuery
from keyboards import create_subscribe_keyboard
from config import config



router = Router()

async def check_subscription(user_id: int, bot: Bot) -> bool:
    try:
        for channel in config.channel_id:
            member = await bot.get_chat_member(channel, user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        return True
    except Exception:
        return False

@router.chat_join_request()
async def handle_join_request(update: ChatJoinRequest):
    # Проверяем подписку
    is_subscribed = await check_subscription(update.from_user.id, update.bot)
    
    if is_subscribed:
        # Если пользователь подписан, одобряем заявку
        await update.approve()
        await update.bot.send_message(
            update.from_user.id,
            "Спасибо за подписку! Ваша заявка на вступление в канал одобрена."
        )
    else:
        # Если не подписан, отправляем приветственное сообщение
        await update.bot.send_message(
            update.from_user.id,
            "Добро пожаловать! Для вступления в канал, пожалуйста, подпишитесь на наш канал:",
            reply_markup=create_subscribe_keyboard()
        )

@router.callback_query(F.data == "check_subscription")
async def check_subscription_callback(callback: CallbackQuery):
    # Проверяем подписку
    is_subscribed = await check_subscription(callback.from_user.id, callback.bot)
    
    if is_subscribed:
        # Если пользователь подписан, одобряем заявку
        await callback.bot.approve_chat_join_request(config.main_channel_id, callback.from_user.id)

        await callback.message.edit_text(
            "Спасибо за подписку! Ваша заявка на вступление в канал одобрена."
        )

    else:
        await callback.answer(
            "Вы еще не подписались на все каналы!",
            show_alert=True
        )
