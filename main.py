import re
from pdfminer.high_level import extract_pages, extract_text
import json
import csv
import tabula
import os
import pandas as pd
import glob
from img2table.document import PDF, Image
from img2table.ocr import PaddleOCR


########################################################
## SAMPLE TESTING
########################################################

# CITE: https://youtu.be/w2r2Bg42UPY
# # print all elements of the page
# for page_layout in extract_pages("./data/SamplePDF.pdf"):
#     for element in page_layout:
#         print(element)

# # print all the text in the page
# text = extract_text("./data/SamplePDF.pdf")
# print(text)

# # print all text that matches the regula expression in the page
# pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
# matches = pattern.findall(text)
# words = [n[:-1] for n in matches]
# print(matches)
# print(words)

# CITE: https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
# # write data to json file
# dictionary = {
#     "name": "hello world",
#     "quantity": 45,
#     "amount": "$52367"
# }
# json_object = json.dumps(dictionary, indent=4)
# with open("./outFiles/sample.json", "w") as outfile:
#     outfile.write(json_object)

# CITE: https://www.tutorialspoint.com/how-to-convert-pdf-files-to-excel-files-using-python
# # read and convert pdf tables to csv file
# df = tabula.read_pdf("./data/SamplePDF2.pdf", pages='all')[0]
# tabula.convert_into("./data/SamplePDF2.pdf", "./outFiles/sample.csv", output_format="csv", pages='all')
# print(df)

# # Write table data into json file
# df = tabula.read_pdf("./data/SamplePDF.pdf", pages='all')
# anime_v = []
# titles_v = []
# for table in df:
#     dfd = table.to_dict('dict')
#     anime_v.append(dfd['Amount'][2])
#     titles_v.append(dfd['Amount'][4])
# dict2 = {
#     "Anime:": anime_v,
#     "Titles": titles_v
# }
# json_object = json.dumps(dict2, indent=4)
# with open("./outFiles/sample.json", "w") as outfile:
#     outfile.write(json_object)


########################################################
## CODE
########################################################

# PAGE/TABLE SETTINGS
# top, left, bottom, right
tableArea = [17, 0, 68, 100]
tableColumns = [13, 22, 55]

# COLLECTION OF TABLEAREA AND TABLECOLUMNS VALUES FOR DIFFERENT PDFS
# key = <pdf-type-name> ; value = { <tableArea>, <tableColumns> }
borderlessTableValues = {
    "td-bank-bank-statement": [ [41, 0, 77, 100], [30, 50, 65, 75] ],
    "business-banking-bank-statement-page-1": [ [65, 0, 90, 95],  [16, 50, 66, 80]],
    "business-banking-bank-statement-page-2": [ [14, 0, 20, 95],  [16, 50, 66, 80]],
    "BMO-mastercard-statement": [ [17, 0, 68, 100], [13, 22, 55] ], # page 3
    "BMO-mastercard-statement-wide": [ [22, 0, 32, 100], [16, 22, 66, 80] ], # page 3
}

# FILE SETTINGS
fileName = "file1"
filePages = [3]

# BORDERLESS TABLES
# pdf = PDF(f"./data/{fileName}.pdf", pages=[0, 2])
# pdf_tables = pdf.extract_tables(borderless_tables=True)
# # pdf_tables = pdf.extract_tables(ocr=ocr, implicit_rows=False, borderless_tables=True, min_confidence=50)
# pdf.to_xlsx(f"./outFiles/{fileName}.xlsx", borderless_tables=True)

# numTables1 = len(pdf_tables)
# print(numTables1)
# print("==========================")
# print(pdf_tables[0])
# print("==========================")
# if (numTables1 > 1):
    # print(pdf_tables[1])

folderName = "mastercard"
dirPath = f"./data/{folderName}"

# DIR OF PDFs
directory = os.fsencode(dirPath)
for file in os.listdir(directory):
    fileName = os.fsdecode(file)
    print(fileName)
    df = tabula.read_pdf(f"./data/{folderName}/{fileName}", pages=filePages, relative_area=True, relative_columns=True, area=tableArea, columns=tableColumns)
    tabula.convert_into(f"./data/{folderName}/{fileName}", f"./outFiles/{folderName}/{fileName}.csv", output_format="csv", pages=filePages, relative_area=True, relative_columns=True, area=tableArea, columns=tableColumns)

# tableArea = [17, 0, 68, 100]
# tableColumns = [13, 22, 55]
# df = tabula.read_pdf(f"./data/{folderName}/{fileName}.pdf", pages=[3], relative_area=True, relative_columns=True, area=tableArea, columns=tableColumns)
# tabula.convert_into(f"./data/{folderName}/{fileName}.pdf", f"./outFiles/{folderName}/{fileName}.csv", output_format="csv", pages=[3], relative_area=True, relative_columns=True, area=tableArea, columns=tableColumns)

# df = tabula.read_pdf(f"./data/{folderName}/{fileName}.pdf", pages=filePages)
# tabula.convert_into(f"./data/{folderName}/{fileName}.pdf", f"./outFiles/{folderName}/{fileName}.csv", output_format="csv", pages=filePages)

# all_files = glob.glob(dirPath + "/*.pdf")
# df = []
# for file in all_files:
#     df = pd.concat(tabula.read_pdf(file, pages = filePages))
# df.to_csv(f"./outFiles/{folderName}.csv", index = False)

# REGULAR BORDERED TABLE
# df = tabula.read_pdf(f"./data/{fileName}.pdf", pages=filePages)
# tabula.convert_into(f"./data/{fileName}.pdf", f"./outFiles/{fileName}.csv", output_format="csv", pages=filePages)

# SCRIPT
# df = tabula.read_pdf(f"./data/{fileName}.pdf", pages=filePages, relative_area=True, relative_columns=True, area=tableArea, columns=tableColumns)
# tabula.convert_into(f"./data/{fileName}.pdf", f"./outFiles/{fileName}.csv", output_format="csv", pages=filePages, relative_area=True, relative_columns=True, area=tableArea, columns=tableColumns)
# numTables = len(df)
# print(numTables)
# print("==========================")
# print(df[0])
# print("==========================")
# if (numTables > 1):
#     print(df[1])
# print(df)

# df = tabula.read_pdf("./data/sampleData.pdf", pages='all')

# quantity_v = []
# id_v = []
# cost_v = []
# dis_v = []
# for table in df:
#     #  CITE: https://stackoverflow.com/questions/26716616/convert-a-pandas-dataframe-to-a-dictionary
#     # convert dataFrame to dictionary
#     dfd = table.to_dict('dict')
#     if (dfd['Box value'][1] == "CAD"):
#         quantity_v.append(dfd['Box value'][3])
#         id_v.append(dfd['Box value'][4])
#         cost_v.append(dfd['Box value'][7])
#         dis_v.append(dfd['Box value'][8])

# dict2 = {
#     "Quantity of securities": quantity_v,
#     "Identification fo securities": id_v,
#     "Cost or book value": cost_v,
#     "Proceeds of disposition or settlement amount": dis_v
# }
# json_object = json.dumps(dict2, indent=4)
# with open("./outFiles/cad.json", "w") as outfile:
#     outfile.write(json_object)

# # CITE: https://www.geeksforgeeks.org/convert-json-to-csv-in-python/
# # write json file to csv file
# with open("./outFiles/cad.json") as json_file:
#     data = json.load(json_file)

# data_file = open("./outFiles/cad_data.csv", "w")

# csv_writer = csv.writer(data_file)

# count = 0

# for value in data:
#     # print(value)
#     if count == 0:
#         header = data.keys()
#         csv_writer.writerow(header)
#         count += 1
#     # print(data[value])
#     csv_writer.writerow(data[value])

# data_file.close()
