# _*_ coding : UTF-8 _*_
# @Time : 2023/11/13 10:37
# @Auther : Tiam
# @File : req_follower_list
# @Project : DouyinSpider
# @Desc :
import json

from v2.api.dhttp import (http_aweme_v1_web, Url)
from v2.log import logger


class ReqFollowerList:

    def __init__(self, sec_user_id):
        self.sec_user_id = sec_user_id
        self.index = 0

    def req_follower_list(self, offset=0, max_time=0, source_type=2):
        """
        请求粉丝列表
        :return:
        """
        self.index += 1
        params = (
            ('user_id', '70886290991'),  # 传参
            ('sec_user_id', self.sec_user_id),
            ('offset', str(offset)),
            ('min_time', '0'),
            ('max_time', str(max_time)),
            ('count', '20'),
            ('source_type', str(source_type)),  # 1表示粉丝列表,
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
        return http_aweme_v1_web.res(response, self.index)

    def req_all_follower_list(self):
        offset = 0
        max_time = 0
        source_type = 2
        follower_list = []
        while True:
            logger.info('正在获取粉丝列表, offset: {}, max_time: {}', offset, max_time)
            res = self.req_follower_list(offset, max_time, source_type)
            if res is None:
                logger.error('请求失败')
                break
            has_more = res['has_more']
            follower_list.extend(res['followers'])
            total = res['total']
            logger.info('已获取粉丝列表: {}', total)
            if not has_more:
                logger.info('没有更多了')
                break
            offset = res['offset']
            max_time = res['max_time']
            source_type = 1
        logger.info('粉丝列表获取完毕, 总粉丝数: {}', len(follower_list))
        return follower_list


def test():
    user_id = '70886290991'
    sec_user_id = 'MS4wLjABAAAAH7XG2XkvkQq8SuAJbN-Km4ecPpyZ3pUI1Yokfw9AWmk'
    req = ReqFollowerList(sec_user_id)
    follower_list = req.req_all_follower_list()
    with open('./data/all_followers.json', 'w', encoding='utf-8') as f:
        json.dump(follower_list, f, indent=2, ensure_ascii=False)


test()
