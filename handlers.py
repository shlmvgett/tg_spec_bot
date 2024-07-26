import logging
from typing import Union, List
from telegram import Update, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton
from telegram.ext import InlineQueryHandler, CallbackQueryHandler
from callbacks import start, send_content

# start_handler = CommandHandler("start", start.init)


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start.start(update, context)


async def send_content_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_content.send_content(update, context)

async def integration_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_content.integration(update, context)

async def resend_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_content.resend_handler(update, context)







async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="pong")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.photo)
    # await context.bot.send_document(chat_id=update.effective_chat.id, document=update.message.photo[0].file_id)
    await context.bot.send_photo(chat_id=-4142687212, photo=update.message.photo[0].file_id)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)
    print(update)


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Sends a message with three inline buttons attached."""
#     keyboard = [
#         [
#             InlineKeyboardButton("Option 1", callback_data="1"),
#             InlineKeyboardButton("Option 2", callback_data="2"),
#         ],
#         [InlineKeyboardButton("Option 3", callback_data="3")],
#     ]
#
#     reply_markup = InlineKeyboardMarkup(keyboard)
#
#     await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
