import pyautogui
import PySimpleGUI
import time

pyautogui.PAUSE = 0.5
# Keypad manager's buzzer number coordinates
listofCoordinates = [(0,0) for x in range(0, 15)] 
listofCoordinates[0] = (450, 420)
listofCoordinates[1] = (450, 440)
listofCoordinates[2] = (450, 460)
listofCoordinates[3] = (450, 480)
listofCoordinates[4] = (450, 500)
listofCoordinates[5] = (450, 520)
listofCoordinates[6] = (450, 540)
listofCoordinates[7] = (450, 560)
listofCoordinates[8] = (450, 580)
listofCoordinates[9] = (450, 600)
listofCoordinates[10] = (450, 620)
listofCoordinates[11] = (450, 640)
listofCoordinates[12] = (450, 660)
listofCoordinates[13] = (450, 680)
listofCoordinates[14] = (450, 700)

def printBuzzerCoordinates(buzzerNumber):

    buzzerCoordinates = listofCoordinates[buzzerNumber - 1]
    print ("Buzzer " + (str(buzzerNumber)) + " is at " + (str(buzzerCoordinates)))
    return buzzerCoordinates

def returnBuzzerCoordinates(buzzerNumber):

    buzzerCoordinates = listofCoordinates[buzzerNumber - 1]
    return buzzerCoordinates

def openBuzzer(buzzerNumber):

    buzzerNumber = returnBuzzerCoordinates(buzzerNumber)
    pyautogui.moveTo(buzzerNumber)
    pyautogui.doubleClick()
    return

def openBuzzerManager():
    pyautogui.moveTo(951, 181)
    pyautogui.leftClick()
    return

def clickSound():
    pyautogui.moveTo (1156, 73)
    pyautogui.leftClick()
    return

def clickRealTimeScores():
    pyautogui.moveTo(548, 67)
    pyautogui.leftClick()
    return

def clickCurrentTotal():
    pyautogui.moveTo(682, 68)
    pyautogui.leftClick()
    return

def increase500Points():
    pyautogui.moveTo(1034, 208)
    pyautogui.leftClick()
    pyautogui.moveTo(975, 565) #Okay Button
    pyautogui.leftClick()
    return

def decrease500Points():
    pyautogui.moveTo(1034, 237)
    pyautogui.leftClick()
    return

def saveMemoryOne():
    pyautogui.moveTo(340, 326)
    pyautogui.click()
    pyautogui.moveTo(707, 442)
    pyautogui.click()

def exitBuzzerManager():
    pyautogui.moveTo(1037, 329)
    pyautogui.leftClick()
    pyautogui.moveTo(774, 442)
    pyautogui.leftClick()
    return

def returnToGo():
    pyautogui.moveTo (967, 609)
    return

def giveTeamPoints(buzzerNumber):
    openBuzzerManager()
    openBuzzer(buzzerNumber)
    pyautogui.press('enter') #skips the teamname screen
    increase500Points()
    saveMemoryOne()
    exitBuzzerManager()
    returnToGo() #Will not click after

def removeTeamPoints(buzzerNumber):
    openBuzzerManager()
    openBuzzer(buzzerNumber)
    pyautogui.press('enter') #skips the teamname screen
    decrease500Points()
    exitBuzzerManager()
    returnToGo() #Will not click after

def makeSecondFirst():
    clickCurrentTotal()
    pyautogui.moveTo(637, 138)
    pyautogui.doubleClick()
    clickRealTimeScores()
    returnToGo()
    
def fastestFinger():
    pyautogui.moveTo(950, 75)
    pyautogui.doubleClick(interval = 4)