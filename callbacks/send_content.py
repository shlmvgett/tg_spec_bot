import logging
from typing import Union, List
from telegram import Update, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton
from telegram.ext import InlineQueryHandler, CallbackQueryHandler

async def send_content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Callback - send_content")
    message = """
    Чтобы увеличить шансы на публикацию пришлите:
    - Название компании;
    - Пару предложений с описанием проекта;
    - Ссылку (если есть).
    - Материалы (видео, скрины, фото).

Если что-то забудете, можете просто дослать отдельным сообщением
    """
    sent_message = await update.effective_message.reply_text(message)
    print("send_content:", sent_message)


async def integration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Callback - integration")
    sent_message = await update.effective_message.reply_text("Раздел в разработке 🚣‍♀️")
    print("integration:", sent_message)


async def resend_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Callback - integration")
    sent_message = await context.bot.forward_message(chat_id=-4142687212, from_chat_id=update.message.chat.id, message_id=update.message.message_id)
    await update.effective_message.reply_text("Спасибо, я получил ваш спец, если он мне понравится, я опубликую его в канале🔥")
    user = update.message.from_user
    user_info = f"""
    Сообщение от юзера: 
    id={user['id']}
    username=@{user['username']}
    first_name={user['first_name']}
    last_name={user['last_name']}
    """
    await context.bot.send_message(chat_id=-4142687212, text=user_info)
    print("resend_handler:", sent_message)
