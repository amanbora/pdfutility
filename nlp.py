import os
import subprocess
import glob
import sys
from pyresparser import ResumeParser

Path = '/Users/aman/Desktop/pdfutility/resumes'
list_of_files = glob.glob(Path + '/*')
inputFilename = max(list_of_files, key=os.path.getctime)
# print(inputFilename)

data = ResumeParser(inputFilename).get_extracted_data()

print(data)

sys.stdout.flush()