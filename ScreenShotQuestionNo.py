import pyscreenshot
import pytesseract as pyt
import QuizFunctions as qf
import pyautogui

def runScreenShot():

    modifier = 0.9

    #Path to tesseract
#    pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #Set to quiz box parameters
    image = pyscreenshot.grab(bbox=(0, 20, 260, 45)) 
  
    # To view the screenshot
    #image.show()
  
    # To save the screenshot
    image.save("C:\Users\Administrator\Desktop\Quiz\CurrentQuestionNumber.png")

    textFromImage = pyt.image_to_string(r'C:\PythonScripts\Quiz\CurrentQuestionNumber.png')

    if 'Question 5' in textFromImage:
        #Run the sequence to open a team, alter points with modifier
        #Testing with buzzer 1
        qf.openBuzzerManager()
        qf.openBuzzer(1)
        pyautogui.press('enter') #skips the teamname screen

        teamScoreImage = pyscreenshot.grab(bbox=(440, 198, 650, 250))

        teamScoreImage.save("C:\PythonScripts\Quiz\CurrentTeamScore.png")

        #Read screenshot
        textFromTeamScore = pyt.image_to_string(r'C:\PythonScripts\Quiz\CurrentTeamScore.png')

        teamScore = int(textFromTeamScore)
        newTeamScore = teamScore * modifier

        pyautogui.typewrite(newTeamScore)
        pyautogui.moveTo(975, 565) #Okay Button
        pyautogui.leftClick()
        qf.exitBuzzerManager()
        qf.returnToGo()



