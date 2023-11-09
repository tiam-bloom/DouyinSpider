# _*_ coding : UTF-8 _*_
# @Time : 2023/11/7 11:19
# @Auther : Tiam
# @File : __init__.py
# @Project : DouyinSpider
import random
import re

import execjs
from urllib.parse import urlparse

import requests
# import logging
import os

# logger = logging.getLogger(__name__)


def gen_random_str(random_length):
    """
            根据传入长度产生随机字符串
            """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789='
    length = len(base_str) - 1
    for _ in range(random_length):
        random_str += base_str[random.randint(0, length)]
    return random_str


class Signature:
    # 这里Cookie指的一提的是msToken可以是随机107位大小写英文字母、数字生成的字符串; 参考: https://github.com/B1gM8c/X-Bogus
    @staticmethod
    def gen_ms_token():
        return gen_random_str(107)

    @staticmethod
    def gen_xbogus(url, user_agent):
        # 解析url参数
        query = urlparse(url).query
        # js算法加密生成 X-bogus, 执行js文件中的sign方法
        # os.getcwd() 可以获取当前python程序的工作目录, 使用相对路径是相对的当前工作目录, 并不是相对于当前文件

        path = os.path.dirname(__file__) + '\\X-Bogus.js'
        return execjs.compile(open(path).read()).call('sign', query, user_agent)

    @staticmethod
    def gen_ttwid():
        url = 'https://ttwid.bytedance.com/ttwid/union/register/'
        data = {
            "region": "cn",
            "aid": 1768,
            "needFid": False,
            "service": "www.ixigua.com",
            "migrate_info": {"ticket": "", "source": "node"},
            "cbUrlProtocol": "https",
            "union": True
        }
        response = requests.post(url, json=data)
        set_cookie = response.headers['set-cookie']
        # print(set_cookie.split(';'))
        regex = r'ttwid=([^;]+)'
        match = re.search(regex, set_cookie)
        return match.group(1) if match else ''


def test():
    url = 'https://www.ixigua.com/i6768216128099698187/'
    user_agent = 'Mozilla/5.0 (Linux; Android 10; Redmi K30 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'
    print(Signature.gen_xbogus(url, user_agent))
    print(Signature.gen_ms_token())
    print(Signature.gen_ttwid())

# test()
