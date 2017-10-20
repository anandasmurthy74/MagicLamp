from pymongo import MongoClient
from datetime import datetime


class Project:
    dbName = "MagicLamp"
    collection = "ProjectMaster"
    client = MongoClient()

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

    def getProj(self, projid):
        projmstr = {'retcode': -2}

        # get a connection to MagicLamp db
        db = Project.client[Project.dbName]
        coll = db[Project.collection]

        cursor = coll.find_one({"projid": projid})
        projmstr = cursor

        # housekeeping
        cursor.close()
        Project.Client.close()

        return projmstr
