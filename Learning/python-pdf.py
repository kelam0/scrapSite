# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:05:13 2016

if not flag:

else:

"""

import PyPDF2
path = 'C:\\Users\\Malek\\Documents\\Python Projects\\AtBS\\automate_online-materials\\'

pdfFileObj = open(path + 'meetingminutes.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

if pdfReader.isEncrypted:
    pdfReader.decrypt('barclays')
    
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
pageObj.extractText()

print(pageObj.extractText())


# script to combine 2 existing pdf files into 1.

import PyPDF2
path = 'C:\\Users\\Malek\\Documents\\Python Projects\\AtBS\\automate_online-materials\\'

pdfFileObj = open(path + 'meetingminutes.pdf', 'rb')

pdf1File = open('meetingminutes.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)

pdf2File = open('meetingminutes2.pdf', 'rb')
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()


# rotate pages of a pdf file and save it as a different pdf file.
# #AlwaysKeepACopy

import PyPDF2

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)

page = pdfReader.getPage(0)
page.rotateClockwise(90)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)

resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)

resultPdfFile.close()
minutesFile.close()


# script to overlay pages a watermark template like "draft" on every page.

import PyPDF2

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)

minutesFirstPage = pdfReader.getPage(0)

pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))

minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)

minutesFile.close()
resultPdfFile.close()

# script to encript your pdf files

import PyPDF2

pdfFile = open('meetingminutes.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))
    
pdfWriter.encrypt('swordfish')

resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()

