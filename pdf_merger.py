import sys
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

def merge_pdfs():
	print(f'Executing Merge PDFs')
	#pdf_file_path = input(f'Enter pdf file path: ')
	pdf_file_path = '.'

	pdfs = input('Enter file names: ').split(' ')

	print(f'PDFs:{pdfs}\nTotal arg: {len(pdfs)}')

	merger = PdfFileMerger()

	result_pdf = ""

	if len(pdfs) < 2:
		print(f'Incorrect usage!!! Correct syntax is as follows:\n> python3 pdf_merger.py <pdf_1> <pdf_2> [pdf_3] ... [pdf_n]')
		exit()

	print(f'{pdfs}')
	out_pdf = PdfFileWriter()

	for pdf in pdfs:
		result_pdf = result_pdf + pdf.replace(" ","_").replace(".pdf","")+"_"
		in_pdf = PdfFileReader(pdf, 'rb')
		for i in range(in_pdf.getNumPages()):
			page = in_pdf.getPage(i)
			out_pdf.addPage(page)

	with open(f'{result_pdf[:-1]}.pdf', 'wb') as f:
		out_pdf.write(f)
		print(f'Saved {result_pdf[:-1]}.pdf')	


def delete_pages():
	print(f'Executing Delete Pages')

	#pdf_file_path = input(f'Enter pdf file path: ')
	pdf_file_path = '.'

	pdf_name = input('Enter file names: ')

	input_pdf = PdfFileReader(pdf_name, 'rb')
	output_pdf = PdfFileWriter()
	output_pdf_name = f'trimmed_{pdf_name}'
	print(f'Options Available:\n1. Delete set of pages (1,3,4,...)\n2. Delete from start to X\n3. Delete from X to end')
	del_choice = (input('Enter you choice: '))

	if del_choice == '1':
		pages_to_delete = [int(x)-1 for x in input(f'Enter space separated pages to delete: ').split(' ')]
		
		for i in range(input_pdf.getNumPages()):
			if i not in pages_to_delete:
				page = input_pdf.getPage(i)
				output_pdf.addPage(page)

		with open(f'{output_pdf_name}', 'wb') as f:
			output_pdf.write(f)
			print(f'Saved {output_pdf_name}')
	elif del_choice == '2':
		del_till_page = int(input(f'Delete from start till (including) page: '))-1

		for i in range(input_pdf.getNumPages()):
			if i > del_till_page:
				page = input_pdf.getPage(i)
				output_pdf.addPage(page)

		with open(f'{output_pdf_name}', 'wb') as f:
			output_pdf.write(f)
			print(f'Saved {output_pdf_name}')
	elif del_choice == '3':
		del_from_page = int(input(f'Delete from (including) page X till end: '))-1

		for i in range(input_pdf.getNumPages()):
			if i < del_from_page:
				page = input_pdf.getPage(i)
				output_pdf.addPage(page)

		with open(f'{output_pdf_name}', 'wb') as f:
			output_pdf.write(f)
			print(f'Saved {output_pdf_name}')

	pass

print(f'Options available:\n1. Merge PDFs\n2. Delete some pages')

choice = input('Enter you choice: ')

if choice == '1':
	merge_pdfs()
elif choice == '2':
	delete_pages()
else:
	print(f'Invalid choice!')