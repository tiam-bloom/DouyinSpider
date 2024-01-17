# _*_ coding : UTF-8 _*_
# @Time : 2024/1/16 13:29
# @Auther : Tiam
# @File : first_page
# @Project : DouyinSpider
# @Desc :

import requests

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
    ('max_cursor', '0'),
    ('locate_item_id', '7313558967433694498'),
    ('locate_query', 'false'),
    ('show_live_replay_strategy', '1'),
    ('need_time_list', '1'),
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
    ('msToken', 'NU1zSDESvDm4EfxMiA2oBiz25Bq3AwYEVHMiFT5AcPZNx7PnCLxbCFS3ZsN_y4utTXRDANiNl7Tjbm9E9VK73pnRjl4tTmGQegqD-Sqnp5QsSnSzjw3ZhuxomcKdvYtvgBA='),
    ('X-Bogus', 'DFSzswVYXNhANJpsti1Zo7O3H84P'),
)

# response = requests.get('https://www.douyin.com/aweme/v1/web/aweme/post/', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
response = requests.get('https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAArcoz8pyUJSASISQnP_JMfUgNATaCTOJJzQsG6HSzeAU&max_cursor=0&locate_item_id=7313558967433694498&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=1067&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7297962636765939237&msToken=NU1zSDESvDm4EfxMiA2oBiz25Bq3AwYEVHMiFT5AcPZNx7PnCLxbCFS3ZsN_y4utTXRDANiNl7Tjbm9E9VK73pnRjl4tTmGQegqD-Sqnp5QsSnSzjw3ZhuxomcKdvYtvgBA=&X-Bogus=DFSzswVYXNhANJpsti1Zo7O3H84P', headers=headers, cookies=cookies)
print(response.text)
