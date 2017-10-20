from pymongo import MongoClient
from datetime import datetime


class ProjMaster:
    dbName = "MagicLamp"
    client = MongoClient("mongodb://dbuser:Vin75!yaka@ds151153.mlab.com:51153/magiclamp")

    def __init__(self):
        super(self)
        pass

    def addProj(self, username, prjGrade, projName, desc, tags):
        docid = 0
        self.uname = username
        self.prjGrade = prjGrade
        self.projName = projName
        self.desc = desc
        self.tags = tags

        # get a connection to MagicLamp db
        db = CreateProject.client[CreateProject.dbName]
        coll = db['Profile']
        # get last seq number
        crseq = db['seq'].find_one()
        seqid = crseq['seqid']
        incid = seqid + 1

        # Dict of Project, name, grade
        projdate = datetime.utcnow()
        projdoc = {"prjname": projName, "prjGrade": prjGrade, "createdDate": projdate, "desc": desc, "tags": tags, "projid": incid}

        # Create a new entry in Projects collection
        crsr = coll.find_one({"username": username})

        if crsr.count() == 1:
            docid = coll.update({"username": username}, {"$set": {'projects': projdoc}}, upsert=True)
            db['seq'].update_one({'seqid': seqid}, {"$set": {'seqid': incid}}, upsert=False)
        else:
            print("User not found")

        crsr.close()
        CreateProject.client.close()

        return docid
