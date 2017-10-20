from pymongo import MongoClient
from datetime import datetime 


class searchSorter:
    dbName="MagicLamp"
    collection="ProjectDetails"
    client=MongoClient()    
    def __init(self, projectId):
        self.projectId=projectId
    def storeTitle(self, title):
        self.title=title
    def storeDefinition(self, list):
        self.definition = list
    def storeImglinks(self,list):
        self.imgLinks=list
    
    