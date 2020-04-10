import os
import subprocess
import glob

pdfPath = '/Users/aman/Desktop/pdfutility/resumes'
docxPath = '/Users/aman/Desktop/pdfutility/resumetodocx'

list_of_files = glob.glob(pdfPath + '/*')
inputFilename = max(list_of_files, key=os.path.getctime)
print(inputFilename)

# for top, dirs, files in os.walk(pdfPath):
#     for file in files:
#         if file.endswith('.pdf'):
            # abspath = os.path.join(top,file)
subprocess.call('soffice --headless --infilter=writer_pdf_import --convert-to doc --outdir /Users/aman/Desktop/pdfutility/resumetodocx "{}"'
                .format(inputFilename), shell=True)
print("DONE")