TodayTweet
====
Twitterに今日はなんの日かをツイートしてくれるプログラム

## Description
wikiAPIから今日起こった誕生日や事件等々を受取り、ランダムでツイッターにツイートするプログラム

## Demo
```bash
$ python TodayTweet_main.py 3月12日
```

## Requirement
* python3系
* 必要なパッケージ
    ```
    twitter
    twitter
    ```

## Usage
* TwitterAPIを取得し,tweet.pyにAPI情報を入力
    ```python
    consumerKey = "consumerKey"
    consumerSecret = "consumerSecret"
    accessToken = "accessToken"
    accessSecret = "accessSecret"
    ```

## Install
* python TodayTweet_main.py

    今日行った出来事を取得してツイート

* python TodayTweet_main.py 3月12日

    引数で与えた日付に起こった出来事をツイート

* 今日はなんの日かを格納しているデータは'day_data'というディレクトに保存されます.

## Licence
This software is released under the MIT License, see LICENSE.

## Author
[Twitter](https://twitter.com/momijinn_aka)

[Blog](http://www.autumn-color.com/)