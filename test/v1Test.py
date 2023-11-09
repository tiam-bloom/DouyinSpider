# _*_ coding : UTF-8 _*_
# @Time : 2023/11/7 16:31
# @Auther : Tiam
# @File : v1Test
# @Project : DouyinSpider
import json
import unittest
from v1 import ReqUserAwemePost


class V1Test(unittest.TestCase):
    def test_req_user_aweme_post(self):
        sec_user_id = 'MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz'
        req = ReqUserAwemePost(sec_user_id)
        # 默认请求第一页
        json_data = req.aweme_v1_web_aweme_post()
        with open('/data/v1Test.json', 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)

