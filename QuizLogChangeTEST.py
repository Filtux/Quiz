import re

file = r'C:\PythonScripts\Quiz\Test Venue_Log.txt'

checkWords = ("Domanda","Corretta","Tasto","Nome","Secondi","P.ti Question","P.ti Totali")
repWords = ("Question","Correct","Pressed","Name","Seconds","Question Points","Total")

originalFile = open(file, 'r')
originalData = originalFile.readlines()

newFile = open(r'C:\Users\Joe\Desktop\Log\TestLog.txt', 'w')

for line in originalData:

    for check, replace in zip(checkWords, repWords):
        line = str(line).replace(check, replace)
        
    newFile.write(line)

originalFile.close()
newFile.close()



