import pyscreenshot
import pytesseract as pyt
import QuizFunctions as qf
import pyautogui
import pyperclip
import math
import time
from PIL import Image


pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def screenshotandReadQuestionNo():
  #Take screenshot of area
  questionNumberImage = pyscreenshot.grab(bbox=(0, 22, 260, 47))

  #Save and overwrite previous to specified file path
  questionNumberImage.save(r"C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png")

  #Necessary resizing and increase of DPI for pyTesseract to read
  image = Image.open(r'C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png')
  image = image.resize((520, 50))
  image.save(r'C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png', dpi=((600,600)))

  textFromImage1 = pyt.image_to_string(r'C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png')

  if 'Question n. 5' in textFromImage1:
    print("Found")
    return True

  if 'Question n. 11' in textFromImage1:
    print("Found")
    return True

  return False

def screenshotandReadDelPoints():
  #Take screenshot of area
  questionNumberImage = pyscreenshot.grab(bbox=(544, 569, 673, 643))

  #Save and overwrite previous to specified file path
  questionNumberImage.save(r"C:\Users\Administrator\Desktop\Quiz\Quiz\viewOfButton.png")

  #Necessary resizing and increase of DPI for pyTesseract to read
  #image = Image.open(r'C:\Users\Administrator\Desktop\Quiz\Quiz\viewOfButton.png')
  #image = image.resize((520, 50))
  #image.save(r'C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png', dpi=((600,600)))

  textFromImage2 = pyt.image_to_string(r'C:\Users\Administrator\Desktop\Quiz\Quiz\viewOfButton.png')

  if 'Delete' in textFromImage2:
    print("Detected delete in current textFromImage2 file")
    return True
  return False

def runModifierifQ5(buzzerNumber, multiplier):

      time.sleep(2)
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
  found = False
  while found == False:
    print("Searching for Question 5")
    found = screenshotandReadQuestionNo()
    time.sleep(10)
    
  buttonAppeared = False
  while buttonAppeared == False:
    print("Waiting for button to appear")
    time.sleep(2)
    buttonAppeared = screenshotandReadDelPoints()

  print("Button has appeared")
  runModifierifQ5(int(buzzerNumber), float(multiplier))