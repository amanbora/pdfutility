import PyPDF2
import textract
import nltk

nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

filename = './resumes/Resume_1.pdf'

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

#checking if words are retruned from above
if text != "":
	text = text

#if no text then we run OCR library textract to convert scanned/image based PDF
else:
	text = textract.process(fileurl, method='tesseract', language='eng')

print(text)

#remove whitespaces and extracting keywords

#break text into indivisual words
tokens = word_tokenize(text)

#remove punctuations
punctuations = ['(', ')' , ',' , ';' , ':' , '[' , ']' ]

#remove (stopwords) words like "the", "I", "and" etc
stop_words = stopwords.words('english')

#getting our keywords
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]

print(keywords)

def listToString(s):
	str = ""
	for ele in s:
		str +="\n"+ele
	return str
output_file = open('output.txt','w')
output_file.write(listToString(keywords))
output_file.close()
