import pyscreenshot
import pytesseract as pyt
import QuizFunctions as qf
import pyautogui
import pyperclip
import math
import time
from PIL import Image

pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def runModifierifQ5(buzzerNumber, multiplier):

  #Take screenshot of area
  questionNumberImage = pyscreenshot.grab(bbox=(0, 22, 260, 47))

  #Save and overwrite previous to specified file path
  questionNumberImage.save(r"C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png")

  #Necessary resizing and increase of DPI for pyTesseract to read
  image = Image.open(r'C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png')
  image = image.resize((520, 50))
  image.save(r'C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png', dpi=((600,600)))

  #Read image and save found text to string
  #textFromImage = pyt.image_to_string(r'C:\PythonScripts\Quiz\CurrentQuestionNumber.png')
  textFromImage = pyt.image_to_string(r'C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png')

  if 'Question n. 1' in textFromImage:

      qf.openBuzzerManager()
      qf.openBuzzer(buzzerNumber)
      pyautogui.press('enter') #skips the teamname screen
      pyautogui.hotkey('ctrl', 'c')
      modifiedValue = int(pyperclip.paste()) * multiplier
      print(modifiedValue)
      pyautogui.typewrite(str(math.floor(modifiedValue)))
      pyautogui.moveTo(975, 565) #Okay Button
      pyautogui.leftClick()
      qf.roundCheckAndSave()
      qf.exitBuzzerManager()
      qf.returnToGo() #Will not click after

verify = 'n'

while verify == 'n':

  print('verify is currently equalling n')
  buzzerNumber = input("Enter the buzzer number to add modifier to: ")
  multiplier = input("Enter the multiplier as a decimal (x.x): ")
  print("You want to add a " + multiplier + " multiplier to buzzer " + buzzerNumber)
  verify = input("Is that correct? (y/n)")

if verify.lower() == 'y':
  print("Multiplier running in background...")
  while True:
    print("In True Loop")
    time.sleep(5)
    runModifierifQ5(int(buzzerNumber), float(multiplier))
    print("Reading: " + pyt.image_to_string(r'C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png'))
    time.sleep(10)