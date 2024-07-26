import logging
from telegram import Update, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton

keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Отправить Спец🚀", callback_data="send_spec"),
        #InlineKeyboardButton("Хочу интеграцию", callback_data="get_integration"),
    ],
])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Callback - start - init")
    msg = """
    Привет! Это бот канала Спецы. Сюда вы можете отправить свои примеры спецпроектов. 
    
Если кейс мне понравится, я опубликую его в канале https://t.me/interactivespec
    """
    sent_message = await update.effective_message.reply_photo(
        photo=open('static/start_logo.jpeg', 'rb'),
        caption=msg,
        reply_markup=keyboard,
    )
    print("start", sent_message)
