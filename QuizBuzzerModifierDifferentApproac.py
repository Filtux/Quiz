import re
import datetime
#Option 1
#Select particular buzzer number
#Apply score modifier right before scoreboards e.g. 0.9x/1.25x etc

#Test file, need to figure a way of automatically selecting the venue you're playing at
venueLogFile = r'C:\Users\Joe\Desktop\Log\TestLog.txt'
buzzerToChange = "5 " #Keep space
currentSessionLog = []
modifierAmount = 0.9

#Delete these comments when not testing
#currentStringDate = datetime.datetime.now()
#currentStringDate = currentStringDate.strftime("%d" + "/" + "%m" + "/" + "%Y")
currentStringDate = "10/07/2020"

#def findBuzzer(buzzerToChange):

#    contents = log.readlines()
#    something = re.finditer("Keypad:" + str(buzzerToChange), str(contents))

#def findCurrentQuiz():

#    contents = log.readlines()
#    something = re.search(currentStringDate, str(contents))
#    return something



def monitorCurrentSession():

    with open(venueLogFile) as log:

        listOfLines = log.readlines()
        foundEntryIndexList = [i for i, item in enumerate(listOfLines) if re.search(currentStringDate, item)] #grabs index of all appearances of today's date in log file

    log.close()

    #Makes new list of all entries of today's date from the log
    
    for currentSessionLines in foundEntryIndexList:
        currentSessionLog.append(listOfLines[currentSessionLines])

#Start
#keepSearching()
#keep checking log to see if it's question 5 yet
#while not any("Question 5" and "Keypad:" + str(buzzerToChange) in s for s in currentSessionLog):   
#    keepSearching()


monitorCurrentSession()

print("Keypad:" + str(buzzerToChange))

for i in currentSessionLog:
    #e.g. single digit
    if "Keypad:" + buzzerToChange in i:
        
        if re.search("Question Points:" + '.\w+', i) != None:

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




#newList = []
#for i in foundEntryIndex:
#    newList.append(i)
#print(newList)


 #   indexes = {v: index for index, v in enumerate(foundEntryIndex)}

 #   newList = [indexes.get(v+1, indexes[0]) for v in foundEntryIndex]

 #   findBuzzer(buzzerToChange)


























#Option 2
#Assign a ranking system to teams
#If they have played at least x games as a teamname (exclude generic team names), add them to a list
#List contains their name, average total score and ranks them against each other.
#Higher the ranking, the more they have to work for points e.g. score modifier 0.9x

#Option 3
