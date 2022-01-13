from tkinter import *
#import ScreenShotQuestionNo as SSQN
import pyscreenshot
import pytesseract as pyt
import QuizFunctions as qf
import pyautogui
import pyperclip
import math
import time
import TkinterGUISS

pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

multiplier = 0.9

def runModifierifQ5(buzzerNumber):

  #Take screenshot of area
  teamScoreImage = pyscreenshot.grab(bbox=(0, 20, 260, 45))

  #Save and overwrite previous to specified file path
  #teamScoreImage.save(r"C:\Users\Administrator\Desktop\Quiz\Quiz\CurrentQuestionNumber.png")
  teamScoreImage.save(r"C:\PythonScripts\Quiz\CurrentQuestionNumber2.png")


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


main = Tk()
main.geometry('500x400')
main.resizable(0,0) #Boolean
#main.config(bg='#34ebb4')
main.title('Quizzame Extender')

Label(main,text = 'Quizzame Extender', font='Arial 15').pack()

buzzerNo = IntVar()
buzzerChoices = [1, 2, 3, 4, 5]
buzzerNo.set(1) #Default choice

Label(main,text = 'Select buzzer number', font='Arial 15').pack()
buzzerDropdown = OptionMenu(main, buzzerNo, *buzzerChoices).pack()

# Change the label text
def returnChoice():
    buzzerToChange = buzzerNo.get()
    print(buzzerToChange)
    return buzzerToChange

button = Button(main, text = "Confirm Buzzer Number", command= returnChoice).pack()
button2 = Button(main, text = "Run Program", command = runProgram()).pack()

  
main.mainloop()











'''

path = StringVar()
Label(main, text = 'Specify full path to download to:', font = 'Arial 15').place(x=130, y=60)
pathEnter = Entry(main, width = 70, textvariable= path).place(x=32, y=90)

link = StringVar()
Label(main, text = 'Paste YouTube link here:', font = 'Arial 15').place(x=134, y=120)
linkEnter = Entry(main, width = 70, textvariable= link).place(x=32, y=150)

def VideoDownloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download(output_path=str(path.get()))
    Label(main, text = 'Downloaded video', font = 'Arial 15').place(x=160, y=320)

def AudioDownloader():
    url = YouTube(str(link.get()))
    audio = url.streams.get_audio_only()
    audio.download(output_path=str(path.get()))
    Label(main, text = 'Downloaded audio', font = 'Arial 15').place(x=160, y=350)

Button(main, text = 'Download Video', font = 'Arial 15', bg= 'orange', command = VideoDownloader).place(x=160, y=210)
Button(main, text = 'Download Audio', font = 'Arial 15', bg= 'orange', command = AudioDownloader).place(x=162, y=280)

'''