'''
当使用 exitwp 生成 md 文件时, 文件名会乱码, 使用该脚本可以修复
'''
# -*- coding: utf-8 -*-
import re
import urllib
import os


files=os.listdir('C:/Users/Administrator/Desktop/exitwp-master/build/jekyll/www.smallcpp.cn/_posts')
for file in files:
    if file != u'change_md_file_name.py':
        file_object = open(file)
        all_the_text = file_object.read( )
        header = re.search('''---(.*?)---''', all_the_text, re.S)
        slug = re.search('''slug: (.*?)title''', header.group(1), re.S)
        new = urllib.unquote(slug.group(1)).replace('\n', '').decode('utf-8')
        file_object.close()

        os.renames(file, new + '.markdown')
