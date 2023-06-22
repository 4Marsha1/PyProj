from PyPDF2 import PdfMerger
import os

PATH_IN = './files'
PATH_OUT = './mergedFiles'

merger = PdfMerger()

for file in os.listdir(PATH_IN):
    if file.endswith('.pdf'): 
        merger.append(f"{PATH_IN}/{file}")

merger.write(f"{PATH_OUT}/merged.pdf")
merger.close()
