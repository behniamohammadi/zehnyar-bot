import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv(8480081257:AAHKzUDJ_HBHrKTHdMp2Kk0hJwJzwsh1vLo)

def start(update, context):
    update.message.reply_text("🌟 سلام! به ربات ذهن‌یار خوش اومدی. هر سوالی درباره خودشناسی و آگاهی داری بپرس.")

def help_command(update, context):
    update.message.reply_text("🔍 با دستورات /start یا /help شروع کن، یا مستقیم سوالتو بپرس.")

def echo(update, context):
    text = update.message.text
    update.message.reply_text(f"تو گفتی: {text}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler(None, echo))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
