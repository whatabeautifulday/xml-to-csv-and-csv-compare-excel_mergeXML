from pandas.io.parsers import read_table
import pandas as pd
import numpy as np
import datetime as date

from pandas.core.frame import DataFrame

today = date.date.today()
today = today.strftime("%m%d")

# # 1. input csv
# df1 = pd.read_csv(f'{today}_xml_del_out_in_to_csv_new.csv', thousands=",", sep='|', engine='python', error_bad_lines=False) #新資料 new_sort_head.csv
# df2 = pd.read_csv(f'{today}_xml_del_out_in_to_csv_old.csv', thousands=",", sep='|', engine='python', error_bad_lines=False) #舊_y資料 old_sort_head.csv
# print(type(df1))
key = f'{today}_key.txt' #create _select_header.txt by  _xml_head
f = open(key, 'w')
print("1. Please edit the mmdd_select_header.txt in the current folder")
print("2. Please edit the mmdd_merge_key.txt in the current folder")
print("3. input key : merge")
key2 = input('input key :')
f.write(key2 + '\n')
f.close()


pwb = open(f'{today}_select_header.txt','r').read().split() #透過header 手動 刪掉不要的tag
print(pwb)

# df1 = df1.loc[:,pwb]
# print(df1)
# df2 = df2.loc[:,pwb]
# print(df2)

pwb = pd.DataFrame(pwb).T
print(pwb)

#del head
pwb.columns = pwb.iloc[0]
print(pwb)
pwb = pwb[1:]
#最左邊 add column
pwb.insert(0, "", '', True)

print(len(pwb.columns))
pwb.insert(len(pwb.columns), "merge", '', True)
pwb.to_csv('s_new_header.csv',sep='|', index=False)
# print(pwb)
#create old_header_y
child5 = []
for i in pwb:
    if i != '':
        child5.append(i + '_y')
child5 = pd.DataFrame(child5).T
print(child5)
child5.columns = child5.iloc[0]
child5 = child5[1:]
child5.insert(0, "", '', True)
child5.to_csv('s_old_header_y.csv',sep='|', index=False)

