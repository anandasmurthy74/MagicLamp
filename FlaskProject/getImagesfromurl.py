from pymongo import MongoClient
import urllib.request
import os


class getImg:
    number = 0
    dbName = "magiclamp"
    client = MongoClient('mongodb://dbuser:Vin75!yaka@ds151153.mlab.com:51153/magiclamp')
    basedir = 'c:\pyProjects\FlaskProject\Projects'

    def __init__(self, prjid):
        os.makedirs(getImg.basedir + '\\' + str(prjid) + '\images')

    def getwebimage(self, prjid):
        db = getImg.client[getImg.dbName]
        images = db.Project.find_one({'projId': prjid}, {'images': 1})
        img_list = images['images']
        print(len(img_list))
        if img_list:
            for x in range(0, len(img_list)):
                img_url = img_list[x]
                filename = getImg.basedir + str(prjid) + '\images' + '\img-' + str(getImg.number) + '.jpg'
                img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Chennai_Montage.jpg/250px-Chennai_Montage.jpg'
                res = urllib.request.urlretrieve(img_url, filename)
                print(res)
                getImg.number += 1
        else:
            return -1
        return getImg.number


new = getImg(4)
print(new.getwebimage(4))
