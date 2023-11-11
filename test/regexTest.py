# _*_ coding : UTF-8 _*_
# @Time : 2023/11/10 10:16
# @Auther : Tiam
# @File : regexTest
# @Project : DouyinSpider

import re

# https://www.douyin.com/user/MS4wLjABAAAAEsFCZkCJwsJPiwqQbcYw3DPklVb0B2X9ZPt5KVWl7dE?enter_from=author_card&from_gid=7299437074703256841&tab_name=recommend&vid=7299437074703256841
# https://www.douyin.com/user/MS4wLjABAAAABHH6yC5Niqrc3qRWiKVlmyKF3vxIe_sUfzrdEDn4LMNZKbr7vL3ycfXOoYWNEiIV

# regex = re.compile(r'https://www.douyin.com/user/[w-]+')
# url = 'https://www.douyin.com/user/MS4wLjABAAAABHH6yC5Niqrc3qRWiKVlmyKF3vxIe_sUfzrdEDn4LMNZKbr7vL3ycfXOoYWNEiIV'
# url1 = 'https://www.douyin.com/user1/MS4wLjABAAAAEsFCZkCJwsJPiwqQbcYw3DPklVb0B2X9ZPt5KVWl7dE?enter_from=author_card&from_gid=7299437074703256841&tab_name=recommend&vid=7299437074703256841'
#
#
# res = re.search(r'(?<=https://www.douyin.com/user/)[\w-]+', url1)
# print(res)
# print(res.group())

file_name = '/.鞠婧\n祎/'
file_name = (file_name.replace('/', '').replace('\\', '').replace(':', '')
             .replace('*', '').replace('?', '').replace('.', ''))
print(file_name)
file_name = re.sub(r'\s', '', file_name)
print(file_name)

print(
    "请输入用户主页链接, 比如: https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz")
while True:
    url = input('请在此后粘贴链接(输入q退出):')
    if url == 'q':
        print('退出')
        exit(0)
    else:
        break
print('输入正确, 开始下载', url)