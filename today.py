#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import datetime
import sys
import re
from lxml import etree
import os

def main(argv):
    #引数の処理
    if argv is None:
        argv = '%s月%s日' % (datetime.datetime.today().month, datetime.datetime.today().day)
        date = urllib.parse.quote(argv)
        pass
    else:
        if re.match(r'\d+月\d+日',argv):
            date = urllib.parse.quote(argv)
            pass
        else:
            print ("error!! [ example run:python today.py 4月13日 ]")
            sys.exit("Argument error #1")
            pass
        pass

    #urlの読み込み
    url = 'https://ja.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=xml&titles=' + date
    response = urllib.request.urlopen(url)
    html = response.read()


    #解析
    f = open('today_py_tmp','wb') #TypeError: write() argument must be str, not bytesの回避 ファイルをバイナリモードで開く
    tree = etree.fromstring(html)
    tag = tree.xpath('//rev')

    for txt in tag:
        textline = txt.text #stringを持ってくる

        textline = textline.replace('[[','')
        textline = textline.replace(']]','')
        textline = textline.replace('{{','{')
        textline = textline.replace('}}','}')
        textline = textline.replace('<!--','')
        textline = textline.replace('-->','')
        textline = textline.replace('<ref>',' <詳細>')
        textline = textline.replace('</ref>',' ')
        textline = textline.replace('　','')
        textline = textline.replace('http://',' http://')

        f.write(textline.encode('utf_8'))
        pass
    f.close()


    #さらに解析
    f = open('today_py_tmp', 'rb')
    f_lines = f.readlines()
    f.close()
    os.remove('today_py_tmp') #tmpファイルは削除

    r = open(argv, 'wb')
    for line in f_lines:
        #タイトルの摘出
        if re.search(r'== +\S+ ==', line.decode('utf-8')):
            if not(re.search('出典', line.decode('utf-8')) or re.search('関連項目', line.decode('utf-8'))
                or re.search('脚注', line.decode('utf-8')) or re.search('注釈', line.decode('utf-8'))):
                r.write(line)
                pass
            pass

        #何があったかの摘出
        elif line.decode('utf-8').startswith('*'):
            r.write(line)
            pass
        pass
    r.close()
    pass


if __name__ == '__main__':
    #テキトーに作ったお試しのもの
    argv = sys.argv
    argc = len(argv)

    if argc == 2:
        tmp = argv[1]
        main(argv[1])
        pass
    else:
        main(None)
        pass