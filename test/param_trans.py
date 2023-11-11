# _*_ coding : UTF-8 _*_
# @Time : 2023/11/5 15:15
# @Auther : Tiam
# @File : param_trans
# @Project : DouyinSpider

import requests
from urllib.parse import quote

print(1 if 1 > 0 else 0)

url = "https://example.com/api"
params = {"key": "value with = sign"}

# 使用quote()函数对参数进行编码
encoded_params = {k: quote(v) for k, v in params.items()}

print(encoded_params)
