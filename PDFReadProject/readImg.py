from PIL import Image
import pytesseract

img = Image.open("myimg.jpg")

print(img)

text = pytesseract.image_to_string(img, lang='eng')

print(text)
