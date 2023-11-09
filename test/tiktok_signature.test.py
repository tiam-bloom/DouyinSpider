# _*_ coding : UTF-8 _*_
# @Time : 2023/11/5 16:53
# @Auther : Tiam
# @File : tiktok_signature.test
# @Project : DouyinSpider

import requests
import json

url = "https://tiktok.signature.yujing.icu/"

payload = json.dumps({
   "url": "https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=36&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2560&screen_height=1440&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7297274756444276239&msToken=LvUPiShgy7Q4Hi1U-QA9W-Y603GT8B8zH5NZwfL8hFFhMWvnrIXMvnEMKSJmXbabMt39bDj3bREfCxkbiuseLg0w9hOgMoUfSfzveEuhk-JW9-eCQ9NLVN30Mmd9gJI=&X-Bogus=DFSzswVYqXkANCMrtFQrGBt/pLfc",
   "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
})
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json',
   'Accept': '*/*',
   'Host': 'tiktok.signature.yujing.icu',
   'Connection': 'keep-alive'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)