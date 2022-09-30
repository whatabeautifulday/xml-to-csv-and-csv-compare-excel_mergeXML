import csv
import pandas as pd
import win32com.client
import pandas as pd
import os
import re

excel = win32com.client.DispatchEx('Excel.Application')
xml1 = excel.Workbooks.Open(os.getcwd() + "\\" + "xml_merge_old.xml")
xml1.SaveAs(os.getcwd() +"\\" + "xml_merge_old.xlsx")
xml1.Close()

df = pd.read_excel('xml_merge_old.xlsx',header=1)
df = df[df.columns.drop(list(df.filter(regex='agg')))] #刪除多餘的col 含有agg
df.to_csv('xml_merge_old.csv', index=None)
print(df)

# # 把'/asx:abap/asx:values/', '/asx:abap/@' 替換掉
# with open('xml_merge_old.csv',encoding="utf-8") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = ',')
#     list_of_column_names = []
 
#     for row in csv_reader:
#         list_of_column_names.append(row)
#         break
# header = list_of_column_names[0]
# # header = [w.replace('/asx:abap/asx:values/', '') for w in header]
# # header = [w.replace('/asx:abap/@', '') for w in header]
# # header = [w.replace('/', '_') for w in header]
# # header = [w.replace('-', '_') for w in header]
# header = [w.replace('/ns0_abap/ns0_values/', '') for w in header]
# print(header)

# df = pd.read_csv('xml_merge_old.csv',header=1, names = header)
df.to_csv('combined_old_csv.csv',index=None)


