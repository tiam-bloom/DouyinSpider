import scrapy


class DouyinSpider(scrapy.Spider):
    # 爬虫名称
    name = "douyin"
    # 允许的域名
    allowed_domains = ["douyin.com"]
    # 起始url
    start_urls = ["https://www.douyin.com/user/MS4wLjABAAAA0W6MrnV7YIYmneCLCypeKVoZj4VDk9amQorNZ8aIVfs"]
    # 星狗主页
    # https://www.douyin.com/user/MS4wLjABAAAA0W6MrnV7YIYmneCLCypeKVoZj4VDk9amQorNZ8aIVfs
    headers = {
        'authority': 'www.douyin.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'cookie': 'douyin.com; xgplayer_user_id=152104322538; n_mh=Cnh05CH1Mtmld1KnWiQ-4Gqbkf702lUnDliGiTaf92g; store-region-src=uid; LOGIN_STATUS=1; store-region=cn-hb; pwa2=%220%7C1%7C3%7C1%22; d_ticket=c6337b48db285d72e73fe2cbcd97854c87f54; passport_assist_user=CjxwceZlK-VNALbVqW62kp9WDdfzbzbqi8Y4yIMX7y-kAGgPTpvO9ecfy4q2CEB94dfxi216gsW9skQdsUQaSAo8qLkBLf_8NZMPkqf0mJPOzEHLL5LqjgTiNELZY1_9PkwTdjBtXFDMfUA4VNSCFmUINOOBxpFjX7NcYgqzEIjstg0Yia_WVCIBAxgSZVk%3D; sso_uid_tt=7208fc825e838b2c4290ce9fc61f23d5; sso_uid_tt_ss=7208fc825e838b2c4290ce9fc61f23d5; toutiao_sso_user=c583a4e405d534d5e9f6cc73e0a9e863; toutiao_sso_user_ss=c583a4e405d534d5e9f6cc73e0a9e863; uid_tt=b6426093ea2b823f85a4040e232b0b93; uid_tt_ss=b6426093ea2b823f85a4040e232b0b93; sid_tt=4c769734ce752a918588a603842211ff; sessionid=4c769734ce752a918588a603842211ff; sessionid_ss=4c769734ce752a918588a603842211ff; _bd_ticket_crypt_cookie=5128cec53947015ee79c31fd8f5eda91; s_v_web_id=verify_lm7xwzrb_nbSNOZWC_4tkh_494p_8IqP_zAISmIKVPTlK; passport_csrf_token=2ef0f17fd1cb67cc968c9bb20608a2f0; passport_csrf_token_default=2ef0f17fd1cb67cc968c9bb20608a2f0; xgplayer_device_id=4975380006; sid_ucp_sso_v1=1.0.0-KDNkZTQ5MDkwZTNjOGE0ZGU1Mjk1MTE0NDYxYjVjNjRiNjhlZTJhZDcKHQiv7JuJiAIQ5tLJqQYY7zEgDDDKrr7OBTgCQPEHGgJsZiIgYzU4M2E0ZTQwNWQ1MzRkNWU5ZjZjYzczZTBhOWU4NjM; ssid_ucp_sso_v1=1.0.0-KDNkZTQ5MDkwZTNjOGE0ZGU1Mjk1MTE0NDYxYjVjNjRiNjhlZTJhZDcKHQiv7JuJiAIQ5tLJqQYY7zEgDDDKrr7OBTgCQPEHGgJsZiIgYzU4M2E0ZTQwNWQ1MzRkNWU5ZjZjYzczZTBhOWU4NjM; sid_guard=4c769734ce752a918588a603842211ff%7C1697802599%7C5184000%7CTue%2C+19-Dec-2023+11%3A49%3A59+GMT; sid_ucp_v1=1.0.0-KDVlMDMxOGE2ODg3ZWM5YzM3MWM1YThhNTJkYmNhNzM0NzQwMGUwMmUKGQiv7JuJiAIQ59LJqQYY7zEgDDgCQPEHSAQaAmxxIiA0Yzc2OTczNGNlNzUyYTkxODU4OGE2MDM4NDIyMTFmZg; ssid_ucp_v1=1.0.0-KDVlMDMxOGE2ODg3ZWM5YzM3MWM1YThhNTJkYmNhNzM0NzQwMGUwMmUKGQiv7JuJiAIQ59LJqQYY7zEgDDgCQPEHSAQaAmxxIiA0Yzc2OTczNGNlNzUyYTkxODU4OGE2MDM4NDIyMTFmZg; __live_version__=%221.1.1.4685%22; publish_badge_show_info=%220%2C0%2C0%2C1698578473546%22; download_guide=%223%2F20231027%2F1%22; SEARCH_RESULT_LIST_TYPE=%22single%22; my_rd=2; strategyABtestKey=%221699029604.168%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; webcast_local_quality=origin; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAH7XG2XkvkQq8SuAJbN-Km4ecPpyZ3pUI1Yokfw9AWmk%2F1699113600000%2F0%2F0%2F1699074138561%22; csrf_session_id=a426b541599d7c19edbaf70cfa4eef41; ttwid=1%7C4bQ0eV-509jqsz2TMBWV9WwBdNN_j-orncC17n0MVsE%7C1699073452%7C3863edcea7f3e0ec09893d981cdd8bf845594370791465b7c0aa83df8d08fdf4; _tea_utm_cache_1243=undefined; MONITOR_WEB_ID=dcbc4e0c-8c9f-4137-8645-46b835319c15; EnhanceDownloadGuide=%220_0_0_0_1_1699075154%22; __ac_signature=_02B4Z6wo00f01e.HnPAAAIDCukUXb.vJM3Xv55hAAB62J6oineKeF.Nq-f0gKDVgguN6beRwCnlhP2ISbW5ThIE7N9qAqNyh7RtcYQ9OaSqbApqXbm4wTF3Up60XOuFLWAIO-S35Vn4g.s4Hff; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAH7XG2XkvkQq8SuAJbN-Km4ecPpyZ3pUI1Yokfw9AWmk%2F1699113600000%2F0%2F1699075180926%2F0%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1699679981252%2C%22type%22%3A1%7D; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQ1VZZGVEWjdpY2g2QW1TL1A0S0JTVXpOSnNtZHMwclNpRVV6UmlaUXA3Mkw2cFlNVEVuaHJ5c01LZXV5ekh5d0FLcE1nbnk5MTM4QndnZXlpMzhtalE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; tt_scid=cAp4IEYjDkPLec2q8gEHdhixuLqf0sYVq38iHMKzL8YbW1BrpCUtHK-lee3gIEVu4d11; odin_tt=c6a0c8c6d5986b96f8d24ae243d4bbd6f3673f7015908502b3c9c8d5af08c94869900d5ac54e8ba2037b2d7a9f74b73c; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.443%7D; msToken=5SItS4zXJGKsL8yn7ZeSVrFg7KfJ1rJkWrOgSAvA6bD5tj92nHJmnuTPRCfrnHkgXy1pDnHUVS2kiXYo94K5r1n62-zhS39CVpSAexRLb95bzAmv0clY3DNXSHwyyHWPfA==; __ac_nonce=06545e32600e34ee9ba2e; msToken=L5-qCgVttPeZrEfBjPqXRiXiLyoL32j0QZlQiWlItx-DcjutNv7bFykJJbjY553_L_e12TDFraGb-A0rKKXkru4kuTK1oF_GNw_m3D4w_R7gA7Y0YGLf0kQu0W8VjYKMwg==; IsDouyinActive=false; passport_fe_beating_status=false',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, method='GET', headers=self.headers, callback=self.parse)

    def parse(self, response, **kwargs):
        print("begin...", response.status)
        with open('data/douyin.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        title = response.xpath('//*[@id="douyin-right-container"]/div[2]/div/div/div[1]/div[2]/div['
                               '1]/h1/span/span/span/span/span/span/text').extract_first()
        print(title)
        pass
