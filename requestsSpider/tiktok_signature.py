# _*_ coding : UTF-8 _*_
# @Time : 2023/11/5 16:33
# @Auther : Tiam
# @File : tiktok_signature
# @Project : DouyinSpider
# @Desc : 参考https://github.com/5ime/Tiktok_Signature, 自动生成抖音 xbogus、mstoken 和 ttwid。
# 本地接口: post https://tiktok.signature.yujing.icu/
import json
import random
from urllib.parse import urlencode

import requests


def get_signature(url, user_agent):
    """
    获取抖音的 xbogus、mstoken 和 ttwid
    :param user_agent:
    :param url: 抖音分享链接
    :return: xbogus、mstoken 和 ttwid
    """
    data = {
        "url": url,
        "userAgent": user_agent
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post('https://tiktok.signature.yujing.icu/', headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        return None


def generate_random_str(random_length=107):
    """
    根据传入长度产生随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789='
    length = len(base_str) - 1
    for _ in range(random_length):
        random_str += base_str[random.randint(0, length)]
    return random_str


# test
def test():
    params = (
        ('device_platform', 'webapp'),  # 设备平台
        ('aid', '6383'),  # 应用id
        ('channel', 'channel_pc_web'),  # 渠道
        ('sec_user_id', 'MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz'),  # 用户id
        ('max_cursor', '0'),  # 最大游标
        ('locate_query', 'false'),  # 定位查询
        ('show_live_replay_strategy', '1'),  # 显示直播重播策略
        ('need_time_list', '1'),  # 是否需要时间列表
        ('time_list_query', '0'),  # 时间列表查询
        ('whale_cut_token', ''),  # 鲸鱼切割令牌
        ('cut_version', '1'),  # 切割版本
        ('count', '64'),  # 查询数量
        ('publish_video_strategy_type', '2'),  # 发布视频策略类型
        ('pc_client_type', '1'),  # pc客户端类型
        ('version_code', '170400'),  # 版本代码
        ('version_name', '17.4.0'),  # 版本名称
        ('cookie_enabled', 'true'),  # cookie是否启用
        ('screen_width', '1707'),  # 屏幕宽度
        ('screen_height', '1067'),  # 屏幕高度
        ('browser_language', 'zh-CN'),  # 浏览器语言
        ('browser_platform', 'Win32'),  # 浏览器平台
        ('browser_name', 'Edge'),  # 浏览器名称
        ('browser_version', '119.0.0.0'),  # 浏览器版本
        ('browser_online', 'true'),  # 浏览器是否在线
        ('engine_name', 'Blink'),  # 引擎名称
        ('engine_version', '119.0.0.0'),  # 引擎版本
        ('os_name', 'Windows'),  # 操作系统名称
        ('os_version', '10'),  # 操作系统版本
        ('cpu_core_num', '16'),  # cpu核心数
        ('device_memory', '8'),  # 设备内存
        ('platform', 'PC'),  # 平台
        ('downlink', '10'),  # 下载链接
        ('effective_type', '4g'),  # 有效类型
        ('round_trip_time', '50'),  # 往返时间
        ('webid', '7297499797400897065'),  # 网页id
        ('msToken',
         'I4AhuILPeb_qvbcik9wB4Y6PcehDtcmVU1tL7GXf8g3CVmT_hs2zeayCHW7T8pidQU1-dwVDybEmCn0KB_F-idTdxseFSA8n_MG0a79UPhGJCjoTtm3IDTLDDtoI_9Pphg=='),
        # msToken
        ('X-Bogus', 'DFSzswVOy3tANGzZtFMCjfNSwbFE'),  # X-Bogus
    )
    encode_params = urlencode(params, safe='=')
    url = f'https://www.douyin.com/aweme/v1/web/aweme/post/?{encode_params}'
    print(url)
    # result = get_signature(url)
    # print(json.dumps(result, indent=2, ensure_ascii=False))
    # print(result['data']['url'])
    #
    # print("msToken:", generate_random_str())

"""
    输出
    "data": {
        "xbogus": "DFSzswSLhsvANc4HtF/vgt9WcBj4",  
        "mstoken": "SxJqbqNdWa8hHa3vayAEmRSyotyTcgweIQJ5XDrNHgOpJC8HPQTxFcyRFDFxs0nnG7OFFX6FBNoY3IHFiPMIneOQEQZcJRI4aSpZadxSICm",
        "ttwid": "1%7CamdZgzG1KjwQYohZsQpam6JrrYL6FadEr6jwtFm3UzM%7C1699173757%7C665320913fa9cafbce7577d4c538b4ca6ea24e9c9abb79cef9e682a3bc045ede",   # header的cookie中替换
        "url": "https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=36&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2560&screen_height=1440&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7297274756444276239&msToken=LvUPiShgy7Q4Hi1U-QA9W-Y603GT8B8zH5NZwfL8hFFhMWvnrIXMvnEMKSJmXbabMt39bDj3bREfCxkbiuseLg0w9hOgMoUfSfzveEuhk-JW9-eCQ9NLVN30Mmd9gJI=&X-Bogus=DFSzswVYqXkANCMrtFQrGBt/pLfc&X-Bogus=DFSzswSLhsvANc4HtF/vgt9WcBj4"
    }
"""
