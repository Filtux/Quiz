from cmath import e
import re
import datetime
from tkinter import E
import regex

#Test file, need to figure a way of automatically selecting the venue you're playing at
venueLogFile = r'C:\Users\Joe\Desktop\Log\Test Venue_Log.txt'
outputFile = r'C:\Users\Joe\Desktop\Log\CurrentSessionOutput.txt'

buzzerToChange = "5 " #Keep space
currentSessionLog = []
modifierAmount = 0.9

#Delete these comments when not testing
currentStringDate = datetime.datetime.now()
currentStringDate = currentStringDate.strftime("%d" + "/" + "%m" + "/" + "%Y")
#currentStringDate = "10/07/2020"
#currentStringDate = "24/11/2021"

#Creates temporary logfile of all entries matching current date
def createCurrentSessionLog():

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

    return currentSessionLog
        
createCurrentSessionLog()

#Prints and returns a list of teamnames from currentSessionLog
def returnTeamNames(currentSessionLog):
    
    teamNameList = []

    for i in currentSessionLog:

        teamName = regex.search(r'(?<=Name:)[^|]+(?<!\s)', i)
        teamName = teamName.group()

        if teamName not in teamNameList:
            teamNameList.append(teamName)

    print(teamNameList)
    return teamNameList

teamNameList = returnTeamNames(createCurrentSessionLog())

with open(outputFile, 'w') as log:

    for name in teamNameList:

        log.write(name + '\n')
        print(name)

        #search for last entry of that teamname from currentSession Log in each round

        for i in currentSessionLog:

            if regex.search('ROUND 1', i) != None:

                if regex.search(name, i) != None:
                    lastEntry = regex.search(name, i)
                    lastR1Entry = i
        try:
            log.write(lastR1Entry + '\n')
        except:
            Exception

        for i in currentSessionLog:

            if regex.search('ROUND 2', i) != None:

                if regex.search(name, i) != None:
                    lastEntry = regex.search(name, i)
                    lastR2Entry = i
        try:
            log.write(lastR2Entry + '\n')
        except:
            Exception

        for i in currentSessionLog:

            if regex.search('ROUND 3', i) != None:

                if regex.search(name, i) != None:
                    lastEntry = regex.search(name, i)
                    lastR3Entry = i
        try:
            log.write(lastR3Entry + '\n')
        except:
            Exception

        for i in currentSessionLog:

            if regex.search('ROUND 4', i) != None:

                if regex.search(name, i) != None:
                    lastEntry = regex.search(name, i)
                    lastR4Entry = i
        try:
            log.write(lastR4Entry + '\n')
        except:
            Exception



#        print(lastR1Entry)
#        print(lastR2Entry)
#        print(lastR3Entry)
#        print(lastR4Entry)

    





    




    #regex for final score and append to round 1 list

    #Repeat for round n + 1














'''
for i in currentSessionLog:
    
#    name = regex.search(r'(?r)(?<=Name:)[^|]+(?<!\s)', i)
#    name = name.group()  

#    print(name)      

    found = re.search("Question Points:" + '.\w+', i)

    exactMatch = (found.group())
    exactMatchSliced = int(exactMatch[16:]) #Removes Question Points:

    if exactMatchSliced > 0: #If positive integer
        print(exactMatchSliced)
        exactMatchSlicedModified = int(exactMatchSliced * modifierAmount)
        print(exactMatchSlicedModified)

        #substitute and replace string exact match with exact match sliced at value part
        
        replacedMatch = re.sub(str(exactMatchSliced), str(exactMatchSlicedModified), i)
        print(replacedMatch)

        #Update the actual log file
    else:
        print("it's negative")


        
        
        #printre.search(r'Question Points:\b.+\|g', i)

    #Change value of score (question points for now)
    #    print(i + "END")

#print("Buzzer number not found in list")






'''

