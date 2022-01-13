import pyscreenshot
import pytesseract as pyt
import QuizFunctions as qf
import pyautogui
import pyperclip
import math
import time

pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Every 1 minute, take a screenshot - set toggle for on/off
run = False

def runProgram():
  run = True
  return run

def runModifierifQ5(buzzerNumber, multiplier):

  #Take screenshot of area
  teamScoreImage = pyscreenshot.grab(bbox=(0, 20, 260, 45))

  #Save and overwrite previous to specified file path
  teamScoreImage.save(r"C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png")

  #Read image and save found text to string
  textFromImage = pyt.image_to_string(r'C:\PythonScripts\Quiz\CurrentQuestionNumber.png')
  #textFromImage = pyt.image_to_string(r'C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png')

  if 'Question n. 5' in textFromImage:

      qf.openBuzzerManager()
      qf.openBuzzer(buzzerNumber)
      pyautogui.press('enter') #skips the teamname screen
      pyautogui.hotkey('ctrl', 'c')
      modifiedValue = int(pyperclip.paste()) * multiplier
      print(modifiedValue)
      pyautogui.typewrite(str(math.floor(modifiedValue)))

while run == True:
  #Every 30 seconds, run function
  #time.sleep(30)
  print("running")
  runModifierifQ5()


