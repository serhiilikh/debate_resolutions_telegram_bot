import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.dispatcher import run_async
from config import token, resolutions, url
from random import randint


@run_async
def start(bot, update):
    update.message.reply_text("Привет! У меня есть темы для дебатов. Пиши номер резолюции или испытай /random")


@run_async
def get_resolution_by_random(bot, update):
    x = randint(0, len(resolutions)-1)
    update.message.reply_text(resolutions[x])


@run_async
def get_resolution_by_number(bot, update):
    message_text = update.message.text.replace(",", ".")
    if update.message.text.isdigit:
        result_string = resolutions[round(int(message_text)) % len(resolutions) - 1]
        update.message.reply_text(result_string)


def main():
    port = int(os.environ.get('PORT', '8443'))
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("random", get_resolution_by_random))
    dp.add_handler(MessageHandler(Filters.text, get_resolution_by_number))

    updater.start_webhook(listen="0.0.0.0",
                          port=port,
                          url_path=token)
    updater.bot.set_webhook(url + token)
    updater.idle()


if __name__ == "__main__":
    main()
