# -*- coding: utf-8 -*-
#!/usr/bin/env python
from twitter import *
import sys

def main(str_tweet):
  #OAuth ToolからもらえるKeyなどを入力
  consumerKey = "consumerKey"
  consumerSecret = "consumerSecret"
  accessToken = "accessToken"
  accessSecret = "accessSecret"

  t = Twitter(auth=OAuth(accessToken, accessSecret, consumerKey, consumerSecret))
  t.statuses.update(status= str_tweet)



if __name__ == '__main__':
  mes = sys.argv
  main(mes[1])
