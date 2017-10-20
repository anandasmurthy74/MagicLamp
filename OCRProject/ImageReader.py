from PIL import Image
import numpy as np
import pytesseract


left, top, right, bottom = 325, 700, 385, 750
offset = 90
size = (8, 8)


img = Image.open("2017-09-21-brd.png")

left, top, right, bottom = 325, 700, 385, 750
offset = 90
size = (8, 8)
area = (left, top, right, bottom)

img_chbox1 = img.crop(area).resize(size)

area = (left, top + offset, right, bottom + offset)
img_chbox2 = img.crop(area).resize(size)

area = (left, (top + 2 * offset), right, (bottom + 2 * offset))
img_chbox3 = img.crop(area).resize(size)

chbx_1 = np.asarray(img_chbox1, dtype='uint8')
chbx_2 = np.asarray(img_chbox2, dtype='uint8')
chbx_3 = np.asarray(img_chbox3, dtype='uint8')

match = 0

if chbx_1.all() == chbx_2.all():
    match = 12
else:
    if chbx_2.all() == chbx_3.all():
        match = 23
    if chbx_1.all() == chbx_3.all():
        match = 13

if match == 12:
    area = (left + (offset - 30), (top + 2 * offset), (right + 3.5 * offset), (bottom + 2 * offset))
    img_bank = img.crop(area)
    area = (left + (9 * offset), (top + 2 * offset), (right + 14 * offset), (bottom + 2 * offset))
    img_branch = img.crop(area)
    txt = pytesseract.image_to_string(img_bank)
    print("Bank : ", txt)
    print("Handwritten branch name: ", pytesseract.image_to_string(img_branch))

area = ((left - offset), (top + 6.75 * offset), (right + 5.25 * offset), (bottom + 7.25 * offset))
client_bnk_act = img.crop(area)
cl_acnum_txt = pytesseract.image_to_string(client_bnk_act)
print(cl_acnum_txt)

area = ((left + 6.75 * offset), (top + 6.75 * offset), (right + 17 * offset), (bottom + 7.25 * offset))
client_bnk_act_num = img.crop(area)
cl_bnk_ac_txt = pytesseract.image_to_string(client_bnk_act_num)
print(cl_bnk_ac_txt)
