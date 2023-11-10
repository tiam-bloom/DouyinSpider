# _*_ coding : UTF-8 _*_
# @Time : 2023/11/10 12:06
# @Auther : Tiam
# @File : ffmpeg
# @Project : DouyinSpider

# pip install python-ffmpeg
# from ffmpeg import FFmpeg, FFmpegError
# pip install ffmpeg-python
import ffmpeg

"""
需有ffmpeg环境
"""
def get_video_info(source_video_path):
    # ffmpeg = FFmpeg()
    probe = ffmpeg.probe(source_video_path)
    print('source_video_path: {}'.format(source_video_path))
    format = probe['format']
    bit_rate = int(format['bit_rate']) / 1000
    duration = format['duration']
    size = int(format['size']) / 1024 / 1024
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    if video_stream is None:
        print('No video stream found!')
        return
    width = int(video_stream['width'])
    height = int(video_stream['height'])
    num_frames = int(video_stream['nb_frames'])
    fps = int(video_stream['r_frame_rate'].split('/')[0]) / int(video_stream['r_frame_rate'].split('/')[1])
    duration = float(video_stream['duration'])
    print('width: {}'.format(width))
    print('height: {}'.format(height))
    print('num_frames: {}'.format(num_frames))
    print('bit_rate: {}k'.format(bit_rate))
    print('fps: {}'.format(fps))
    print('size: {}MB'.format(size))
    print('duration: {}'.format(duration))


if __name__ == "__main__":
    # video_path = "F:\\Tiam\\Desktop\\JustPlay\\Python\\DouyinSpider\\data\\MS4wLjABAAAACV5Em110SiusElwKlIpUd-MRSi8rBYyg0NfpPrqZmykHY8wLPQ8O4pv3wPL6A-oz\\18-🔴🔴🔴.mp4"
    # video_path = "18ju.mp4"
    video_path = r"F:\Tiam\Desktop\JustPlay\Python\DouyinSpider\test\18ju.mp4"
    get_video_info(video_path)
