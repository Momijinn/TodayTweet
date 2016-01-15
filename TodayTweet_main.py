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

argv = sys.argv
argc = len(argv)

if argc == 2:
    argv = argv[1]
    pass
else:
    argv = '%s月%s日' % (datetime.datetime.today().month, datetime.datetime.today().day)
    pass

#一時間ごとにURLを参照しては失礼なので、同じファイルがあったら参照しない
if not(glob.glob(argv)):
    today.main(argv)
    pass

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
        break
        pass
    pass

now_tweet = argv + 'の' + topic_line + '\n' + line
print (now_tweet)

tweet.main(now_tweet)