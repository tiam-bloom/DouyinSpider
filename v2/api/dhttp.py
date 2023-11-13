# _*_ coding : UTF-8 _*_
# @Time : 2023/11/12 19:57
# @Auther : Tiam
# @File : http
# @Project : DouyinSpider
# @Desc :
import re
from urllib.parse import urlencode

import requests

from v2.downloader import Downloader
from v2.log import logger
from v2.signature import Signature, gen_random_str


class Http:
    def __init__(self, base_url):
        self.downloader = Downloader("JSON")
        self.base_url = base_url
        # todo 创建UA池, 随机UA
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        cookies = {
            # 登录凭证
            'sessionid': 'f73bbdf4d086d39742d21042ae244799',
            # 游客ID, 用于推荐
            'ttwid': '1%7CF6oAfQ2-NDzH4Ma6NR_j4SEAmknHsh_jLTV2F1XAtUE%7C1699029194%7C57185f4dfeca5d3cde14a9b7a10b8a90d6863b3ba92f69834483945e16d9b8e4'
        }
        cookies = '; '.join([f'{key}={value}' for key, value in cookies.items()])
        self.headers = {
            'user-agent': user_agent,
            'cookie': cookies
        }
        ms_token = Signature.gen_ms_token()
        self.params = (
            ('device_platform', 'webapp'),
            ('aid', '6383'),
            ('channel', 'channel_pc_web'),
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

    def requests(self, method, url, params, headers, **kwargs):
        """
        重写requests方法
        :param headers:
        :param params:
        :param method: 请求方法
        :param url: 请求地址
        :param kwargs: 其他参数
        :return:
        """
        # 合并公共参数
        params = self.params + params
        # 编码参数
        encode_params = urlencode(params, safe='=')  # safe='=' 保留等号, 避免被编码为%3D
        # 生成X-Bogus
        new_url = self.base_url + url + '?' + encode_params
        xbogus = Signature.gen_xbogus(new_url, self.headers['user-agent'])
        # 添加上X-Bogus参数
        new_url = new_url + '&X-Bogus=' + xbogus
        # 添加请求头
        self.headers.update(headers)
        # params 参数使用拼接形式, 避免被编码为%3D
        return requests.request(method, new_url, headers=self.headers, **kwargs)

    def get(self, url, params, headers, **kwargs):
        """
        重写get方法
        :param headers:
        :param url: 请求地址
        :param params: 请求参数
        :param kwargs: 其他参数
        :return:
        """
        return self.requests('GET', url, params, headers, **kwargs)

    def post(self, url, params, headers, **kwargs):
        """
        重写post方法
        :param headers:
        :param params:
        :param url: 请求地址
        :param kwargs: 其他参数
        :return:
        """
        return self.requests('POST', url, params, headers, **kwargs)

    def res(self, response, index=0):
        """
        统一处理返回结果
        :param index:
        :param response:
        :return:
        """
        logger.info('{}、本次请求状态码: {}, 返回数据长度: {}', index, response.status_code, len(response.text))
        if response.status_code == 200 and len(response.text) > 0:
            url = response.url
            filename = re.search(r'(?<=https://www.douyin.com/aweme/v1/web/).*(?=/\?)', url).group(0)
            filename = str(index) + '_' + filename.replace('/', '_') + '_' + gen_random_str(10)
            logger.info('保存文件名: {}', filename)
            json_data = response.json()
            # 保存json文件做备份
            self.downloader.save_json_file(json_data, filename)
            return json_data


class Url:
    domain = 'https://www.douyin.com'
    aweme_v1_web = '/aweme/v1/web'
    # 用户信息
    user_profile_other = '/user/profile/other/'
    # 用户作品相关数据
    aweme_post = '/aweme/post/'
    # 用户关注列表
    user_following_list = '/user/following/list/'
    # 用户粉丝列表
    user_follower_list = '/user/follower/list/'
    # 作品评论列表
    comment_list = "/comment/list/"
    # 作品评论回复列表
    aweme_detail = "/aweme/detail/"
    # 视频收藏列表
    aweme_list_collection = "/aweme/listcollection/"
    # 音乐收藏列表
    music_list_collection = "/music/listcollection/"
    # 热搜列表
    hot_search_list = "/hot/search/list/"


http_aweme_v1_web = Http(Url.domain + Url.aweme_v1_web)
