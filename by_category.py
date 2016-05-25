# -*- coding: utf-8 -*-
'''
读取文件中的 Category, 然后将文件放到 Category 指定的文件夹
'''
import re
import urllib
import os
import shutil


files=os.listdir('C:/Users/Administrator/Desktop/content')
for file in files:
    file = file.decode('gbk').encode('utf-8')
    if file != 'sss.py':
        file_object = open(file.decode('utf-8').encode('gbk'))
        lnum = 0
        for line in file_object:
                lnum += 1
                if lnum == 5:
                    result = re.search('''Category: (.*?)\n''', line, re.S)
                    tar = 'C:/Users/Administrator/Desktop/field/' + result.group(1)
                    shutil.copy(file.decode('utf-8').encode('gbk'),  tar.decode('utf-8').encode('gbk'))
                    break
        file_object.close()
