import re

file = r'C:\Users\Joe\Desktop\Log\Test Venue_Log - Copy.txt'

checkWords = ("Domanda","Corretta","Tasto","Secondi","P.ti Question","P.ti Totali")
repWords = ("Question","Correct","Pressed","Seconds","Question Points","Total")

originalFile = open(file, 'r')
originalData = originalFile.readlines()

newFile = open(r'C:\Users\Joe\Desktop\Log\TestLog.txt', 'w')

for line in originalData:

    for check, replace in zip(checkWords, repWords):
        line = line.replace(check, replace)

    newFile.write(line)

originalFile.close()
newFile.close()
