from numpy.lib.function_base import append
import pandas as pd
import numpy as np
import datetime as date
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import re
from io import StringIO
import pandas as pd
import glob, os

today = date.date.today()
today = today.strftime("%m%d")

# # 從csv_old 抓取[0]一筆資料
# os.chdir("./csv_old")
# files = []
# for file in glob.glob("*.csv"):
#     files.append(file)
# print(files[0])

df1 = pd.read_csv('combined_old_csv.csv', dtype=object ,encoding='latin1')
before_columns = list(df1.columns) #get column
# #delete space 存進k=[]
k = []
for i in before_columns:
    j = i.replace(' ','')
    k.append(j)
print(k)

df = pd.DataFrame(k).T #list to T 橫轉直
df.columns = df.iloc[0] #Do not display index
print(df)
df = df[1:] # 從位置1開始取值

# get header
select_header = f'{today}_select_header.txt' #create _select_header.txt by  _xml_head
f = open(select_header, 'w',encoding='UTF-8')
for df1 in df:
    f.write(df1 + '\n')
    print(df1)
f.close()

# get header
merge_key = f'{today}_merge_key.txt' #create _select_header.txt by  _xml_head
f = open(merge_key, 'w',encoding='UTF-8')
for df1 in df:
    f.write(df1 + '\n')
    print(df1)
f.close()


df.to_csv('header.csv', sep=';', index=False) #Do not display index
df.to_csv('new_header.csv', sep='|') #Do not display index


child5 = []
for i in df:
    if i != '':
        child5.append(i + '_y')
child5 = pd.DataFrame(child5).T
# print(child5)
child5.columns = child5.iloc[0]
child5 = child5[1:]
child5.insert(0, "", '', True)
child5.to_csv('old_header_y.csv',sep='|', index=False)
