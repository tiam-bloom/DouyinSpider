# _*_ coding : UTF-8 _*_
# @Time : 2023/11/4 15:42
# @Auther : Tiam
# @File : down
# @Project : DouyinSpider
import json
import os

import requests
# import logging

from v1.signature import gen_random_str


# 文件夹层级 /user_id/视频文件
# 文件夹层级 /user_id/年份/视频文件
# 文件夹层级 /user_id/分页/视频文件
class Downloader:
    # 类变量, 所有实例共享
    # 程序运行, 所有实例的总下载数
    all_counts = 0
    # 总出错次数
    err_counts = 0

    def __init__(self, save_dir_path):
        path = os.path.dirname(__file__) + save_dir_path
        if not os.path.exists(path):
            os.makedirs(path)
        # 下载器保存文件夹路径
        self.save_dir_path = path
        # 统计一个Downloader实例下载的视频数量
        self.index = 0
        pass

    def download_video(self, url, file_name=f'{gen_random_str(10)}.mp4'):
        """
        下载视频
        :param url: 视频地址
        :param file_name: 默认随机10位字符串
        :return:
        """
        Downloader.all_counts += 1
        print(f'\n{Downloader.all_counts}: 开始下载视频: ', file_name)
        r = requests.get(url, stream=True)
        path = self.save_dir_path + file_name
        with open(path, 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            print(f'视频大小:{total_length / 8 / 1024 / 1024}MB', )
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
                # 打印进度条
                print('\r' + '[下载进度]:%s%.2f%%' % (
                    '>' * int((f.tell() / total_length) * 50), float(f.tell() / total_length) * 100), end='')

    def save_video_batch(self, json_data):
        """
        接口/aweme/v1/web/aweme/post/接口返回的json数据批量下载视频
        :param json_data:
        :return:
        """
        aweme_list = json_data['aweme_list']
        for aweme in aweme_list:
            video_url_list = aweme['video']['play_addr']['url_list']
            video_name = aweme['desc']
            # 文件名中不能有特殊字符, 替换掉
            video_name = video_name.replace('/', '').replace('\\', '').replace(':', '').replace('*', '').replace('?',
                                                                                                                 '')
            # 长度限制
            video_name = video_name[:50]
            self.index += 1
            # 一个视频有三个地址, 成功一个就OK
            for video_url in video_url_list:
                # print(video_url)
                try:
                    self.download_video(video_url, f'{self.index}-{video_name}.mp4')
                    break
                except Exception as e:
                    Downloader.err_counts += 1
                    print('下载失败', e)
                    print(f'{Downloader.err_counts}、{self.index}-{video_name}:{video_url}\n')
                    # with open('../data/error.log', 'a', encoding='utf-8') as log:
                    #     log.write(f'{Downloader.err_counts}、{self.index}-{video_name}:{video_url}\n')

    def save_json_file(self, json_data, file_name=f'{gen_random_str(10)}.json'):
        """
        将返回的json数据保存到文件
        :param json_data:
        :param file_name:
        :return:
        """
        if not os.path.exists(self.save_dir_path + 'json/'):
            os.makedirs(self.save_dir_path + 'json/')
        path = f'{self.save_dir_path}json/{file_name}'
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
            self.save_video_batch(json_data)
