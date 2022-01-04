import os
import telebot
import QuizFunctions as qf
import pyscreenshot
import ScreenShotQuestionNo as ss
import QuizInitialTestLoad as tl
import QuizBuzzerModifierCurrentFinal as qb
import pyautogui
import ScreenShotQuestionNo as ss
from flask import Flask, request

TOKEN = '5079172619:AAHCary8yVpgIOKcsxrJuQWv4h8ApxPhtww'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://warm-plateau-09315.herokuapp.com' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

@bot.message_handler('Greet')
def greet(message):
  bot.reply_to(message, "Hey! How's it going?")
  os.system("start cmd")

@bot.message_handler(['test'])
def test(test):
    bot.reply_to(test, "Test")

#Add default 500 points, just for memory one right now

@bot.message_handler(["add1"])
def add1(message):
    qf.giveTeamPoints(1)

@bot.message_handler(["add2"])
def add2(message):
  qf.giveTeamPoints(2)

@bot.message_handler(["add3"])
def add3(message):
    qf.giveTeamPoints(3)

@bot.message_handler(["add4"])
def add4(message):
  qf.giveTeamPoints(4)

@bot.message_handler(["add5"])
def add5(message):
    qf.giveTeamPoints(5)

@bot.message_handler(["add6"])
def add6(message):
  qf.giveTeamPoints(6)

@bot.message_handler(["add7"])
def add7(message):
    qf.giveTeamPoints(7)

@bot.message_handler(["add8"])
def add8(message):
  qf.giveTeamPoints(8)

@bot.message_handler(["add9"])
def add9(message):
    qf.giveTeamPoints(9)

@bot.message_handler(["add10"])
def add10(message):
  qf.giveTeamPoints(10)

@bot.message_handler(["add11"])
def add11(message):
    qf.giveTeamPoints(11)

@bot.message_handler(["add12"])
def add12(message):
  qf.giveTeamPoints(12)

@bot.message_handler(["add13"])
def add13(message):
    qf.giveTeamPoints(13)

@bot.message_handler(["add14"])
def add14(message):
  qf.giveTeamPoints(14)

@bot.message_handler(["add15"])
def add15(message):
    qf.giveTeamPoints(15)

#Remove default 500 points, just for memory one right now

@bot.message_handler(["rem1"])
def rem1(message):
    qf.giveTeamPoints(1)

@bot.message_handler(["rem2"])
def add3(message):
  qf.giveTeamPoints(2)

@bot.message_handler(["rem3"])
def rem3(message):
    qf.giveTeamPoints(3)

@bot.message_handler(["rem4"])
def rem4(message):
  qf.giveTeamPoints(4)

@bot.message_handler(["rem5"])
def rem5(message):
    qf.giveTeamPoints(5)

@bot.message_handler(["rem6"])
def rem6(message):
  qf.giveTeamPoints(6)

@bot.message_handler(["rem7"])
def rem7(message):
    qf.giveTeamPoints(7)

@bot.message_handler(["rem8"])
def rem8(message):
  qf.giveTeamPoints(8)

@bot.message_handler(["rem9"])
def rem9(message):
    qf.giveTeamPoints(9)

@bot.message_handler(["rem10"])
def rem10(message):
  qf.giveTeamPoints(10)

@bot.message_handler(["rem11"])
def rem11(message):
    qf.giveTeamPoints(11)

@bot.message_handler(["rem12"])
def rem12(message):
  qf.giveTeamPoints(12)

@bot.message_handler(["rem13"])
def rem13(message):
    qf.giveTeamPoints(13)

@bot.message_handler(["rem14"])
def rem14(message):
  qf.giveTeamPoints(14)

@bot.message_handler(["rem15"])
def rem15(message):
    qf.giveTeamPoints(15)

@bot.message_handler(['msf'])
def makeSecondFirst(message):
  bot.reply_to(message, "msf")
  qf.makeSecondFirst()

@bot.message_handler(["screenshot"])
def screenshot(message):
  image = pyscreenshot.grab(bbox=(483, 107, 879, 561)) #set to quiz box parameters
  image.save("liveTeamPosition.png") #save it in a folder and +date to filename or something
  #image = open('liveTeamPosition.png', 'rb')
  bot.send_photo(message.chat.id, image)

"""@bot.message_handler(['t'])
def buzzerModifier(message):
  qb.periodicSessionGrab()
  grabbedPointsFromLog = qb.scan()
  qf.openBuzzerManager()
  qf.openBuzzer(1)
  pyautogui.press('enter') #skips the teamname screen
  pyautogui.typewrite(str(grabbedPointsFromLog))
  pyautogui.moveTo(975, 565) #Okay Button
  pyautogui.leftClick()
  qf.saveMemoryOne()
  qf.exitBuzzerManager()
  qf.returnToGo()"""

@bot.message_handler(["modTEST"])
def modifyTEST(message):
  teamScoreImage = pyscreenshot.grab(bbox=(0, 20, 260, 45))
  teamScoreImage.save(r"C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png")
  bot.send_photo(message.chat.id, teamScoreImage)
  ss.runScreenShot()

@bot.message_handler(["mod"])
def modify(message):
  while ss.runModifierifQ5 != True:
    if ss.runModifierifQ5() == True:
      qf.saveMemoryOne()
      qf.exitBuzzerManager()
      qf.returnToGo()

@bot.message_handler(["loadGame"])
def loadGame(message):
  tl.performMovements()

@bot.message_handler(["ff"])
def fastestFinger(message):
  qf.fastestFinger()
  qf.returnToGo()



#bot.polling()