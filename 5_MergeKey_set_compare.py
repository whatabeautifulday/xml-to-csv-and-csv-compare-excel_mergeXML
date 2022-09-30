#1. 將兩表重複資料抓出 筆數一定等於

import pandas as pd
import numpy as np
import datetime as date
import re
from io import StringIO
import os

today = date.date.today()
today = today.strftime("%m%d")

# # 1. input csv
df1 = pd.read_csv("combined_new_csv.csv", thousands=",", engine='python', error_bad_lines=False, dtype=object) #新資料 new_sort_head.csv
df2 = pd.read_csv("combined_old_csv.csv", thousands=",", engine='python', error_bad_lines=False, dtype=object) #舊_y資料 old_sort_head.csv

pwb = open(f'{today}_select_header.txt','r').read().split()
print(pwb)

df1 = df1.loc[:,pwb]
print(df1)
df2 = df2.loc[:,pwb]
print(df2)

merge_key = open(f'{today}_merge_key.txt','r').read().split()
print(merge_key)
print(type(merge_key))
df1['merge'] = df1[merge_key].astype(str).apply(lambda x: ' + '.join(x), axis=1)
df2['merge'] = df2[merge_key].astype(str).apply(lambda x: ' + '.join(x), axis=1)
# df1['merge'] = df1[['26_CORR_TYPE', '27_CORR_KEY']].astype(str).apply(lambda x: ''.join(x), axis=1)
# df2['merge'] = df2[['26_CORR_TYPE', '27_CORR_KEY']].astype(str).apply(lambda x: ''.join(x), axis=1)
print(df1)
print(df2)
df1.to_csv('df1.csv')
df2.to_csv('df2.csv')

key = open(f'{today}_key.txt','r').read().split()
sort_df1 = df1.sort_values(by=key)
sort_df2 = df2.sort_values(by=key)
print(sort_df1)
print(sort_df2)

#3. old + new
data_m = sort_df2.append(sort_df1) 
print(data_m)
# data_m.to_csv(f'{today}_data_m.csv')

#4. 將重複資料刪除剩一個 distinct
a = data_m.drop_duplicates(key, keep='first') 
print(a)
# a.to_csv(f'{today}_distinct.csv')

#5. 將重複資料刪除保留孤立的
b = data_m.drop_duplicates(key, keep=False) 
b.to_csv(f'{today}_old_independent_set.csv')
b.to_excel(f'{today}_old_independent_set.xlsx')


#6. 將重複資料刪除剩一個 - 孤立的 = 重複資料
data_df2_append = a.append(b).drop_duplicates(keep=False)
data_df2_append = data_df2_append.reset_index(inplace=False, drop=True)
# data_df2_append.to_csv(f'{today}_data_df2_duplicates.csv', sep='|')

#new + old
data_m = sort_df1.append(sort_df2) 
#將重複資料刪除剩一個
a = data_m.drop_duplicates(key, keep='first') 
#將重複資料刪除保留孤立的
b = data_m.drop_duplicates(key, keep=False) 
# b.to_csv(f'{today}_new_independent_set.csv')

#將重複資料刪除剩一個 - 孤立的 = 重複資料
data_df1_append = a.append(b).drop_duplicates(keep=False)
data_df1_append = data_df1_append.reset_index(inplace=False, drop=True)
# data_df1_append.to_csv(f'{today}_data_df1_duplicates.csv', sep='|')

print(data_df1_append)
print(data_df2_append)
data_df1_append = data_df1_append.sort_values(by=key)
data_df2_append = data_df2_append.sort_values(by=key)
print(data_df1_append)
print(data_df2_append)
data_df1_append = data_df1_append.reset_index(inplace=False, drop=True)
data_df2_append = data_df2_append.reset_index(inplace=False, drop=True)

data_df1_append.to_csv('new_eq.csv', sep='|')
data_df2_append.to_csv('old_eq.csv', sep='|')


df1 = pd.read_csv('new_eq.csv', sep='|', engine='python').fillna('nan') #新資料 new_sort_head.csv
df2 = pd.read_csv('old_eq.csv', sep='|', engine='python').fillna('nan') #舊_y資料 old_sort_head.csv



array1 = np.array(df1) # Storing the data in an array will allow the equation below to show the differences.
array2 = np.array(df2)
df1_header = pd.read_csv('s_new_header.csv', sep='|', engine='python') #新資料標題
df2_header = pd.read_csv('s_old_header_y.csv', sep='|', engine='python') #舊資料標題
df_CSV_1 = pd.DataFrame(array1, columns = df1_header.columns)
df_CSV_2 = pd.DataFrame(array2, columns = df2_header.columns)

print(df_CSV_1)
# df_CSV_1.to_csv(f'{today}_df_CSV_1.csv')
print(df_CSV_2)
# df_CSV_2.to_csv(f'{today}_df_CSV_2.csv')

print(df1.eq(df2)) # This shows the differences between the two arrays.
csv_TorF = df1.eq(df2).astype(str) #df1比較df2 欄位是用 df1 存
print(csv_TorF)
# csv_TorF.to_csv(f'{today}_csv_TorF.csv')

df_CSV12_merge = df_CSV_1.merge(df_CSV_2, on='Unnamed: 0', how='left') #df_CSV_1 df_CSV_2 合併
# df_CSV12_merge.to_csv(f'{today}_df_csv12_merge.csv')

data_r = pd.DataFrame([])
for dfcsv2, dfcsv1 in zip(df_CSV_2, df_CSV_1):
    print(dfcsv2, dfcsv1)
    csv_f = csv_TorF[dfcsv1].str.contains('False', na=False) #某一欄, 如果是false 得 True
    print(csv_f)
    csv_f_result = df_CSV12_merge.loc[csv_f, [dfcsv2, dfcsv1]] #根據csv_f : true 抓取[內容]
    print(csv_f_result)
    

    if len(csv_f_result) == 0:
        print('true, empty')
    else:
        data_r = data_r.join(csv_f_result, how='outer') #合併

data_r_columns = data_r.columns
print(data_r_columns)
print(data_r)

CORR_KEY_data_r = df_CSV_1[key] #抓出COOR_KEY

CORR_KEY_data_r = pd.concat([CORR_KEY_data_r, data_r], axis=1) #COOR_KEY 合併 data_r
print(CORR_KEY_data_r) 



CORR_KEY_data_r = CORR_KEY_data_r.dropna(subset=data_r.columns, how='all') #把某一row都是nan 刪除(把相比後得出false的空值欄位刪除)
print(CORR_KEY_data_r) 


CORR_KEY_data_r.to_csv(f'{today}_result.csv', index = False)
CORR_KEY_data_r.to_csv(f'{today}_result_I_.csv', sep='|', index = False)
CORR_KEY_data_r.to_excel(f'{today}_result_xlsx.xlsx', index = False)

df_result = pd.read_csv(f'{today}_result_I_.csv', sep='|', engine='python') #新資料 new_sort_head.csv
print(df_result.columns)

df_result_col_update = []
for df_r_col in df_result.columns:
    df_r_col = re.sub("_y", "_old", df_r_col) 
    df_r_col = re.sub("merge", str(merge_key), df_r_col)
    df_result_col_update.append(df_r_col)
print(df_result_col_update)

df_result.columns = [df_result_col_update]
print(df_result)

# df_result.to_csv(f'{today}_result_I_.csv', sep='|', index = False)
df_result.to_csv(f'{today}_result.csv', index = False)
df_result.to_excel(f'{today}_result_xlsx.xlsx', index = False)


new_header = []
data = pd.read_csv(f'{today}_result.csv')

for i in range(len(data.columns)):
    if i == 0:
        print(data.columns[i])
        new_header.append(data.columns[i])
        continue
    ss = os.path.basename(data.columns[i])

    new_header.append(ss)
    print(i, ss)
print(new_header)

data.columns = new_header
data.to_csv(f'{today}_result.csv', index = False)
data.to_excel(f'{today}_result_xlsx.xlsx', index = False)
