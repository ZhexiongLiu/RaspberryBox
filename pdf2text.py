from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import glob2
import sys, getopt

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 


def convertMultiple(pdfDir, txtDir):

    for path_name in glob2.iglob(pdfDir+'**/*.pdf', recursive=True):
    	
        _, file_name = os.path.split(path_name)
        fileExtension = path_name.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = path_name 
            text = convert(pdfFilename)
            text_path = txtDir + file_name.split(".")[0] + ".txt"
            textFile = open(text_path, "w")
            text = text.replace('\n','\n').replace('', '').replace('  ', ' ')
            textFile.write(text)


if __name__ == '__main__':
    pdfDir = "./pdfs/"
    txtDir = "./data/"

    convertMultiple(pdfDir, txtDir)
