# _*_ coding : UTF-8 _*_
# @Time : 2023/11/5 10:13
# @Auther : Tiam
# @File : msToken
# @Project : DouyinSpider


import requests
from urllib.parse import quote, urlencode

# from requestsSpider.models import CustomRequest

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'cookie': 'ttwid=1%7Cv0EmhqF7mzb-6LJHuETCVojHF1OKAlH08Zp5-Q3Grwc%7C1699081592%7C8247861b3903d6b67a3a90b5c14ac12840a726ddd670c5676672fa2bad3a5c00; passport_csrf_token=00439b952195a3d96bd95a61925743f9; passport_csrf_token_default=00439b952195a3d96bd95a61925743f9; s_v_web_id=verify_lojpbdh0_P8pHdE0z_ec8e_4CyC_8Ma7_4hHtFk7l8zOD; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; passport_assist_user=CjyYV_g3dBBKSK_8EQYJxmp2Sn1j7c1hYXsrtkc8U0tav1jAdqha8oxTdGGTTA_Lm-ttznDiljeLcsaNCvAaSgo8uM3J_VPlRJc65thXyhajCJr6wtwVZN8CL1b1zTzLFZ4MLD19SHbMCqcGLxiDmcD_RsOd7CEeep55j_6gELSwwA0Yia_WVCABIgEDXC3CeQ%3D%3D; n_mh=Cnh05CH1Mtmld1KnWiQ-4Gqbkf702lUnDliGiTaf92g; sso_uid_tt=dba9adee3ab771db0c832b04e955f3db; sso_uid_tt_ss=dba9adee3ab771db0c832b04e955f3db; toutiao_sso_user=318cded8a3d8f5e83d0ef5b162b09137; toutiao_sso_user_ss=318cded8a3d8f5e83d0ef5b162b09137; sid_ucp_sso_v1=1.0.0-KGIyZDhjMzlkMzQyNTM5NTUzYmZkODE4NGIxMmE0MmY5ZmVmMTk3NGIKHQiv7JuJiAIQwduXqgYY7zEgDDDKrr7OBTgGQPQHGgJsZiIgMzE4Y2RlZDhhM2Q4ZjVlODNkMGVmNWIxNjJiMDkxMzc; ssid_ucp_sso_v1=1.0.0-KGIyZDhjMzlkMzQyNTM5NTUzYmZkODE4NGIxMmE0MmY5ZmVmMTk3NGIKHQiv7JuJiAIQwduXqgYY7zEgDDDKrr7OBTgGQPQHGgJsZiIgMzE4Y2RlZDhhM2Q4ZjVlODNkMGVmNWIxNjJiMDkxMzc; passport_auth_status=166b61dc31a8ef0c6dd6055d03941cb2%2C; passport_auth_status_ss=166b61dc31a8ef0c6dd6055d03941cb2%2C; uid_tt=9f0500255ccfb09453e2590e7de659f6; uid_tt_ss=9f0500255ccfb09453e2590e7de659f6; sid_tt=f73bbdf4d086d39742d21042ae244799; sessionid=f73bbdf4d086d39742d21042ae244799; sessionid_ss=f73bbdf4d086d39742d21042ae244799; publish_badge_show_info=%220%2C0%2C0%2C1699081677005%22; LOGIN_STATUS=1; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=a2fd0167087d25ed969a7ff19da3b136; __security_server_data_status=1; sid_guard=f73bbdf4d086d39742d21042ae244799%7C1699081676%7C5183992%7CWed%2C+03-Jan-2024+07%3A07%3A48+GMT; sid_ucp_v1=1.0.0-KDJkNDYzODFhZDE3MzI1ZmM2M2I5MDZjNmUwMmIyYTRmMDA0NmJkZjAKGQiv7JuJiAIQzNuXqgYY7zEgDDgGQPQHSAQaAmxmIiBmNzNiYmRmNGQwODZkMzk3NDJkMjEwNDJhZTI0NDc5OQ; ssid_ucp_v1=1.0.0-KDJkNDYzODFhZDE3MzI1ZmM2M2I5MDZjNmUwMmIyYTRmMDA0NmJkZjAKGQiv7JuJiAIQzNuXqgYY7zEgDDgGQPQHSAQaAmxmIiBmNzNiYmRmNGQwODZkMzk3NDJkMjEwNDJhZTI0NDc5OQ; my_rd=2; download_guide=%223%2F20231104%2F0%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.443%7D; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1699697308648%2C%22type%22%3A1%7D; SEARCH_RESULT_LIST_TYPE=%22single%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; pwa2=%220%7C0%7C3%7C0%22; webcast_local_quality=origin; strategyABtestKey=%221699152407.011%22; store-region=cn-hb; store-region-src=uid; csrf_session_id=bf24502cdf299f7e407151b53865676e; FRIEND_NUMBER_RED_POINT_INFO=%22MS4wLjABAAAAH7XG2XkvkQq8SuAJbN-Km4ecPpyZ3pUI1Yokfw9AWmk%2F1699200000000%2F1699152592850%2F0%2F0%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAH7XG2XkvkQq8SuAJbN-Km4ecPpyZ3pUI1Yokfw9AWmk%2F1699200000000%2F1699152608994%2F1699152426547%2F0%22; passport_fe_beating_status=true; __ac_nonce=065473a750058826aa9cb; __ac_signature=_02B4Z6wo00f01qdk4fAAAIDB8uZqbkS1cRanROVAAMyqDC8encKQ7qBTdX-K8Vh5F4xs4GXaSQ1McYNvFyLDNjYLQqWjWqiK-IcUv.8evaqzYbD7h0BRGtk5KxlP7qzaNkLXgXgeXXwRCsLMb1; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAH7XG2XkvkQq8SuAJbN-Km4ecPpyZ3pUI1Yokfw9AWmk%2F1699200000000%2F0%2F1699166840623%2F0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQ1VZZGVEWjdpY2g2QW1TL1A0S0JTVXpOSnNtZHMwclNpRVV6UmlaUXA3Mkw2cFlNVEVuaHJ5c01LZXV5ekh5d0FLcE1nbnk5MTM4QndnZXlpMzhtalE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=I4AhuILPeb_qvbcik9wB4Y6PcehDtcmVU1tL7GXf8g3CVmT_hs2zeayCHW7T8pidQU1-dwVDybEmCn0KB_F-idTdxseFSA8n_MG0a79UPhGJCjoTtm3IDTLDDtoI_9Pphg==; msToken=yAr8lZ7e5X0kTN7NAILl4l1d1o4hehzW1E2Y_Y5cv7wJmBrB77Lm00PqrKkZDmOIlQhBtWQU4RbjBcANzh8efdn5Sfy6zLSPtWzgQU35yDab_i4xXeVp4wnw98wcEFfUVg==; tt_scid=ko9jKy16T4-LiaEJBFr-ONxPceeoRUke0hGBuhLqUAvcw18fQjNQ-rs4i9kjpUqG787b; odin_tt=bb08ea45328f5138299a6311d058035b388390067e05360bb90f4c57f0eb0850ae4f45c59c8cdff5a0412b1bd683e55bf8e3df8a1087bbba95b72c376f5050cf; IsDouyinActive=true; home_can_add_dy_2_desktop=%221%22',
    'pragma': 'no-cache',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}

msToken = 'I4AhuILPeb_qvbcik9wB4Y6PcehDtcmVU1tL7GXf8g3CVmT_hs2zeayCHW7T8pidQU1-dwVDybEmCn0KB_F-idTdxseFSA8n_MG0a79UPhGJCjoTtm3IDTLDDtoI_9Pphg=='

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
    ('screen_width', '1707'),
    ('screen_height', '1067'),
    ('browser_language', 'zh-CN'),
    ('browser_platform', 'Win32'),
    ('browser_name', 'Edge'),
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
    ('webid', '7297499797400897065'),
    ('msToken', msToken),  # = 会被转义为 %3D, 但是转义后的msToken无法被服务器识别
    ('X-Bogus', 'DFSzswVOy3tANGzZtFMCjfNSwbFE'),
)
# 如何避免参数==被转义为%3D
encode_params = urlencode(params, safe='=')
# print(encode_params)

# 使用params参数 "=" 会被转义为 %3D, 但是转义后的msToken无法被服务器识别, 这里使用拼接形式
response = requests.get(f'https://www.douyin.com/aweme/v1/web/aweme/post/?{encode_params}', headers=headers)

print(response.status_code)
print(response.text)
