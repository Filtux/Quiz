import pytesseract as pyt



pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

textFromImage1 = pyt.image_to_string(image=r'C:\Users\Administrator\Desktop\Quiz\Quiz\QuestionShot1\CurrentQuestionNumber1.png', config='psm=4')
textFromImage2 = pyt.image_to_string(r'C:\Users\Administrator\Desktop\Quiz\Quiz\QuestionShot1\CurrentQuestionNumber2.png', config='psm=7')
textFromImage3 = pyt.image_to_string(r'C:\Users\Administrator\Desktop\Quiz\Quiz\QuestionShot1\CurrentQuestionNumber3.png', config='psm=7')
textFromImage4 = pyt.image_to_string(r'C:\Users\Administrator\Desktop\Quiz\Quiz\QuestionShot1\CurrentQuestionNumber4.png', config='psm=7')
textFromImage5 = pyt.image_to_string(r'C:\Users\Administrator\Desktop\Quiz\Quiz\QuestionShot1\CurrentQuestionNumber5.png', config='psm=7')
#textFromImageSample = pyt.image_to_string(r'C:\Users\Administrator\Desktop\Quiz\Quiz\QuestionShot1\sample.png')



print('1' + textFromImage1)
print('2' + textFromImage2)
print('3' + textFromImage3)
print('4' + textFromImage4)
print('5' + textFromImage5)
#print(textFromImageSample)

