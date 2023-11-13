# _*_ coding : UTF-8 _*_
# @Time : 2023/11/13 10:37
# @Auther : Tiam
# @File : req_follower_list
# @Project : DouyinSpider
# @Desc :

import requests



headers = {
    'referer': 'https://www.douyin.com/user/self?showTab=post',
}

params = (
    ('user_id', '70886290991'),
    ('sec_user_id', 'MS4wLjABAAAAH7XG2XkvkQq8SuAJbN-Km4ecPpyZ3pUI1Yokfw9AWmk'),
    ('offset', '0'),
    ('min_time', '0'),
    ('max_time', '1699779496'),
    ('count', '20'),
    ('source_type', '1'),
    ('gps_access', '0'),
    ('address_book_access', '0'),
)

