import pyscreenshot
import pytesseract as pyt
import QuizFunctions as qf
import pyautogui
import pyperclip

pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

textFromImage = pyt.image_to_string(r'C:\PythonScripts\Quiz\CurrentQuestionNumber.png')

multiplier = 0.9

def runModifierifQ1():

    if 'Question n. 1' in textFromImage:

        qf.openBuzzerManager()
        qf.openBuzzer(1)
        pyautogui.press('enter') #skips the teamname screen
        pyperclip.copy()
        modifiedValue = int(pyperclip.paste()) * multiplier
        pyautogui.typewrite(modifiedValue)

        
  #      teamScoreImage = pyscreenshot.grab(bbox=(440, 198, 650, 250))
#
 #       teamScoreImage.save(r"C:\PythonScripts\Quiz\CurrentTeamScore.png")
#
 #       #Read screenshot
  #      textFromTeamScore = pyt.image_to_string(r'C:\PythonScripts\Quiz\CurrentTeamScore.png')
#
 #       teamScore = int(textFromTeamScore)
  #      newTeamScore = teamScore * modifier
#
 ##      pyautogui.moveTo(975, 565) #Okay Button
   #     pyautogui.leftClick()
    #    qf.exitBuzzerManager()
     #   qf.returnToGo()



