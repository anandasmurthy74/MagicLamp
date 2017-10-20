import matplotlib.pyplot as plt
from matplotlib import style
import io
import os
from PIL import Image

class DigiImg:
	def readImg(self, path):
		#style.use("fivethirtyeight")
		img = plt.imread(path) 
		
		plt.imshow(img,cmap=plt.get_cmap('gray'))
		plt.show()
newimg = DigiImg()
newimg.readImg("C:\PyProjects\OCRProject\myimg.jpg")
# img = Image.open("\Images\0\0-1.jpg")
