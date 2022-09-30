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
# file_path = filedialog.askdirectory(title='Please choose old file')

file_path = './xml_old_original'
# dirlist_csv_old = os.listdir(path_csv_old)
# print(file_path)

xml_files_old = glob.glob(file_path + '\*.*')


#抓取old xml fild, all data 

# print(xml_files_old)
xml_element_tree_old = None

#多的xml合併成一個
for xml_file_old in xml_files_old:
    print(xml_file_old)

    # parser = ElementTree.XMLParser(encoding = "iso-8859-1")
    # data = ElementTree.parse(xml_file_old, parser)
    xml_file_old = xml_file_old.replace(u'\uFFFD', "?")
    data = ElementTree.parse(xml_file_old).getroot()
    #print(ElementTree.tostring(data))
    for PWB_DATA in data.iter('sf'):
        if xml_element_tree_old is None:
            xml_element_tree_old = data 
            insertion_point_old = xml_element_tree_old.findall(".")[0]
        else:
            insertion_point_old.extend(PWB_DATA) 
if xml_element_tree_old is not None:
    #print(ElementTree.tostring(xml_element_tree))
    xml_element_tree_old = ElementTree.tostring(xml_element_tree_old)
    # print(xml_result)
    xml_element_tree_old = str(xml_element_tree_old, encoding='utf-8')
    # print(xml_element_tree_old)

    #取代
    xml_element_tree_old = xml_element_tree_old.replace(':', '_')
    xml_element_tree_old = xml_element_tree_old.replace(',', '')
    xml_result_old = xml_element_tree_old.replace(' version="1.0"', '')

    # 開啟檔案xml
    fp = open('./xml_merge_old.xml', 'w')
    # 寫入 This is a testing! 到檔案
    fp.write(xml_result_old)
    
    # 關閉檔案
    fp.close()



    
