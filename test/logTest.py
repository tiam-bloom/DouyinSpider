# _*_ coding : UTF-8 _*_
# @Time : 2023/11/10 11:00
# @Auther : Tiam
# @File : logTest
# @Project : DouyinSpider

import logging
import os
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] : %(message)s')

path = os.path.abspath(os.path.dirname(__file__))+os.path.sep+"debug.log"
file_handler = logging.FileHandler(path)  # 默认追加模式
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Start print log %s", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
logger.debug("Do something")
logger.warning("Something maybe %s fail." % "dangerous")
logger.info("Finish")

