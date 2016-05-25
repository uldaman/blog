# -*- coding: utf-8 -*-
'''
当使用 make html 生成 html 文件, 文件名乱码, 使用该脚本可以修复
'''
import re
import urllib
import os


files=os.listdir('C:/Users/Administrator/Desktop/123')
for file in files:
    if file != 'change_hml_file_name.py':
        new = urllib.unquote(file).replace('\r', '').replace('\n', '')
        print new
        os.renames(file, new.decode('utf-8'))
