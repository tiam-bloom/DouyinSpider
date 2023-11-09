# _*_ coding : UTF-8 _*_
# @Time : 2023/11/5 0:16
# @Auther : Tiam
# @File : aweme_post
# @Project : DouyinSpider
import json

import requests

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'ttwid=1%7CF6oAfQ2-NDzH4Ma6NR_j4SEAmknHsh_jLTV2F1XAtUE%7C1699029194%7C57185f4dfeca5d3cde14a9b7a10b8a90d6863b3ba92f69834483945e16d9b8e4; passport_csrf_token=2ed8b3a4b7aa3443b8f7928cf978943a; passport_csrf_token_default=2ed8b3a4b7aa3443b8f7928cf978943a; strategyABtestKey=%221699029199.562%22; s_v_web_id=verify_loiu48q9_an0x42iY_FAk4_4I2J_9AoQ_njSOtDPwIkau; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.532%7D; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; download_guide=%223%2F20231104%2F0%22; webcast_local_quality=null; pwa2=%220%7C0%7C3%7C0%22; my_rd=2; csrf_session_id=42625dddd880a0e9a82209dbb6ca1bc9; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; xgplayer_user_id=343323172406; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1699710259489%2C%22type%22%3A1%7D; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2560%2C%5C%22screen_height%5C%22%3A1440%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSndteGk4WTZkcjJmRFVxeVN1a0gzZkVzOTJPZUgxZHhyQVllcGNocTJBVWFpRVdCVlIyeUF6TGNsVmJCVzI3WTlBN2kxUWdZQVZNZjVId3B6c3pUc2c9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; tt_scid=ypC6qi1OkviE1tjQGqvnHKV-6O3-zkW3ZnsK7hY2Awiokh61NVPzzdsMuKc1zbNgf11a; msToken=LMrUEfQGvTgnII-6rI_OmpEaRxeTbVEhxSZ0KEp92as0k9fyRQJNnD46P98yrrI1dX9SvQZKZPIW7AMTsRN0mnH7oYlRJev5bvyGkV2C754zHRaYCm9rmJ8Z46ZjKVo=; msToken=LvUPiShgy7Q4Hi1U-QA9W-Y603GT8B8zH5NZwfL8hFFhMWvnrIXMvnEMKSJmXbabMt39bDj3bREfCxkbiuseLg0w9hOgMoUfSfzveEuhk-JW9-eCQ9NLVN30Mmd9gJI=; __ac_nonce=065467786004185591f74; __ac_signature=_02B4Z6wo00f01sPYOawAAIDDSJOiTWu3TZbD-D0AANW90mPk4OVnyA2Zn9eOWL923WN4-HUE-rWeI5.Aofj67VTkuo3usXEdVzEa4xyZl8zjh6yLKFVWEGJmq9BaohcH7HxqXou3EwNpD2Ged6; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22',
    'pragma': 'no-cache',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

params = (
    ('device_platform', 'webapp'),
    ('aid', '6383'),
    ('channel', 'channel_pc_web'),
    ('sec_user_id', 'MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz'),
    ('max_cursor', '0'),
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
    ('msToken', 'LvUPiShgy7Q4Hi1U-QA9W-Y603GT8B8zH5NZwfL8hFFhMWvnrIXMvnEMKSJmXbabMt39bDj3bREfCxkbiuseLg0w9hOgMoUfSfzveEuhk-JW9-eCQ9NLVN30Mmd9gJI='),
    ('X-Bogus', 'DFSzswVYqXkANCMrtFQrGBt/pLfc'),
)

# response = requests.get('https://www.douyin.com/aweme/v1/web/aweme/post/', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
response = requests.get('https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2560&screen_height=1440&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7297274756444276239&msToken=LvUPiShgy7Q4Hi1U-QA9W-Y603GT8B8zH5NZwfL8hFFhMWvnrIXMvnEMKSJmXbabMt39bDj3bREfCxkbiuseLg0w9hOgMoUfSfzveEuhk-JW9-eCQ9NLVN30Mmd9gJI=&X-Bogus=DFSzswVYqXkANCMrtFQrGBt/pLfc', headers=headers)


print(response.status_code)
with open('../data/aweme_post.test.json', 'w', encoding='utf-8') as f:
    json_data = response.json()
    # 格式化写入
    json.dump(json_data, f, ensure_ascii=False, indent=2)

