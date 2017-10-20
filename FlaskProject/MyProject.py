from pymongo import MongoClient
from datetime import datetime


class Project:
    dbName = "MagicLamp"
    collection = "ProjectMaster"
    client = MongoClient("mongodb://dbuser:Vin75!yaka@mycluster0-shard-00-00-wpeiv.mongodb.net:27017,mycluster0-shard-00-01-wpeiv.mongodb.net:27017,mycluster0-shard-00-02-wpeiv.mongodb.net:27017/admin?ssl=true&replicaSet=Mycluster0-shard-0&authSource=admin")

    def __init__(self):
        pass

    def newProj(self, name, grade, projName):
        docid = 0
        self.name = name
        self.grade = grade
        self.projName = projName

        # get a connection to MagicLamp db
        db = Project.client[Project.dbName]
        coll = db[Project.collection]
        # get last seq number
        crseq = db['seq'].find_one()
        seqid = crseq['seqid']
        incid = seqid + 1

        # Dict of Project, name, grade
        projdate = datetime.utcnow()
        projdoc = {"prjname": projName, "Name": name, "Grade": grade, "createdDate": projdate, 'projid': incid}

        # Create a new entry in Projects collection
        crsr = coll.find({"prjname": projName})

        if crsr.count() == 0:
            docid = coll.insert_one(projdoc).inserted_id
            db['seq'].update_one({'seqid': seqid}, {"$set": {'seqid': incid}}, upsert=False)
        else:
            print("Project already exists")

        crsr.close()
        Project.client.close()

        return docid

    def getProj(self, userid):
        projmstr = []

        # get a connection to MagicLamp db
        db = Project.client[Project.dbName]
        coll = db[Project.collection]

        cursor = coll.find({"userid": userid})

        for doc in cursor:
            projmstr.append(doc)

        # housekeeping
        cursor.close()
        Project.client.close()

        return projmstr
