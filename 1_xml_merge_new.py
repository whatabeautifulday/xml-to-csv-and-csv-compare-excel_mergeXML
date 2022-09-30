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



    
