from handlers import *
from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler
from dotenv import load_dotenv
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def init_data(app: Application):
    await app.bot.set_my_commands(
        [
            ("start", "Отправить Спец"),
            ("help", "На помощь"),
        ]
    )


if __name__ == '__main__':
    application = (ApplicationBuilder()
                   .token(TOKEN)
                   .post_init(init_data)
                   .build())

    # https://github.com/91DarioDev/forwardscoverbot/blob/master/forwardscoverbot/__main__.py

    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler('ping', ping))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(CallbackQueryHandler(send_content_handler, pattern="send_spec"))
    # application.add_handler(CallbackQueryHandler(integration_handler, pattern="get_integration"))
    application.add_handler(MessageHandler(None, callback=resend_handler))

    application.run_polling()
