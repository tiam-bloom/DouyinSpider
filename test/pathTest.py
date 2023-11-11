# _*_ coding : UTF-8 _*_
# @Time : 2023/11/11 19:44
# @Auther : Tiam
# @File : pathTest
# @Project : DouyinSpider
# @Desc :
import os

path = '../data/'
path1 = r"F:\Tiam\Desktop\JustPlay\Python\DouyinSpider\data"

hello = os.path.join(os.path.abspath(path1), 'hello\\test.txt')
print(hello.split(os.path.sep)[-1])
print(hello)
hello = os.path.dirname(path1)
print(hello)

# if not os.path.exists(hello):
#     os.makedirs(hello)