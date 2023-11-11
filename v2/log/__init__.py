# _*_ coding : UTF-8 _*_
# @Time : 2023/11/11 19:32
# @Auther : Tiam
# @File : __init__.py
# @Project : DouyinSpider
# @Desc :

from loguru import logger

logger.add("log/debug.log", rotation="10 MB", retention="3 days", level="DEBUG", enqueue=True, encoding="utf-8")
logger.add("log/info.log", rotation="10 MB", retention="3 days", level="INFO", enqueue=True, encoding="utf-8")
logger.add("log/warning.log", rotation="10 MB", retention="3 days", level="WARNING", enqueue=True, encoding="utf-8")

# from v2.log import logger
