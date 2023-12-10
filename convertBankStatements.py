from pdfminer.high_level import extract_pages, extract_text
import tabula

# ===== BANK STATEMENT TO CSV CONVERTOR =====

# SCRIPT SETTINGS
convertFile = True

# PAGE/TABLE SETTINGS
tableArea = [41, 0, 77, 100]
tableColumns = [30, 50, 65, 75]

# FILE SETTINGS
fileName = "2022_SAMPLE"
filePages = [1, 2]
dirName = ""
dirPages = "all"

# SCRIPT
df = tabula.read_pdf(f"./data/{fileName}.pdf",
                    pages=filePages, 
                    relative_area=True, 
                    relative_columns=True, 
                    area=tableArea, 
                    columns=tableColumns)
if convertFile:
    tabula.convert_into(f"./data/{fileName}.pdf", 
                        f"./outFiles/{fileName}.csv", 
                        output_format="csv", 
                        pages=filePages, 
                        relative_area=True, 
                        relative_columns=True, 
                        area=tableArea, 
                        columns=tableColumns)
else:
    tabula.convert_into_by_batch(f"./data/{dirName}", 
                             output_format="csv", 
                             pages=dirPages, 
                             relative_area=True, 
                             relative_columns=True, 
                             area=tableArea, 
                             columns=tableColumns)


# AMATURE LOGGING
numTables = len(df)
print(numTables)
print("==========================")
print(df[0])
print("==========================")
if (numTables > 1):
    print(df[1])