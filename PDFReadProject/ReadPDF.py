import PyPDF2


class Pdfread:
    def __init__(self):
        super()

    def readmyPDF(self, filename):
        doc = {}
        with open(filename, 'rb') as file:
            inputpdf = PyPDF2.PdfFileReader(file)
            d = inputpdf.getDocumentInfo()
            doc['pages'] = inputpdf.getNumPages()
            doc['title'] = d.title

            doc['fields'] = inputpdf.getFields()

            pages = list(inputpdf.pages)

            for page in pages:
                doc['doctext'] = page.extractText()
                doc['contents'] = page.getContents()

        return doc


rdf = Pdfread()
doc = rdf.readmyPDF('BANKERS_ORDER_(FCB,_RBL,_RBC)_Lumpsums_9May2016.pdf')
fields = doc['fields']
for key in fields.keys():
    print(key, " : ", fields[key])
