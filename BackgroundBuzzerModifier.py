import pyscreenshot
import pytesseract as pyt
import QuizFunctions as qf
import pyautogui
import pyperclip
import math
import time

pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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

verify = 'n'

while verify == 'n':

  buzzerNumber = input("Enter the buzzer number to add modifier to: ")
  multiplier = input("Enter the multiplier as a decimal (x.x): ")
  print("You want to add a " + multiplier + " multiplier to buzzer " + buzzerNumber)
  verify = input("Is that correct? (y/n)")

if verify.lower() == 'y':
  print("Multiplier running in background...")
  while True:
    time.sleep(30)
    runModifierifQ5(buzzerNumber, multiplier)