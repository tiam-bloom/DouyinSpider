# _*_ coding : UTF-8 _*_
# @Time : 2023/11/7 12:46
# @Auther : Tiam
# @File : dateTest
# @Project : DouyinSpider


import datetime

cursor = 1693652827000

print(datetime.datetime.fromtimestamp(cursor / 1000).strftime('%Y-%m-%d'))
