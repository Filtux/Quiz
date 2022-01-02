import pytesseract as pyt

pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print(pyt.image_to_string(r'C:\Users\Joe\Desktop\ScreenCapture.png'))

