#!/usr/bin/env python
# -*- coding: utf-8 -*-
import today
import tweet
import datetime
import random
import sys
import linecache
import re
import glob
import os
import shutil

#持ってきたファイルを保管するディレクトリ作成
day_dir = 'day_data'
if not(glob.glob(day_dir)):
    os.mkdir(day_dir)
    pass

argv = sys.argv
argc = len(argv)

if argc == 2:
    argv = argv[1]
    pass
else:
    argv = '%s月%s日' % (datetime.datetime.today().month, datetime.datetime.today().day)
    pass

#一時間ごとにURLを参照しては失礼なので、同じファイルがあったら参照しない
if not(glob.glob(day_dir + '/' + argv)):
    today.main(argv)
    shutil.move(argv, day_dir)
    pass

#ファイルディレクトリの書き換え
tweet_day = argv
argv = day_dir + '/' + argv

#乱数の生成
f = open(argv, 'rb')
line_cnt = sum(1 for line in f) #行数を取得
d = datetime.datetime.today()
random.seed(d.hour + d.second)
ran = random.randint(2,line_cnt)
f.close()

#一行読み出し
line = linecache.getline(argv,ran)

#もし乱数で見出しを引いてしまった時の処理
if re.search(r'== +\S+ ==', line):
    ran = ran - 2
    line = linecache.getline(argv,ran)
    pass
line = line.replace('*','')

#見出しを持ってくる
for i in reversed(range(ran)):
    topic_line = linecache.getline(argv,i)
    if re.search(r'== +\S+ ==', topic_line):
        topic_line = topic_line.replace('==','')
        topic_line = topic_line.replace(' ','')
        break
        pass
    pass

now_tweet = tweet_day + 'の' + topic_line + line
print (now_tweet)

tweet.main(now_tweet)