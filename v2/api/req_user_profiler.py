# _*_ coding : UTF-8 _*_
# @Time : 2023/11/12 16:16
# @Auther : Tiam
# @File : user_profile_other
# @Project : DouyinSpider
# @Desc :


class ReqUserProfileOther:

    def __init__(self, downloader, sec_user_id):
        self.downloader = downloader
        self.sec_user_id = sec_user_id

    def req_user_profile(self):
        """
        请求用户信息
        :return:
        """
