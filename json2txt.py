# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:20:15 2020

@author: 浩克
"""
import json
import numpy as np
import os
#json转txt


def json2txt(path_json, path_txt):
    with open(path_json, 'r') as path_json:
        jsonx = json.load(path_json)
        with open(path_txt, 'w+') as ftxt:
            for shape in jsonx['shapes']:
                xy = np.array(shape['points'])
                label = str(shape['label'])
                x1 = str(int(xy[0][0]))
                y1 = str(int(xy[0][1]))
                x2 = str(int(xy[1][0]))
                y2 = str(int(xy[1][1]))

                strxy = x1+','+y1+','+x2+','+y1+','+x2+','+y2+','+x1+','+y2
                # for m, n in xy:
                #     strxy += str(int(m)) + ',' + str(int(n)) + ','
                # strxy += label
                ftxt.writelines(strxy + "\n")

#json2txt(r"C:\Users\dell\Desktop\001.json", r'C:\Users\dell\Desktop\student_json2txt.txt')

dir_json = 'E:\dataset\Scan_CTPN\方玲玉\json/'
dir_txt = 'E:\dataset\Scan_CTPN\方玲玉/txt/'
if not os.path.exists(dir_txt):
    os.makedirs(dir_txt)
list_json = os.listdir(dir_json)
for cnt,json_name in enumerate(list_json):
    print('cnt=%d,name=%s'%(cnt,json_name))
    path_json = dir_json + json_name
    path_txt = dir_txt + json_name.replace('.json','.txt')
    #print(path_json,path_txt)
    json2txt(path_json,path_txt)

