import pytesseract as pyt

pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

text = pyt.image_to_string(r'C:\PythonScripts\Quiz\CurrentQuestionNumber.png')

print(text)


