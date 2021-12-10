

from PyPDF2 import PdfFileMerger, PdfFileReader
import os


merged_object = PdfFileMerger()
str_output_name = 'output.pdf'

lst_pdfs = []
for obj in os.listdir('pdf/'):
    if '.pdf' not in obj:
        pass
    else:
        lst_pdfs.append(obj)
files = (','.join(lst_pdfs))
print(files)


for file_name in lst_pdfs:
    merged_object.append(PdfFileReader('files', 'rb'))


"""

    #merged_object.write(f’orders/{str_output_name}’)
"""
