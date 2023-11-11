# _*_ coding : UTF-8 _*_
# @Time : 2023/11/12 2:16
# @Auther : Tiam
# @File : progressTest
# @Project : DouyinSpider
# @Desc :
from time import sleep
from loguru import logger

len = 100

for i in range(0, 2):
    for j in range(0, len + 1, 5):
        sleep(0.1)
        # 打印进度条
        print('\r[下载进度]:%s%.2f%%' % (
            '>' * int((j / len) * 50), float(j / len) * 100), end='')
        # logger.debug('\r'+'[下载进度]:%s%.2f%%' % (
        #     '>' * int((j / len) * 50), float(j / len) * 100))
    # print()
