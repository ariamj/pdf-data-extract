import re
from pdfminer.high_level import extract_pages, extract_text
import json


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
# with open("./json/sample.json", "w") as outfile:
#     outfile.write(json_object)


########################################################
## CODE
########################################################


