
# importing required modules
from PyPDF2 import PdfReader
from os import walk
import json
pdfs_readeds = []
for (dirpath, dirnames, filenames) in walk('pdfs'):
    for name in filenames:
      reader = PdfReader(f"pdfs/{filenames[0]}")

      # printing number of pages in pdf file
      print(len(reader.pages))

      # getting a specific page from the pdf file
      for page in reader.pages:
        # extracting text from page
        text = page.extract_text()
        print("TESTE", text)
        pdfs_readeds.append(json.dumps(text, indent=4))

with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(pdfs_readeds, indent=4))
# creating a pdf reader object
