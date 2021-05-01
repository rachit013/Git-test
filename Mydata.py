import PyPDF2
import camelot
import tabula
from tabula import read_pdf
from tabulate import tabulate
# import camelot
import pandas as pd
import ssl

# creating a pdf file object
# pdfFileObj = open('Medivir AB notice-agm.pdf--AGM 2021.pdf', 'rb')
#
# creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
# # printing number of pages in pdf file
# print(pdfReader.numPages)
#
# # creating a page object
# pageObj = pdfReader.getPage(0)
#
# # extracting text from page
# print(pageObj.extractText())
#
# # closing the pdf file object
# pdfFileObj.close()
# with open('Medivir AB notice-agm.pdf--AGM 2021.pdf', 'r') as file:
#
#     # reading each line
#     for line in file:
#
#         # reading each word
#         for word in line.split():
#
#             # displaying the words
#             print(word)

# my_file = open('My_resume.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(my_file)
#
# print(pdf_reader.numPages)
# page_one = pdf_reader.getPage(0)
#
# output_file = open('new.pdf', 'wb')
#
# pdf_writer = PyPDF2.PdfFileWriter()
# pdf_writer.addPage(page_one)
# pdf_writer.write(output_file)

# pdfFileObj = open('Medivir AB notice-agm.pdf--AGM 2021.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
#
# search_word = "remuneration"
# search_word_count = 0
#
# getpage = pdfReader.getPage(30)
#
# for pageNum in range(0, pdfReader.numPages):
#     pageObj = pdfReader.getPage(pageNum)
#     text = pageObj.extractText().encode('utf-8')
#     search_text = text.lower().split()
#     for word in search_text:
#         if search_word in word.decode("utf-8"):
#             search_word_count += 1
#
# print("The word {} was found {} times".format(search_word, search_word_count))
#
# pdfFileObj = open('Medivir AB notice-agm.pdf--AGM 2021.pdf', 'rb')
# try:
#     df = read_pdf(pdfFileObj)
#     print(df)
# except Exception as e:
#     print("Error {}", format(e))


# table1 = tabula.read_pdf("Medivir AB aarsredovisning-2020-eng-index (2).pdf", pages=32)
# t = PrettyTable(table1)
# print(table1[0])

# file = "Medivir AB aarsredovisning-2020-eng-index (2).pdf"
# tables = tabula.read_pdf(file, pages="32")
# print(tabulate(tables[0]))


# tables[0].df
# reads table from pdf file
#
# df = read_pdf("Medivir AB aarsredovisning-2020-eng-index (2).pdf", pages=32)
# print((df))


