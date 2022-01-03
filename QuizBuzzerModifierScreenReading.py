import re
import datetime
import pytesseract as pyt
#Option 1
#Select particular buzzer number
#Apply score modifier right before scoreboards e.g. 0.9x/1.25x etc

pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

text = pyt.image_to_string(r'C:\PythonScripts\Quiz\CurrentQuestionNumber.png')

print(text)





#Test file, need to figure a way of automatically selecting the venue you're playing at
#venueLogFile = r'C:\Users\Joe\Desktop\Log\Test Venue_Log.txt'
venueLogFile = r'C:\Program Files (x86)\QuizzaMePRO\Log\Test Venue_Log.txt'
buzzerToChange = "2 " #Keep space
currentSessionLog = []
modifierAmount = 0.9

#Delete these comments when not testing
#currentStringDate = datetime.datetime.now()
#currentStringDate = currentStringDate.strftime("%d" + "/" + "%m" + "/" + "%Y")
#currentStringDate = "10/07/2020"
currentStringDate = '1/12/2021'

currentStringTime = datetime.datetime.now()
currentStringTime = currentStringTime.strftime("%I:%M")
print(currentStringTime)

#def findBuzzer(buzzerToChange):

#    contents = log.readlines()
#    something = re.finditer("Keypad:" + str(buzzerToChange), str(contents))

#def findCurrentQuiz():

#    contents = log.readlines()
#    something = re.search(currentStringDate, str(contents))
#    return something

def periodicSessionGrab():

    with open(venueLogFile) as log:

        listOfLines = log.readlines()
        foundEntryIndexList = [i for i, item in enumerate(listOfLines) if re.search(currentStringDate, item)] #grabs index of all appearances of today's date in log file

    log.close()

    #Makes new list of all entries of today's date from the log - Also saves them into txt file
    
    for currentSessionLines in foundEntryIndexList:

        currentSessionLog.append(listOfLines[currentSessionLines])

    with open("CurrentSessionLog.txt", 'w') as file:
        for line in currentSessionLog:
            file.write(line)

def scan():

    with open("CurrentSessionLog.txt", 'r') as currentSessionLog:

        for eachEntry in currentSessionLog:

            if re.search("Question 5", eachEntry) != None:
            
                if "Keypad:" + buzzerToChange in eachEntry:
                    if re.search("Total:" + '.\w+', eachEntry) != None:
                    
                        found = re.search("Total:" + '.\w+', eachEntry)
                        
                        exactMatch = (found.group())
                        exactMatchSliced = int(exactMatch[6:]) #Extracts Total Points

                        if exactMatchSliced > 0: #If positive integer
                            
                            exactMatchSlicedModified = int(exactMatchSliced * modifierAmount)

                            return exactMatchSlicedModified
                            

                            #substitute and replace string exact match with exact match sliced at value part
                            
                    #       replacedMatch = re.sub(str(exactMatchSliced), str(exactMatchSlicedModified), eachEntry)
                    #       print(replacedMatch)

                            #Update the actual log file
                    #   else:
                    #       print("it's negative")


            
            
            #printre.search(r'Question Points:\b.+\|g', i)

        #Change value of score (question points for now)
        #    print(i + "END")

    #print("Buzzer number not found in list")
        
periodicSessionGrab()

print("Keypad:" + str(buzzerToChange))

scan()

teamScore = scan()

print(teamScore)





























#Option 2
#Assign a ranking system to teams
#If they have played at least x games as a teamname (exclude generic team names), add them to a list
#List contains their name, average total score and ranks them against each other.
#Higher the ranking, the more they have to work for points e.g. score modifier 0.9x

#Option 3
