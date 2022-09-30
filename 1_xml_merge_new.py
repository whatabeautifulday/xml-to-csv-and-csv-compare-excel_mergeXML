import xml.etree.ElementTree as ET
import glob
from xml.etree import ElementTree
import datetime as date
import pandas as pd
import tkinter as tk
from tkinter import filedialog

today = date.date.today()
today = today.strftime("%m%d")

root = tk.Tk()
root.withdraw()
# file_path = filedialog.askdirectory(title='Please choose new file')

file_path = './xml_new_original'
# dirlist_csv_new = os.listdir(path_csv_new)
# print(file_path)

xml_files_new = glob.glob(file_path + '\*.*')


#抓取new xml fild, all data 
# xml_files_new = glob.glob(r'C:\Users\w9013769\Desktop\anderson\PCB040_new\CPE2LOMSJ.*')
# print(xml_files_new)
xml_element_tree_new = None

#多的xml合併成一個
for xml_file_new in xml_files_new:
    print(xml_file_new)

    # parser = ElementTree.XMLParser(encoding = "iso-8859-1")
    # data = ElementTree.parse(xml_file_new, parser)
    xml_file_new = xml_file_new.replace(u'\uFFFD', "?")
    data = ElementTree.parse(xml_file_new).getroot()
    #print(ElementTree.tostring(data))
    for PWB_DATA in data.iter('sf'):
        if xml_element_tree_new is None:
            xml_element_tree_new = data 
            insertion_point_new = xml_element_tree_new.findall(".")[0]
        else:
            insertion_point_new.extend(PWB_DATA) 
if xml_element_tree_new is not None:
    #print(ElementTree.tostring(xml_element_tree))
    xml_element_tree_new = ElementTree.tostring(xml_element_tree_new)
    # print(xml_result)
    xml_element_tree_new = str(xml_element_tree_new, encoding='utf-8')
    # print(xml_element_tree_new)

    #取代
    xml_element_tree_new = xml_element_tree_new.replace(':', '_')
    xml_element_tree_new = xml_element_tree_new.replace(',', '')
    xml_result_new = xml_element_tree_new.replace(' version="1.0"', '')

    # 開啟檔案xml
    # fp = open(f'{today}_xml_merge_new.xml', 'w')
    fp = open('./xml_merge_new.xml', 'w')
    # 寫入 This is a testing! 到檔案
    fp.write(xml_result_new)
    
    # 關閉檔案
    fp.close()

# #抓取new xml fild, all data 

# root = tk.Tk()
# root.withdraw()
# file_path = filedialog.askdirectory(title='Please choose new file')
# print(file_path)

# xml_files_new = glob.glob(file_path + '\*.*')
# print(xml_files_new)

# # xml_files_new = glob.glob(r'C:\Users\w9013769\Desktop\anderson\PCB040_new\CPE2LOMSK.*')
# # print(xml_files_new)
# xml_element_tree_new = None

# for xml_file_new in xml_files_new:
#     data = ElementTree.parse(xml_file_new).getroot()
#     #print(ElementTree.tostring(data))
#     for PWB_DATA in data.iter('sf'):
#         if xml_element_tree_new is None:
#             xml_element_tree_new = data 
#             insertion_point_new = xml_element_tree_new.findall(".")[0]
#         else:
#             insertion_point_new.extend(PWB_DATA) 
# if xml_element_tree_new is not None:
#     #print(ElementTree.tostring(xml_element_tree))
#     xml_element_tree_new = ElementTree.tostring(xml_element_tree_new)
#     # print(xml_result)
#     xml_element_tree_new = str(xml_element_tree_new, encoding='utf-8')
#     # print(xml_element_tree_new)

#     xml_element_tree_new = xml_element_tree_new.replace(':', '_')
#     xml_result_new = xml_element_tree_new.replace(' version="1.0"', '')

#     fp = open(f'{today}_xml_merge_new.xml', 'w')
#     fp.write(xml_result_new)
#     fp.close()

# #get f'{today}_xml_out.txt'
# tree = ET.parse(f'{today}_xml_merge_new.xml')
# root = tree.getroot()
# path_out = f'{today}_xml_out.txt'
# f = open(path_out, 'w')
# for child0 in root:
#     for child1 in child0:
#         for child2 in child1:
#             print(child2.tag) 
#             f.write(child2.tag + '\n') 
# f.close()

# #根據合併後的xml, 抓取要排除的tag
# tree = ET.parse(f'{today}_xml_merge_new.xml')
# root = tree.getroot()
# path_out = f'{today}_xml_out.txt'
# f = open(path_out, 'w')
# f.write(root[0][0][0].tag + '\n') #ARCHIVE_INDEX
# f.write(root[0][0][1].tag + '\n') #ARCHIVE_INDEX_TAB
# f.write(root[0][0][2].tag + '\n') #ARCHIVE_PARAMETERS
# f.write(root[0][0][3].tag + '\n') #CONTROL_PARAMETERS
# f.write(root[0][0][4].tag + '\n') #MAIL_APPL_OBJ
# f.write(root[0][0][5].tag + '\n') #MAIL_RECIPIENT
# f.write(root[0][0][6].tag + '\n') #MAIL_SENDER
# f.write(root[0][0][7].tag + '\n') #OUTPUT_OPTIONS
# f.write(root[0][0][8].tag + '\n') #USER_SETTINGS
# # f.write(root[0][0][9].tag + '\n') #PWB_DATA
# f.write(root[0][0][10].tag + '\n') #JOB_OUTPUT_INFO

# f.close()

#根據合併後的xml, 抓取useful tag
# tree = ET.parse(f'{today}_xml_merge_new.xml')
# root = tree.getroot()

# path_in = f'{today}_xml_in.txt'
# f = open(path_in, 'w')
# f.write(root[0][0].tag + '\n') #ns0_values
# f.write(root[0][0][9].tag + '\n') #PWB_DATA
# f.write(root[0][0][9][0].tag + '\n') #WA_CORR_HEAD in PWB_DATA
# f.write(root[0][0][9][0][3].tag + '\n') #SEARCH_TAGS
# f.write(root[0][0][9][0][4].tag + '\n') #REPRINT_KEY_IDENTIFIER
# f.write(root[0][0][9][1].tag + '\n') #WA_CORR_KEY
# f.write(root[0][0][9][2].tag + '\n') #WA_RECEIVER
# f.write(root[0][0][9][3].tag + '\n') #WA_ADDR_TYPE
# f.write(root[0][0][9][4].tag + '\n') #WA_REC_ADRESS
# f.write(root[0][0][9][5].tag + '\n') #WA_CORR_TECH
# f.write(root[0][0][9][5][0].tag + '\n') #DISTRIBUTION_CHANNELS
# f.write(root[0][0][9][5][3].tag + '\n') #GW_NOTIFICATIONS
# f.write(root[0][0][9][5][4].tag + '\n') #SMP_NOTIFICATIONS
# f.write(root[0][0][9][5][5].tag + '\n') #CP_NOTIFICATIONS
# f.write(root[0][0][9][5][6].tag + '\n') #SMS_COMMUNICATIONS
# f.write(root[0][0][9][5][7].tag + '\n') #EMAIL_COMMUNICATIONS
# f.write(root[0][0][9][5][8].tag + '\n') #SERVICE_REQUEST
# f.write(root[0][0][9][5][9].tag + '\n') #BANK_AGENT_NOTIFICATION
# f.write(root[0][0][9][6].tag + '\n') #WA_CORR_RCPT
# f.write(root[0][0][9][6][28].tag + '\n') #WA_CORR_RCPT
# f.write(root[0][0][9][7].tag + '\n') #WA_CORR_TA_CO
# f.write(root[0][0][9][8].tag + '\n') #MA_REMARK
# f.write(root[0][0][9][9].tag + '\n') #<T_FIELD/>
# f.write(root[0][0][9][10].tag + '\n') #T_TA_COMPASS
# f.write(root[0][0][9][10][0].tag + '\n') #_-NSL_-CD_CORR_DUN_TA_COMPASS_S
# f.write(root[0][0][9][10][0][0].tag + '\n') #WA_TA_COMPASS
# f.close()

    
