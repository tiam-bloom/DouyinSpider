# _*_ coding : UTF-8 _*_
# @Time : 2024/1/16 13:38
# @Auther : Tiam
# @File : second_page
# @Project : DouyinSpider
# @Desc : 作品请求逻辑测试
from urllib.parse import urlencode, urlparse

import requests
from v2.signature import Signature

cookies = {
    'ttwid': '1%7C7bNwGzlfoxFk0M5A0Ga6bI7jLPpBWLVt2SlW9DnTa9g%7C1699288129%7Ce14c38d31876df442429e626286c276072f7a7a7b5ebe8abfe866fba1c3e950e',
}

headers = {
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAArcoz8pyUJSASISQnP_JMfUgNATaCTOJJzQsG6HSzeAU?vid=7313558967433694498',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
}

params = (
    ('device_platform', 'webapp'),
    ('aid', '6383'),
    ('channel', 'channel_pc_web'),
    ('sec_user_id', 'MS4wLjABAAAArcoz8pyUJSASISQnP_JMfUgNATaCTOJJzQsG6HSzeAU'),
    ('max_cursor', '1698760139000'),  # 第一页 => 0, 其他页 => 前一页返回的max_cursor字段; 第二页: 1702216896000, 第三页: 1698760139000
    # ('locate_item_id', '7313558967433694498'),  # 可选参数, 用于定位视频, 一般不用
    ('locate_query', 'false'),
    ('show_live_replay_strategy', '1'),
    ('need_time_list', '0'),   # 第一页 => 1, 其他页 => 0
    ('time_list_query', '0'),
    ('whale_cut_token', ''),
    ('cut_version', '1'),
    ('count', '18'),
    ('publish_video_strategy_type', '2'),
    ('pc_client_type', '1'),
    ('version_code', '170400'),
    ('version_name', '17.4.0'),
    ('cookie_enabled', 'true'),
    ('screen_width', '1707'),
    ('screen_height', '1067'),
    ('browser_language', 'zh-CN'),
    ('browser_platform', 'Win32'),
    ('browser_name', 'Edge'),
    ('browser_version', '120.0.0.0'),
    ('browser_online', 'true'),
    ('engine_name', 'Blink'),
    ('engine_version', '120.0.0.0'),
    ('os_name', 'Windows'),
    ('os_version', '10'),
    ('cpu_core_num', '16'),
    ('device_memory', '8'),
    ('platform', 'PC'),
    ('downlink', '10'),
    ('effective_type', '4g'),
    ('round_trip_time', '100'),
    ('webid', '7297962636765939237'),
    ('msToken', Signature.gen_ms_token()),
)
encode_params = urlencode(params, safe='=')
url = 'https://www.douyin.com/aweme/v1/web/aweme/post/?' + encode_params
# 生成 X-Bogus
xbogus = Signature.gen_xbogus(url, headers['user-agent'])
url = url + '&X-Bogus=' + xbogus
# 解析url参数
query = urlparse(url).query
print(query)

response = requests.get(url, headers=headers, cookies=cookies)

print(response.status_code)
if response.status_code != 200:
    print('请求失败')
    exit(0)
# 存入文件
with open('second_page.json', 'w', encoding='utf-8') as f:
    f.write(response.text)

