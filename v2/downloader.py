# _*_ coding : UTF-8 _*_
# @Time : 2023/11/4 15:42
# @Auther : Tiam
# @File : down
# @Project : DouyinSpider
# @Desc: 下载器 只做下载相关
import json
import os
import re

import requests

from v2.signature import gen_random_str
from v2.log import logger


class FileUtil:
    @staticmethod
    def legalize_file_name(file_name):
        """
        规范文件名
        :param file_name: 文件名(不包括后缀!)
        :return:
        """
        # 文件名中不能有特殊字符, 替换掉
        file_name = (file_name.replace('/', '').replace('\\', '').replace(':', '')
                     .replace('*', '').replace('?', '').replace('.', ''))
        # 去除\n \t 等空白字符
        file_name = re.sub(r'\s', '', file_name)
        # 长度限制
        file_name = file_name[:50]
        return file_name

    @staticmethod
    def if_not_exists_create_dir(path):
        """
        如果文件夹不存在, 创建文件夹
        :param path:
        :return:
        """
        # 带文件名的路径, 只创建文件夹
        if '.' in path:
            path = os.path.dirname(path)
        if not os.path.exists(path):
            os.makedirs(path)


# 文件夹层级 /user_id/视频文件
# 文件夹层级 /user_id/年份/视频文件
# 文件夹层级 /user_id/分页/视频文件
class Downloader:
    # 默认保存路径在当前程序的data文件夹下
    def __init__(self, save_dir, base_dir_path='./data/'):
        path = os.path.abspath(os.path.join(base_dir_path, save_dir))
        # 创建文件夹
        FileUtil.if_not_exists_create_dir(os.path.join(path, 'json'))
        # 下载器保存文件夹路径
        self.save_dir_path = path
        self.save_json_dir_path = os.path.join(path, 'json')
        # 作品序号
        self.index = 0
        # 成功下载数
        self.ok_counts = 0
        # 失败下载数
        self.err_counts = 0
        # 总下载次数
        self.all_counts = 0

    # 自定义文件夹, file_name = 文件夹名\\文件名.后缀
    # 或者直接传入文件名
    def download(self, url, file_name):
        """
        下载文件,
        :param url: 下载地址
        :param file_name: 文件名.后缀, 若需要自定义文件夹, 文件夹名\\文件名.后缀
        :return: 成功返回True, 出错返回False
        """
        self.all_counts += 1
        try:
            r = requests.get(url, stream=True)
            total_length = int(r.headers.get('content-length'))
            size_kb = total_length / 8 / 1024
            # fixme 异步打印的日志会乱序, 有时会先打印文件大小, 再打印进度条
            logger.info('{}、开始下载： {}，文件大小: {}', self.all_counts, file_name,
                        (f'{size_kb:.2f}KB' if size_kb < 1024 else f'{size_kb / 1024:.2f}MB'))
            path = os.path.join(self.save_dir_path, file_name)
            FileUtil.if_not_exists_create_dir(path)
            with open(path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                    # 打印进度条
                    p = f.tell() / total_length
                    mark = '>' * int(p * 50)  # 进度条50个字符
                    progress = float(p) * 100  # 进度百分比
                    print('\r[下载进度]:%s%.2f%%' % (mark, progress), end='')  # \r回到行首重写
                print('\n')
            return True
        except Exception as e:
            self.err_counts += 1
            logger.error(f'下载失败 err_counts: {self.err_counts}\n'
                         f' url: {url}\n'
                         f' file_name: {file_name}\n'
                         f' error: {e}')
            return False

    def download_image(self, aweme_name, images):
        """
        下载图文类型作品, 可能会有多个图文
        多图文时, 创建文件夹
        :param aweme_name:
        :param images: [aweme_list][images] json数据
        :return: 多图文时, 返回是否全部下载成功
        """
        # 结构变化时的异常处理
        if len(images) == 1:
            # 只有一张图片
            url_list = images[0]['url_list']
            url = url_list[-1]
            return self.download(url, f'{aweme_name}.jpeg')
        is_success = True
        for image in images:
            # download_url_list 有抖音水印, 一个相同的图片有四个地址
            url_list = image['url_list']
            # fixme 可能会异常: 图片类型不匹配
            # 倒序遍历(一般最后一个为jpeg格式, 优先保存jpeg格式的图片, 若不存在则保存webp格式的图片),
            # for url in url_list[::-1]:
            #     # 正则匹配文件后缀,
            #     file_type = re.search(r'\.(\w+)(?=\?)', url).group(0)
            #     if file_type == '.jpeg':
            #         break
            url = url_list[-1]
            if not self.download(url, aweme_name + os.path.sep + f'{gen_random_str(10)}.jpeg'):
                is_success = False
        return is_success

    def download_video(self, aweme_name, video):
        """
        下载视频类型作品
        :param aweme_name:
        :param video: [aweme_list][video] json数据, fixme [aweme_list][video][bit_rate][video_extra] 中包含视频格式信息, 是否都是.mp4格式?
        :return:
        """
        # 视频下载
        video_url_list = video['play_addr']['url_list']
        for video_url in video_url_list:
            # 一个视频有三个地址, 成功一个跳出循环
            if self.download(video_url, aweme_name + '.mp4'):
                return True
        return False

    def download_aweme(self, aweme):
        """
        下载作品
        :param aweme: [aweme_list][n] json数据
        :return:
        """
        self.index += 1
        # 作品名 = 作品序号-作品id-作品描述
        aweme_name = f'{self.index}-{aweme['aweme_id']}-{FileUtil.legalize_file_name(aweme['desc'])}'
        images = aweme['images']
        return self.download_image(aweme_name, images) if images is not None \
            else self.download_video(aweme_name, aweme['video'])

    def save_video_aweme_list(self, aweme_list):
        """
        批量下载视频
        :param aweme_list: [aweme_list] json数据
        :return: None
        """
        # 遍历每一个视频数据
        for aweme in aweme_list:
            if self.download_aweme(aweme):
                self.ok_counts += 1
            else:
                self.err_counts += 1
        logger.info(f'下载完成, 成功: {self.ok_counts}, 失败: {self.err_counts}')

    def save_video_page(self, json_data):
        """
        接口/aweme/v1/web/aweme/post/接口返回的json数据批量下载视频. 一页的请求
        :param json_data:
        :return:
        """
        aweme_list = json_data['aweme_list']
        self.save_video_aweme_list(aweme_list)

    def save_json_file(self, json_data, file_name=gen_random_str(10)):
        """
        将返回的json数据保存到文件
        :param json_data:
        :param file_name:
        :return:
        """
        path = os.path.join(self.save_json_dir_path, file_name + '.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)

    def save_video_batch_by_json_file(self, json_file):
        """
        通过json文件批量下载视频
        :param json_file: json文件路径
        :return:
        """
        # 读取json文件
        with open(json_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            self.save_video_page(json_data)

    def save_video_by_json_dir(self):
        """
        通过备份的json文件夹批量下载视频
        :return:
        """
        # 遍历json文件夹
        for file_name in os.listdir(self.save_json_dir_path):
            self.save_video_batch_by_json_file(os.path.join(self.save_json_dir_path, file_name))
