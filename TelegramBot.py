import os
import telebot
import QuizFunctions as qf
import pyscreenshot
import ScreenShotQuestionNo as ss

API_KEY = '5079172619:AAHCary8yVpgIOKcsxrJuQWv4h8ApxPhtww'

bot = telebot.TeleBot(API_KEY)

@bot.message_handler('Greet')
def greet(message):
  bot.reply_to(message, "Hey! How's it going?")
  os.system("start cmd")

@bot.message_handler(['test'])
def test(test):
    bot.reply_to(test, "Test")

@bot.message_handler(["add1"])
def add1(message):
    bot.reply_to(message, "you said add1")
    qf.giveTeamPoints(1)

@bot.message_handler(['msf'])
def msf(message):
  bot.reply_to(message, "msf")
  qf.makeSecondFirst()

@bot.message_handler(["screenshot"])
def screenshot(message):
  image = pyscreenshot.grab(bbox=(0, 0, 1000, 1000)) #set to quiz box parameters
  image.save("liveTeamPosition.png") #save it in a folder and +date to filename or something
  image = open('liveTeamPosition.png', 'rb')
  bot.send_photo(message.chat.id, image)

@bot.message_handler(["mod"])
def modify(message):
  teamScoreImage = pyscreenshot.grab(bbox=(0, 20, 260, 45))
  teamScoreImage.save(r"C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png")
  bot.send_photo(message.chat.id, teamScoreImage)
  ss.runScreenShot()

bot.polling()