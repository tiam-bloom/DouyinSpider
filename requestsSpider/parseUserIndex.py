# _*_ coding : UTF-8 _*_
# @Time : 2023/11/4 19:03
# @Auther : Tiam
# @File : parseUserIndex
# @Project : DouyinSpider
# @Desc 根据https://www.douyin.com/aweme/v1/web/locate/post/接口返回的数据, 下载视频
# https://www.douyin.com/aweme/v1/web/aweme/post/


import json
import v1.downloader as down
import os

index = 0


# json_file, 接口返回的json文件位置
# save_file_dir, 保存视频的文件夹路径
def save_video_batch(json_file, save_file_dir):
    global index
    if not os.path.exists(save_file_dir):
        os.makedirs(save_file_dir)
    # 读取json文件
    with open(json_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        aweme_list = json_data['aweme_list']
        for aweme in aweme_list:
            video_url_list = aweme['video']['play_addr']['url_list']
            video_name = aweme['desc']
            # 一个视频有三个地址, 成功一个就OK
            index += 1
            for video_url in video_url_list:
                # print(video_url)
                try:
                    down.download_video(video_url, f'{save_file_dir}{index}-{video_name}.mp4')
                    break
                except Exception as e:
                    print('下载失败')


save_video_batch('../params/鞠婧祎主页1.json', '../data/鞠婧祎主页/')
save_video_batch('../params/鞠婧祎主页2.json', '../data/鞠婧祎主页/')
save_video_batch('../params/鞠婧祎主页3.json', '../data/鞠婧祎主页/')
