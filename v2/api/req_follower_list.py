# _*_ coding : UTF-8 _*_
# @Time : 2023/11/13 10:37
# @Auther : Tiam
# @File : req_follower_list
# @Project : DouyinSpider
# @Desc :
# from v2.downloader import Downloader
from v2.api.dhttp import (http_aweme_v1_web, Url)
from v2.log import logger


class ReqFollowerList:

    def __init__(self, sec_user_id):
        self.sec_user_id = sec_user_id

    def req_follower_list(self):
        """
        请求粉丝列表
        :return:
        """
        params = (
            ('user_id', '70886290991'),
            ('sec_user_id', self.sec_user_id),
            ('offset', '0'),
            ('min_time', '0'),
            ('max_time', '1699779496'),
            ('count', '20'),
            ('source_type', '1'),
            ('gps_access', '0'),
            ('address_book_access', '0'),
        )
        headers = {
            'referer': 'https://www.douyin.com/user/self?showTab=post',
        }
        try:
            response = http_aweme_v1_web.get(Url.user_follower_list, params, headers)
        except Exception as e:
            logger.error('请求异常: {}', e)
            return None
        return http_aweme_v1_web.res(response)


def test():
    sec_user_id = 'MS4wLjABAAAAH7XG2XkvkQq8SuAJbN-Km4ecPpyZ3pUI1Yokfw9AWmk'
    req_follower_list = ReqFollowerList(sec_user_id)
    follower_list = req_follower_list.req_follower_list()
    print(follower_list)


# test()
