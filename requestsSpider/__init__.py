# _*_ coding : UTF-8 _*_
# @Time : 2023/11/4 18:49
# @Auther : Tiam
# @File : __init__.py
# @Project : DouyinSpider
import json

import requests

def test():
    headers = {
        'authority': 'www.douyin.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'cookie': 'ttwid=1%7Cv0EmhqF7mzb-6LJHuETCVojHF1OKAlH08Zp5-Q3Grwc%7C1699081592%7C8247861b3903d6b67a3a90b5c14ac12840a726ddd670c5676672fa2bad3a5c00; webcast_local_quality=origin; passport_csrf_token=00439b952195a3d96bd95a61925743f9; passport_csrf_token_default=00439b952195a3d96bd95a61925743f9; strategyABtestKey=%221699081600.094%22; s_v_web_id=verify_lojpbdh0_P8pHdE0z_ec8e_4CyC_8Ma7_4hHtFk7l8zOD; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; passport_assist_user=CjyYV_g3dBBKSK_8EQYJxmp2Sn1j7c1hYXsrtkc8U0tav1jAdqha8oxTdGGTTA_Lm-ttznDiljeLcsaNCvAaSgo8uM3J_VPlRJc65thXyhajCJr6wtwVZN8CL1b1zTzLFZ4MLD19SHbMCqcGLxiDmcD_RsOd7CEeep55j_6gELSwwA0Yia_WVCABIgEDXC3CeQ%3D%3D; n_mh=Cnh05CH1Mtmld1KnWiQ-4Gqbkf702lUnDliGiTaf92g; sso_uid_tt=dba9adee3ab771db0c832b04e955f3db; sso_uid_tt_ss=dba9adee3ab771db0c832b04e955f3db; toutiao_sso_user=318cded8a3d8f5e83d0ef5b162b09137; toutiao_sso_user_ss=318cded8a3d8f5e83d0ef5b162b09137; sid_ucp_sso_v1=1.0.0-KGIyZDhjMzlkMzQyNTM5NTUzYmZkODE4NGIxMmE0MmY5ZmVmMTk3NGIKHQiv7JuJiAIQwduXqgYY7zEgDDDKrr7OBTgGQPQHGgJsZiIgMzE4Y2RlZDhhM2Q4ZjVlODNkMGVmNWIxNjJiMDkxMzc; ssid_ucp_sso_v1=1.0.0-KGIyZDhjMzlkMzQyNTM5NTUzYmZkODE4NGIxMmE0MmY5ZmVmMTk3NGIKHQiv7JuJiAIQwduXqgYY7zEgDDDKrr7OBTgGQPQHGgJsZiIgMzE4Y2RlZDhhM2Q4ZjVlODNkMGVmNWIxNjJiMDkxMzc; passport_auth_status=166b61dc31a8ef0c6dd6055d03941cb2%2C; passport_auth_status_ss=166b61dc31a8ef0c6dd6055d03941cb2%2C; uid_tt=9f0500255ccfb09453e2590e7de659f6; uid_tt_ss=9f0500255ccfb09453e2590e7de659f6; sid_tt=f73bbdf4d086d39742d21042ae244799; sessionid=f73bbdf4d086d39742d21042ae244799; sessionid_ss=f73bbdf4d086d39742d21042ae244799; publish_badge_show_info=%220%2C0%2C0%2C1699081677005%22; LOGIN_STATUS=1; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=a2fd0167087d25ed969a7ff19da3b136; __security_server_data_status=1; sid_guard=f73bbdf4d086d39742d21042ae244799%7C1699081676%7C5183992%7CWed%2C+03-Jan-2024+07%3A07%3A48+GMT; sid_ucp_v1=1.0.0-KDJkNDYzODFhZDE3MzI1ZmM2M2I5MDZjNmUwMmIyYTRmMDA0NmJkZjAKGQiv7JuJiAIQzNuXqgYY7zEgDDgGQPQHSAQaAmxmIiBmNzNiYmRmNGQwODZkMzk3NDJkMjEwNDJhZTI0NDc5OQ; ssid_ucp_v1=1.0.0-KDJkNDYzODFhZDE3MzI1ZmM2M2I5MDZjNmUwMmIyYTRmMDA0NmJkZjAKGQiv7JuJiAIQzNuXqgYY7zEgDDgGQPQHSAQaAmxmIiBmNzNiYmRmNGQwODZkMzk3NDJkMjEwNDJhZTI0NDc5OQ; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAH7XG2XkvkQq8SuAJbN-Km4ecPpyZ3pUI1Yokfw9AWmk%2F1699113600000%2F0%2F1699083530630%2F0%22; my_rd=2; csrf_session_id=a3b36808daf4f2c1f04a1537c82e3a86; download_guide=%223%2F20231104%2F0%22; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.443%7D; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1699697308648%2C%22type%22%3A1%7D; tt_scid=swmhkUl2XiEBFywY8XVZfy7E9jCLQkA-nE7DJ.iObYlNzBLepZxepgfN4AAHpHQK0b18; pwa2=%220%7C0%7C2%7C0%22; passport_fe_beating_status=true; __ac_nonce=0654620f9007eaba581dd; __ac_signature=_02B4Z6wo00f01xXG8zQAAIDAQER4qqeQXGMV5veAAKBBRZnvLnZGPDsEwGNOID9zWhHjQO73fogP4Vt.fUPUgSFwmfrJfLYBrDOTyepd3ZUBYUWuqh79kZVK8AD3jWraD8D9y.xN.zehZAKM9f; SEARCH_RESULT_LIST_TYPE=%22single%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAH7XG2XkvkQq8SuAJbN-Km4ecPpyZ3pUI1Yokfw9AWmk%2F1699113600000%2F0%2F1699094783564%2F0%22; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQ1VZZGVEWjdpY2g2QW1TL1A0S0JTVXpOSnNtZHMwclNpRVV6UmlaUXA3Mkw2cFlNVEVuaHJ5c01LZXV5ekh5d0FLcE1nbnk5MTM4QndnZXlpMzhtalE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=vRiCAQd85-rhOg-gYbxJ-rVKHz3r5AQ058L3Ly7-8B32fBS2BaX0ZO080WN11uCvE7_GuUAmKerZXIOdUxsoAolnLq0cg5j1IM4tNnSTmZbbCkfJpwJBaug-ITHp0k2-Pg==; odin_tt=1f78dbdff2e79236b021e74c3a470c47c184adf012e64c7b609d081a9047a6b32632e4238152d4911e5ed025daf860766f871d1c9aaccf8c29b0934c2281147c; msToken=rhJHMlOOBTHlPijuFCrECkqTsV855hTUgzCEvMqWbCme33C3_gOTQcnYPeWotu7uKxsiay2rR4W3g6opqlfja8FZHKI4BQZgaglU9v1_QZs24kMHLJuYqA1gnHeULbIH0Q==',
        'pragma': 'no-cache',
        'referer': 'https://www.douyin.com/user/MS4wLjABAAAA0W6MrnV7YIYmneCLCypeKVoZj4VDk9amQorNZ8aIVfs',
        'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
    }

    params = (
        ('device_platform', 'webapp'),
        ('aid', '6383'),
        ('channel', 'channel_pc_web'),
        ('sec_user_id', 'MS4wLjABAAAA0W6MrnV7YIYmneCLCypeKVoZj4VDk9amQorNZ8aIVfs'),
        ('max_cursor', '1696500302000'),
        ('locate_query', 'false'),
        ('show_live_replay_strategy', '1'),
        ('need_time_list', '0'),
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
        ('browser_version', '118.0.2088.76'),
        ('browser_online', 'true'),
        ('engine_name', 'Blink'),
        ('engine_version', '118.0.0.0'),
        ('os_name', 'Windows'),
        ('os_version', '10'),
        ('cpu_core_num', '16'),
        ('device_memory', '8'),
        ('platform', 'PC'),
        ('downlink', '10'),
        ('effective_type', '4g'),
        ('round_trip_time', '50'),
        ('webid', '7297499797400897065'),
        ('msToken',
         'rhJHMlOOBTHlPijuFCrECkqTsV855hTUgzCEvMqWbCme33C3_gOTQcnYPeWotu7uKxsiay2rR4W3g6opqlfja8FZHKI4BQZgaglU9v1_QZs24kMHLJuYqA1gnHeULbIH0Q=='),
        ('X-Bogus', 'DFSzswVuUKvANJUctFBbRjNSwbFJ'),
    )

    response = requests.get('https://www.douyin.com/aweme/v1/web/aweme/post/', headers=headers, params=params)
    # 响应200, 但是没有数据
    print(response.status_code)
    print(response.text)

    with open('../data/douyin.json', 'w', encoding='utf-8') as f:
        f.write(response.text)
        # json_data = response.json()
        # # 格式化json
        # json_data = json.dumps(json_data, indent=4, ensure_ascii=False)
        # f.write(json_data)
