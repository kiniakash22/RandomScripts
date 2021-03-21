import sys
from PyPDF2 import PdfFileMerger

pdfs = sys.argv[1:]

print(f'PDFs:{pdfs}\nTotal arg: {len(pdfs)}')

merger = PdfFileMerger()

result_pdf = ""

if len(pdfs) < 2:
	print(f'Incorrect usage!!! Correct syntax is as follows:\n> python3 pdf_merger.py <pdf_1> <pdf_2> [pdf_3] ... [pdf_n]')
	exit()

print(f'{pdfs}')

for pdf in pdfs:
	result_pdf = result_pdf + pdf.replace(" ","_").replace(".pdf","")+"_"
	merger.append(pdf)

result_pdf = result_pdf[:-1]+".pdf"
merger.write(result_pdf)
print(f'File saved as {result_pdf}')
merger.close()