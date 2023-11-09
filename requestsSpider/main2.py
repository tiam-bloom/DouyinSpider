# _*_ coding : UTF-8 _*_
# @Time : 2023/11/6 20:38
# @Auther : Tiam
# @File : main2
# @Project : DouyinSpider
import json
import os
import re
from urllib.parse import urlencode

import requests
from requestsSpider.tiktok_signature import (get_signature, generate_random_str)
from download.down import (save_video_batch)

cookies = {
    'ttwid': '1%7CF6oAfQ2-NDzH4Ma6NR_j4SEAmknHsh_jLTV2F1XAtUE%7C1699029194%7C57185f4dfeca5d3cde14a9b7a10b8a90d6863b3ba92f69834483945e16d9b8e4',
}


# MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz
def aweme_v1_web_aweme_post(sec_user_id, max_cursor='0', need_time_list='1'):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    ms_token = generate_random_str()
    params = (
        ('device_platform', 'webapp'),
        ('aid', '6383'),
        ('channel', 'channel_pc_web'),
        ('sec_user_id', sec_user_id),
        ('max_cursor', max_cursor),
        ('locate_query', 'false'),
        ('show_live_replay_strategy', '1'),
        ('need_time_list', need_time_list),
        ('time_list_query', '0'),
        ('whale_cut_token', ''),
        ('cut_version', '1'),
        ('count', '32'),  # 每次请求的数量
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
    encode_params = urlencode(params, safe='=')
    url = f'https://www.douyin.com/aweme/v1/web/aweme/post/?{encode_params}'
    # print("get_signature url: ", url)
    # 获取X-Bogus, ttwid, new_url
    result = get_signature(url, user_agent)
    if result is None or result['code'] != 200:
        print('get_signature error')
        return
    # print(json.dumps(result, indent=2, ensure_ascii=False))
    result_data = result['data']
    ttwid = result_data['ttwid']
    new_url = result_data['url']
    # 将参数添加到元祖
    # xbogus = result_data['xbogus']
    # params += (('X-Bogus', xbogus),)
    # 替换msToken
    # params = tuple(map(lambda x: ('msToken', ms_token) if x[0] == 'msToken' else x, params))
    # encode_params = urlencode(params, safe='=')
    # print(encode_params)
    # response = requests.get(f'https://www.douyin.com/aweme/v1/web/aweme/post/?{encode_params}', headers=headers)

    headers = {
        'referer': f'https://www.douyin.com/user/{sec_user_id}',
        'user-agent': user_agent,
        'cookie': f'ttwid=1%7CF6oAfQ2-NDzH4Ma6NR_j4SEAmknHsh_jLTV2F1XAtUE%7C1699029194%7C57185f4dfeca5d3cde14a9b7a10b8a90d6863b3ba92f69834483945e16d9b8e4; '
    }
    print("new_url: ", new_url)
    response = requests.get(new_url, headers=headers)
    print(response.status_code)
    print(len(response.text))
    if response.status_code == 200 and len(response.text) > 0:
        with open('../data/test.main2.json', 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, indent=2, ensure_ascii=False)
        return response.json()


def save_user_video_page(sec_user_id):
    # 统计视频数量
    video_counts = 0
    max_cursor = '0'
    need_time_list = '1'
    while True:
        res = aweme_v1_web_aweme_post(sec_user_id, max_cursor, need_time_list)
        if res is None:
            print('aweme_v1_web_aweme_post error')
            return
        has_more = res['has_more']
        aweme_list = res['aweme_list']
        video_counts += len(aweme_list)
        print('本次请求到的视频数量:', len(aweme_list))
        # 处理数据
        save_video_batch(res, f'../data/{sec_user_id}/')
        if not os.path.exists(f'../data/{sec_user_id}-json/'):
            os.makedirs(f'../data/{sec_user_id}-json/')
        with open(f'../data/{sec_user_id}-json/{max_cursor}.json', 'w', encoding='utf-8') as f:
            json.dump(res, f, indent=2, ensure_ascii=False)

        if has_more == 0:
            print('没有更多了')
            break
        max_cursor = str(res['max_cursor'])
        need_time_list = '0'
    print('视频总数:', video_counts)


def save_user_video(url):
    # 获取sec_user_id
    sec_user_id = url.split('/')[-1]
    save_user_video_page(sec_user_id)


def main():
    # 获取用户输入
    print(
        "请输入用户主页链接, 比如: https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz")
    while True:
        url = input('请在此后粘贴链接(输入q退出):')
        # 检查输入
        if url is None or len(url) == 0:
            print('输入为空, 请重新输入')
        # 正则匹配
        elif re.fullmatch(r"https://www.douyin.com/user/[\w-]+", url, flags=0) is None:
            print('输入格式错误, 请不要携带参数等')
        elif url == 'q':
            print('退出')
            exit(0)
        else:
            break
    save_user_video(url)


def test():
    save_user_video(
        'https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz')


# test()
main()