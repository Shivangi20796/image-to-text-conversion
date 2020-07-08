import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Users\Jatin Gambhir\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image
img = Image.open('1.png')
text = tess.image_to_string(img)
print(text)