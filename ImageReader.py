import pytesseract as pyt

pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

text = pyt.image_to_string(r'C:\PythonScripts\Quiz\test.png')

print(text)


