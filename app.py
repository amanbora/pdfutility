import PyPDF2
import textract
import nltk
import glob
import os
import sys
import subprocess
import groupdocs_conversion_cloud
import shutil
from docx import *
import re
import slate3k

nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



pdfs_path = '/Users/aman/Desktop/pdfutility/resumes/'
docx_path = '/Users/aman/Desktop/pdfutility/resume-to-docx/'
# list_of_files = glob.glob('/Users/aman/Desktop/pdfutility/resumes/*')
# filename = max(list_of_files, key=os.path.getctime)
filename = '/Users/aman/Desktop/pdfutility/resumes/Resume_1.pdf'

file = os.path.splitext(os.path.basename(filename))[0]
print(file)
output_name= file + '.docx'
filenameDocx = '/Users/aman/Desktop/pdfutility/resume-to-docx/'+output_name

app_sid= 'ccd4b025-8cb8-4696-8936-84c99b110712'
app_key= '4586c5ef8a096dba403e74d94c576ac9'

convert_api = groupdocs_conversion_cloud.ConvertApi.from_keys(app_sid, app_key)
file_api = groupdocs_conversion_cloud.FileApi.from_keys(app_sid, app_key)

def convertPdfToDocx():
    try:

            #upload soruce file to storage
            # filename = 'Sample.pdf'
            remote_name = 'Sample.pdf'
            strformat='docx'

            request_upload = groupdocs_conversion_cloud.UploadFileRequest(remote_name,filename)
            response_upload = file_api.upload_file(request_upload)
            #Convert PDF to Word document
            settings = groupdocs_conversion_cloud.ConvertSettings()
            settings.file_path =remote_name
            settings.format = strformat
            settings.output_path = output_name

            loadOptions = groupdocs_conversion_cloud.PdfLoadOptions()
            loadOptions.hide_pdf_annotations = True
            loadOptions.remove_embedded_files = False
            loadOptions.flatten_all_fields = True

            settings.load_options = loadOptions

            convertOptions = groupdocs_conversion_cloud.DocxConvertOptions()
            convertOptions.from_page = 1
            convertOptions.pages_count = 1

            settings.convert_options = convertOptions        
            request = groupdocs_conversion_cloud.ConvertDocumentRequest(settings)
            response = convert_api.convert_document(request)

            request_download = groupdocs_conversion_cloud.DownloadFileRequest(output_name)
            response_download = file_api.download_file(request_download)
            shutil.copyfile(response_download, filenameDocx)
        
            print("Document converted successfully: " + str(response))
    except groupdocs_conversion_cloud.ApiException as e:
            print("Exception when calling get_supported_conversion_types: {0}".format(e.message))

def pdfToText():
	doc = slate3k.PDF(open(filename,'r'))
	print(doc[0])
	return doc


pdfFileObj = open(filename, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

total_pages = pdfReader.numPages
count = 0
text = ""

#while loop to go through each page
while count < total_pages:
	pageObj = pdfReader.getPage(count)
	count += 1
	text += pageObj.extractText()

# #checking if words are retruned from above
# if text != "":
# 	text = text

# #if no text then we run OCR library textract to convert scanned/image based PDF
# else:
# 	text = textract.process(fileurl, method='tesseract', language='eng')


# #remove whitespaces and extracting keywords

# #break text into indivisual words
# tokens = word_tokenize(text)

# #remove punctuations
# punctuations = ['(', ')' , ',' , ';' , ':' , '[' , ']' ]

# #remove (stopwords) words like "the", "I", "and" etc
# stop_words = stopwords.words('english')

# #getting our keywords
# keywords = [word for word in tokens if not word in stop_words and not word in punctuations]

# convertPdfToDocx()

#extract all bold titles
# document = Document()

# bolds = []
# for para in document.paragraphs :
# 	for run in para.runs :
# 		if run.bold :
# 			bolds.append(run.text)

# doc = pdfToText()
# print(doc[0])

#extract email
lst = re.findall('\S+@\S+', text)
print(lst)

def listToString(s):
	str = ""
	for ele in s:
		str +="\n"+ele
	return str
output_file = open('/Users/aman/Desktop/pdfutility/output.txt','w')
output_file.write(text)
output_file.close()

# print(bolds)
sys.stdout.flush()