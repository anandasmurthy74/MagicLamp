from PIL import ImageFile

fp = open("Test1.pdf", "rb")

p = ImageFile.Parser()

while 1:
    s = fp.read(1024)
    if not s:
        break
    else:
        p.feed(s)
im = p.close()
im.save("00985413-1_img.jpg")
