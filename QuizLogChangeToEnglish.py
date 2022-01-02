import re
import os

directory = r"C:\Users\Joe\Desktop\Log"

for fileName in os.listdir(directory):
    
    file = r'C:\\Users\\Joe\\Desktop\\Log\\' + fileName

    print(file)

    checkWords = ("Domanda","Corretta","Tasto","Nome","Secondi","P.ti Question","P.ti Totali")
    repWords = ("Question","Correct","Pressed","Name","Seconds","Question Points","Total")

    originalFile = open(file, 'r')
    originalData = originalFile.readlines()

    newFile = open(r'C:\\Users\\Joe\\Desktop\\Log\\' + fileName, 'w')

    for line in originalData:

        for check, replace in zip(checkWords, repWords):
            line = line.replace(check, replace)

        newFile.write(line)

    originalFile.close()
    newFile.close()
