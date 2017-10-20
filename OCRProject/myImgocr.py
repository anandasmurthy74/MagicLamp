from PIL import Image
import pytesseract


ocr_read = pytesseract.image_to_string(Image.open("2017-09-21-brd.png"))

print(ocr_read)
