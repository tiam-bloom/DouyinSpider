# _*_ coding : UTF-8 _*_
# @Time : 2023/11/10 10:16
# @Auther : Tiam
# @File : regexTest
# @Project : DouyinSpider

import re

# https://www.douyin.com/user/MS4wLjABAAAAEsFCZkCJwsJPiwqQbcYw3DPklVb0B2X9ZPt5KVWl7dE?enter_from=author_card&from_gid=7299437074703256841&tab_name=recommend&vid=7299437074703256841
# https://www.douyin.com/user/MS4wLjABAAAABHH6yC5Niqrc3qRWiKVlmyKF3vxIe_sUfzrdEDn4LMNZKbr7vL3ycfXOoYWNEiIV

regex = re.compile(r'https://www.douyin.com/user/[w-]+')
url = 'https://www.douyin.com/user/MS4wLjABAAAABHH6yC5Niqrc3qRWiKVlmyKF3vxIe_sUfzrdEDn4LMNZKbr7vL3ycfXOoYWNEiIV'
url1 = 'https://www.douyin.com/user1/MS4wLjABAAAAEsFCZkCJwsJPiwqQbcYw3DPklVb0B2X9ZPt5KVWl7dE?enter_from=author_card&from_gid=7299437074703256841&tab_name=recommend&vid=7299437074703256841'


res = re.search(r'(?<=https://www.douyin.com/user/)[\w-]+', url1)
print(res)
print(res.group())
