# importing required modules 
import PyPDF2 
	
# creating a pdf file object 
pdfFileObj = open('contract.pdf', 'rb') 
	
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
	
# printing number of pages in pdf file 
# print(pdfReader.numPages) 
nPages = pdfReader.numPages	
# creating a page object 
for i in range(nPages):
	pageObj = pdfReader.getPage(i) 
	# extracting text from page 
	print(pageObj.extractText()) 

	
# closing the pdf file object 
pdfFileObj.close() 


