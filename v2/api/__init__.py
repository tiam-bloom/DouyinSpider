# _*_ coding : UTF-8 _*_
# @Time : 2023/11/11 19:14
# @Auther : Tiam
# @File : __init__.py
# @Project : DouyinSpider
# @Desc: 数据请求  只做api请求相关

import datetime
import re
from urllib.parse import urlencode

import requests
from v2.signature import Signature
from v2.downloader import Downloader
from v2.log import logger


class ReqUserAwemePost:
    base_url = 'https://www.douyin.com'
    post_url = '/aweme/v1/web/aweme/post/'
    url = base_url + post_url

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

    def __init__(self, sec_user_id, count=32):
        """
        请求用户作品相关数据
        :param sec_user_id: 用户id
        :param count: 每次请求的数量
        """
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
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        ms_token = Signature.gen_ms_token()
        params = (
            ('device_platform', 'webapp'),
            ('aid', '6383'),
            ('channel', 'channel_pc_web'),
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
            ('msToken', ms_token)
        )
        encode_params = urlencode(params, safe='=')  # safe='=' 保留等号, 避免被编码为%3D
        url = f'{ReqUserAwemePost.url}?{encode_params}'
        # 加密url等生成xbogus
        xbogus = Signature.gen_xbogus(url, user_agent)
        # 貌似不需要ttwid, 减少一次请求
        # ttwid = Signature.gen_ttwid()
        new_url = url + f'&X-Bogus={xbogus}'
        headers = {
            'referer': f'{ReqUserAwemePost.base_url}/user/{self.sec_user_id}',
            'user-agent': user_agent,
            'cookie': f'ttwid=1%7CF6oAfQ2-NDzH4Ma6NR_j4SEAmknHsh_jLTV2F1XAtUE%7C1699029194%7C57185f4dfeca5d3cde14a9b7a10b8a90d6863b3ba92f69834483945e16d9b8e4; '
        }
        logger.info('第 {} 次请求url: {}', self.index, new_url)
        try:
            response = requests.get(new_url, headers=headers)
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
