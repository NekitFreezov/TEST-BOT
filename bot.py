from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update


TOKEN = 'you_token'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Test Bot')

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
