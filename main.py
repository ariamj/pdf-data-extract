import re
from pdfminer.high_level import extract_pages, extract_text
import json
import csv
import tabula


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

# # convert pdf tables to csv file
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

df = tabula.read_pdf("./data/T_slips_Kevin_Wu.pdf", pages='all')
# tabula.convert_into("./data/T_slips_Kevin_Wu.pdf", "./outFiles/T_slips_Kevin_Wu.csv", output_format="csv", pages='all')
# print(df)

# df = tabula.read_pdf("./data/sampleData.pdf", pages='all')

quantity_v = []
id_v = []
cost_v = []
dis_v = []
for table in df:
    dfd = table.to_dict('dict')
    if (dfd['Box value'][1] == "USD"):
        quantity_v.append(dfd['Box value'][3])
        id_v.append(dfd['Box value'][4])
        cost_v.append(dfd['Box value'][7])
        dis_v.append(dfd['Box value'][8])

dict2 = {
    "Quantity of securities": quantity_v,
    "Identification fo securities": id_v,
    "Cost or book value": cost_v,
    "Proceeds of disposition or settlement amount": dis_v
}
json_object = json.dumps(dict2, indent=4)
with open("./outFiles/usd.json", "w") as outfile:
    outfile.write(json_object)

with open("./outFiles/usd.json") as json_file:
    data = json.load(json_file)

data_file = open("./outFiles/usd_data.csv", "w")

csv_writer = csv.writer(data_file)

count = 0

for value in data:
    # print(value)
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    # print(data[value])
    csv_writer.writerow(data[value])

data_file.close()
