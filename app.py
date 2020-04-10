import os
import subprocess
import glob
import re
import json
from docx import *

pdfPath = '/Users/aman/Desktop/pdfutility/resumes'
docxPath = '/Users/aman/Desktop/pdfutility/resumetodocx'

list_of_pdf_files = glob.glob(pdfPath + '/*')
inputFilename = max(list_of_pdf_files, key=os.path.getctime)
print(inputFilename)

def convertToDoc():
	subprocess.call('soffice --headless --infilter=writer_pdf_import --convert-to docx --outdir /Users/aman/Desktop/pdfutility/resumetodocx "{}"'
                    .format(inputFilename), shell=True)

# convertToDoc()
list_of_doc_files = glob.glob(docxPath + '/*')
docFile = max(list_of_doc_files, key=os.path.getctime)
print(docFile)
document = Document('/Users/aman/Desktop/pdfutility/resumetodocx/Resume3.docx')
bolds=[]
emails=[]
phones=[]

for para in document.paragraphs:
	text = para.text
	email_list = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",text)
	phone_list=re.findall(r'[\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9]',text)
	for email in email_list:
		emails.append(email)
	
	for phone in phone_list:
		phones.append(phone)

	for run in para.runs:
		if run.bold:
			bolds.append(run.text)

style_Dict={'emails':emails,
              'phone_numbers':phones,
              'bold_phrases':bolds
              }
 
print("\nWord File Output:\n")
 
r = json.dumps(style_Dict)
loaded_r = json.loads(r)
print("\n",json.dumps(loaded_r,indent=4, sort_keys=False))

sys.stdout.flush()