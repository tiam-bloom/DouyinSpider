# _*_ coding : UTF-8 _*_
# @Time : 2023/11/13 11:30
# @Auther : Tiam
# @File : req_aweme_post
# @Project : DouyinSpider
# @Desc :


import datetime
import re

import requests

from v2.api.http import (http, Url)
from v2.downloader import Downloader
from v2.log import logger


class ReqUserAwemePost:

    @staticmethod
    def from_url(url):
        """
        从url中提取sec_user_id
        :param url:
        :return: 成功实例化对象
        """
        sec_user_id = re.search(r'(?<=https://www.douyin.com/user/)[\w-]+', url).group()
        if sec_user_id is None:
            logger.error(
                r'请输入用户主页地址!, 格式应匹配正则: (?<=https://www.douyin.com/user/)[\w-]+ 可匹配到sec_user_id')
            return None
        return ReqUserAwemePost(sec_user_id)

    def __init__(self, sec_user_id, count=18):
        """
        请求用户作品相关数据
        :param sec_user_id: 用户id
        :param count: 每次请求的数量
        """
        super().__init__()
        self.sec_user_id = sec_user_id
        self.downloader = Downloader(sec_user_id)
        self.count = count
        self.index = 0

    def aweme_v1_web_aweme_post(self, max_cursor=0, need_time_list=1):
        """
        通过接口https://www.douyin.com/aweme/v1/web/aweme/post/请求用户作品相关数据
        :param max_cursor: 用于分页, 0表示第一页, 意义表示视频的时间戳
        :param need_time_list: 1表示需要时间列表, 0表示不需要(仅第一页需要)
        :return: 返回json数据, 失败返回None
        """
        self.index += 1
        params = (
            ('sec_user_id', self.sec_user_id),
            ('max_cursor', str(max_cursor)),
            ('locate_query', 'false'),
            ('show_live_replay_strategy', '1'),
            ('need_time_list', str(need_time_list)),
            ('time_list_query', '0'),
            ('whale_cut_token', ''),
            ('cut_version', '1'),
            ('count', str(self.count)),  # 每次请求的数量
            ('publish_video_strategy_type', '2'),
        )
        headers = {
            'referer': f'{Url.domain}/user/{self.sec_user_id}',
        }
        logger.info('第 {} 次请求', self.index)
        try:
            response = http.get(Url.aweme_post, params, headers)
            # response = requests.get(new_url, headers=headers)
        except Exception as e:
            logger.error('请求异常: {}', e)
            # 判断异常类型
            if isinstance(e, requests.exceptions.ConnectionError):
                logger.error('网络连接错误异常，如DNS查询失败、拒绝连接等')
            elif isinstance(e, requests.exceptions.Timeout):
                logger.error('请求URL超时，产生超时异常')
            elif isinstance(e, requests.exceptions.HTTPError):
                logger.error('HTTP错误异常')
            elif isinstance(e, requests.exceptions.TooManyRedirects):
                logger.error('超过最大重定向次数，产生重定向异常')
            else:
                logger.error('其他异常')
            return None
        logger.info('本次请求状态码: {}, 返回数据长度: {}', response.status_code, len(response.text))
        if response.status_code == 200 and len(response.text) > 0:
            json_data = response.json()
            logger.info('本次请求到的视频数量: {}', len(json_data['aweme_list']))
            # 保存json文件做备份
            date = datetime.datetime.fromtimestamp(int(max_cursor) / 1000).strftime('%Y-%m-%d') if max_cursor > 0 \
                else datetime.date.today()
            self.downloader.save_json_file(json_data, str(date))
            return json_data

    def req_user_aweme_list(self):
        # 统计视频数量
        max_cursor = 0
        need_time_list = 1
        user_aweme_list = []
        while True:
            res = self.aweme_v1_web_aweme_post(max_cursor, need_time_list)
            if res is None:
                break
            has_more = res['has_more']
            aweme_list = res['aweme_list']
            user_aweme_list.extend(aweme_list)
            if has_more == 0:
                break
            max_cursor = res['max_cursor']
            need_time_list = 0
        logger.info('请求完成, 获取的视频总数: {}', len(user_aweme_list))
        return user_aweme_list
