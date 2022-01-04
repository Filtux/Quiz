#import os
#import telebot
#import QuizFunctions as qf
#import pyscreenshot
#import ScreenShotQuestionNo as ss
#import QuizInitialTestLoad as tl
#import QuizBuzzerModifierCurrentFinal as qb
#import pyautogui
#import ScreenShotQuestionNo as ss
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

API_KEY = '5079172619:AAHCary8yVpgIOKcsxrJuQWv4h8ApxPhtww'

# Create the Updater and pass it your bot's token.
updater = Updater(API_KEY, workers=10, use_context=True)

# setWebhook
.set_webhook(url="https://warm-plateau-09315.herokuapp.com/", certificate=open('mycert.pem'))
# unset webhook
tb.remove_webhook()

# Get the dispatcher to register handlers
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", help))
dp.add_handler(CommandHandler("help", help))

updater.start_polling(timeout=30, clean=True)
updater.idle() 

dp = updater.dispatcher

def test(update, context):
  update.message.reply_text("Testing, 1 2 3")

dp.add_handler(CommandHandler("test", test))

updater.start_polling