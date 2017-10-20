from pymongo import MongoClient
from datetime import datetime
import bs4 as bs
import urllib.request
import pandas as pd


class CreateProj:
    dbName = "magiclamp"
    client = MongoClient("mongodb://dbuser:Vin75!yaka@ds151153.mlab.com:51153/magiclamp")

    def __init__(self):
        super()

    # Add a new project to a existing user
    def addProj(self, username, prjGrade, projName, desc, tags):
        self.username = username
        self.prjGrade = prjGrade
        self.projName = projName
        self.desc = desc
        self.tags = tags

        # get a connection to MagicLamp db
        db = CreateProj.client[CreateProj.dbName]
        coll = db['Profile']
        # get last seq number
        crseq = db['seq'].find_one()
        seqid = crseq['seqid']
        incid = seqid + 1

        # Dict of Project, name, grade
        projdate = datetime.utcnow()
        projdoc = {"prjname": self.projName, "prjGrade": self.prjGrade, "createdDate": projdate, "desc": self.desc, "tags": self.tags, "projid": incid}

        # Create a new entry in Projects collection
        crsr = coll.find_one({"username": self.username})
        crsr["Projects"].append(projdoc)

        if crsr:
            coll.update({"username": username}, {"$set": {'Projects': crsr["Projects"]}}, upsert=True)
            db['seq'].update_one({'seqid': seqid}, {"$set": {'seqid': incid}}, upsert=False)
        else:
            print("User not found")

        CreateProj.client.close()
        return incid

    # Add project details by searching on topic
    def projDetails(self, topic, projId):
        self.topic = topic
        self.projId = projId

        docid = 0
        db = CreateProj.client[CreateProj.dbName]
        coll = db['Project']

        pKeys = ['projId', 'toc', 'images', 'ref']
        pVals = [projId]

        url = 'https://en.wikipedia.org/wiki/' + topic
        print(url)
        sauce = urllib.request.urlopen(url).read()
        df_list = pd.read_html(url)
        soup = bs.BeautifulSoup(sauce, "lxml")
        contents = soup.find_all('span', class_='toctext')
        first = soup.find_all('p')
        images = soup.find_all('a', class_="image")
        headlines = soup.find_all('span', class_="mw-headline")

        # Introduction - the first 3 paragraphs
        intro = {'introduction': None}
        s = ""
        for x in range(0, 2):
            s = s + first[x].text

        intro['introduction'] = s

        # Get the topics and the associated paragraphs
        headings = []
        paragraphs = []
        for x in range(0, len(headlines)):
            for elt in headlines[x].parent.nextSiblingGenerator():
                if elt.name == 'h2':
                    break
                if elt.name == 'p':
                    headings.append(headlines[x].text)
                    paragraphs.append(elt.text)

        keytopics = dict(zip(headings, paragraphs))
        pVals.append(keytopics)

        # Get the list of images and their link
        baseurl = "https://en.wikipedia.org"
        img = []
        for image in images:
            imgurl = baseurl + image.get('href')
            img.append(imgurl)

        pVals.append(img)

        # Get the contents and their links
        toclist = []
        for toc in contents:
            toclist.append(toc.text)
        pop_list = ["See also", "References", "Bibliography", "External links", "Primary sources", "Notes", "Notes and references", "Further reading"]

        for x in range(0, len(pop_list)):
            if pop_list[x] in toclist:
                toclist.remove(pop_list[x])

        # Get all the references
        ref = []
        references = soup.find_all('span', class_="reference-text")

        for reference in references:
            ref.append(reference.text)

        pVals.append(ref)

        pDoc = dict(zip(pKeys, pVals))
        pDoc.update(intro)
        for df in df_list:
            pDoc.update({'tables': df.to_json()})

        docid = coll.insert(pDoc)

        return docid
