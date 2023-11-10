# _*_ coding : UTF-8 _*_
# @Time : 2023/11/10 11:32
# @Auther : Tiam
# @File : loguruTest
# @Project : DouyinSpider

from loguru import logger
# 封装looger

logger.add("log/debug1.log", rotation="500 MB", retention="10 days", level="DEBUG", enqueue=True, encoding="utf-8")
logger.add("log/info.log", rotation="500 MB", retention="10 days", level="INFO", enqueue=True, encoding="utf-8")
logger.add("log/warning.log", rotation="500 MB", retention="10 days", level="WARNING", enqueue=True, encoding="utf-8")

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")