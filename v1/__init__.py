# _*_ coding : UTF-8 _*_
# @Time : 2023/11/7 9:59
# @Auther : Tiam
# @File : __init__.py
# @Project : DouyinSpider
import datetime
import json
import os
import re
from urllib.parse import urlencode

import requests
from v1.signature import Signature
from v1.downloader import Downloader


# import logging

# logging.basicConfig(level=logging.DEBUG)


class ReqUserAwemePost:
    base_url = 'https://www.douyin.com'
    post_url = '/aweme/v1/web/aweme/post/'
    url = base_url + post_url

    def __init__(self, sec_user_id):
        self.sec_user_id = sec_user_id
        self.downloader = Downloader(f'\\data\\{sec_user_id}/')

    def aweme_v1_web_aweme_post(self, max_cursor='0', need_time_list='1'):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        ms_token = Signature.gen_ms_token()
        params = (
            ('device_platform', 'webapp'),
            ('aid', '6383'),
            ('channel', 'channel_pc_web'),
            ('sec_user_id', self.sec_user_id),
            ('max_cursor', max_cursor),
            ('locate_query', 'false'),
            ('show_live_replay_strategy', '1'),
            ('need_time_list', need_time_list),
            ('time_list_query', '0'),
            ('whale_cut_token', ''),
            ('cut_version', '1'),
            ('count', '12'),  # 每次请求的数量
            ('publish_video_strategy_type', '2'),
            ('pc_client_type', '1'),
            ('version_code', '170400'),
            ('version_name', '17.4.0'),
            ('cookie_enabled', 'true'),
            ('screen_width', '2560'),
            ('screen_height', '1440'),
            ('browser_language', 'zh-CN'),
            ('browser_platform', 'Win32'),
            ('browser_name', 'Chrome'),
            ('browser_version', '119.0.0.0'),
            ('browser_online', 'true'),
            ('engine_name', 'Blink'),
            ('engine_version', '119.0.0.0'),
            ('os_name', 'Windows'),
            ('os_version', '10'),
            ('cpu_core_num', '16'),
            ('device_memory', '8'),
            ('platform', 'PC'),
            ('downlink', '10'),
            ('effective_type', '4g'),
            ('round_trip_time', '50'),
            ('webid', '7297274756444276239'),
            ('msToken', ms_token)
        )
        encode_params = urlencode(params, safe='=')  # safe='=' 保留等号, 避免被编码为%3D
        url = f'{ReqUserAwemePost.url}?{encode_params}'
        # 加密url等生成xbogus
        xbogus = Signature.gen_xbogus(url, user_agent)
        # 貌似不需要ttwid, 减少一次请求
        # ttwid = Signature.gen_ttwid()
        new_url = url + f'&X-Bogus={xbogus}'
        headers = {
            'referer': f'{ReqUserAwemePost.base_url}/user/{self.sec_user_id}',
            'user-agent': user_agent,
            'cookie': f'ttwid=1%7CF6oAfQ2-NDzH4Ma6NR_j4SEAmknHsh_jLTV2F1XAtUE%7C1699029194%7C57185f4dfeca5d3cde14a9b7a10b8a90d6863b3ba92f69834483945e16d9b8e4; '
        }
        print('本次请求url: ', new_url)
        response = requests.get(new_url, headers=headers)
        print('本次请求状态码: ', response.status_code, '返回数据长度: ', len(response.text))

        if response.status_code == 200 and len(response.text) > 0:
            # 保存json文件做备份
            date = datetime.datetime.fromtimestamp(int(max_cursor) / 1000).strftime('%Y-%m-%d')
            self.downloader.save_json_file(response.json(), date)
            return response.json()

    def req_user_aweme_post(self):
        # 统计视频数量
        video_counts = 0
        max_cursor = '0'
        need_time_list = '1'
        user_aweme_post_json_list = []
        while True:
            res = self.aweme_v1_web_aweme_post(max_cursor, need_time_list)
            if res is None:
                print('aweme_v1_web_aweme_post error')
                return
            has_more = res['has_more']
            aweme_list = res['aweme_list']
            video_counts += len(aweme_list)
            print('本次请求到的视频数量:', len(aweme_list))
            # todo 处理数据
            user_aweme_post_json_list.append(res)
            # self.downloader.save_video_batch(res)

            if has_more == 0:
                print('没有更多了')
                break
            max_cursor = str(res['max_cursor'])
            need_time_list = '0'
        print('视频总数: ', video_counts)
        return user_aweme_post_json_list


def save_user_video(sec_user_id):
    # 获取sec_user_id
    req = ReqUserAwemePost(sec_user_id)
    post_json_list = req.req_user_aweme_post()
    # 保存视频
    downloader_ = Downloader(f'\\data\\{sec_user_id}\\')
    need = 20
    index = 0
    for post_json in post_json_list:
        index += 1
        if index > need:
            break
        downloader_.save_video_batch(post_json)
    print('---------------统计-----------------')
    print("共下载视频次数", Downloader.all_counts)
    print("失败次数", Downloader.err_counts)


def main():
    # 获取用户输入 todo 优化输入
    print(
        "请输入用户主页链接, 比如: https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz")
    while True:
        url = input('请在此后粘贴链接(输入q退出):')
        # 检查输入
        if url is None or len(url) == 0:
            print('输入为空, 请重新输入')
        elif url == 'q':
            print('退出')
            exit(0)
        # 正则匹配
        elif re.search(r'(?<=https://www.douyin.com/user/)[\w-]+', url) is None:
            print(r'输入格式错误, 格式应匹配正则: (?<=https://www.douyin.com/user/)[\w-]+ 可匹配到sec_user_id')
        else:
            break
    sec_user_id = re.search(r'(?<=https://www.douyin.com/user/)[\w-]+', url).group()
    print('输入正确, 开始下载', sec_user_id)
    save_user_video(sec_user_id)


main()
