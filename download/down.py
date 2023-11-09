# _*_ coding : UTF-8 _*_
# @Time : 2023/11/4 15:42
# @Auther : Tiam
# @File : down
# @Project : DouyinSpider
import json
import os

import requests

# 总下载数
all_counts = 0


# download_video(video_url1, '../data/3.mp4')
def download_video(url, path):
    global all_counts
    all_counts += 1
    print(f'\n{all_counts}: 开始下载视频: ', path.split('/')[-1])
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        # 进度条
        total_length = int(r.headers.get('content-length'))
        print('视频大小:', total_length)
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)
            # 打印进度条
            print('\r' + '[下载进度]:%s%.2f%%' % (
                '>' * int((f.tell() / total_length) * 50), float(f.tell() / total_length) * 100), end='')


def test():
    url = 'https://www.douyin.com/aweme/v1/play/?video_id=v0d00fg10000ci60h9rc77u1m6ch7cng&line=0&file_id=980f0b8417fb4f9eb6e030da8c349f77&sign=d60c90ba370d592df6e316eac5e704b1&is_play_url=1&source=PackSourceEnum_PUBLISH'
    download_video(url, '../data/test.mp4')


# test()
# 出错次数
err_counts = 0


# save_video_batch('../params/鞠婧祎主页1.json', '../data/鞠婧祎主页/')
def save_video_batch_by_json_file(json_file, save_file_dir):
    global err_counts
    if not os.path.exists(save_file_dir):
        os.makedirs(save_file_dir)
    # 读取json文件
    with open(json_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        save_video_batch(json_data, save_file_dir)


index = 0


def save_video_batch(json_data, save_file_dir):
    global err_counts, index
    if not os.path.exists(save_file_dir):
        os.makedirs(save_file_dir)
    aweme_list = json_data['aweme_list']
    for aweme in aweme_list:
        video_url_list = aweme['video']['play_addr']['url_list']
        video_name = aweme['desc']
        # 文件名中不能有特殊字符, 替换掉
        video_name = video_name.replace('/', '').replace('\\', '').replace(':', '').replace('*', '').replace('?', '')
        index += 1
        # 一个视频有三个地址, 成功一个就OK
        for video_url in video_url_list:
            # print(video_url)
            try:
                download_video(video_url, f'{save_file_dir}{index}-{video_name}.mp4')
                break
            except Exception as e:
                print('下载失败', e)
                err_counts += 1
                with open('../data/error.log', 'a', encoding='utf-8') as log:
                    log.write(f'{err_counts}、{index}-{video_name}:{video_url}\n')
