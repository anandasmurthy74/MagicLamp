from PIL import Image
import io
class ImageConvert:
    def convert(self, imgf, labelf, outf, n):
        f = open(imgf, "rb")
        o = open(outf, "w")
        l = open(labelf, "rb")

        f.read(16)
        l.read(8)
        images = []

        for i in range(n):
            image = [ord(l.read(1))]
            for j in range(28*28):
                image.append(ord(f.read(1)))
            images.append(image)

        for image in images:
            o.write(",".join(str(pix) for pix in image)+"\n")
        f.close()
        o.close()
        l.close()
    
    def imgtobytes(self, imgf, outf):
        f = Image.open(imgf)
        of = open(outf,"wb")
        imgList = list(f.getdata())
        byteList =[]
        for val in range(len(imgList)):
            of.write((str(imgList[val]).encode()))
        
        of.write(('\n').encode())
        f.close()
        of.close()

aImgConvert = ImageConvert()
#aImgConvert.imgtobytes("hw_digitread_2.jpg", "hw_digit-2-ubytes")
aImgConvert.convert("hw_digit-2-ubytes", "hw_digitread_label_2",
       "hw_digit-2.csv", 1)
