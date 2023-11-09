# _*_ coding : UTF-8 _*_
# @Time : 2023/11/5 15:47
# @Auther : Tiam
# @File : override_models
# @Project : DouyinSpider

from urllib.parse import urlencode
from requests.utils import to_key_val_list
from requests.models import PreparedRequest

"""
重写requests库中的PreparedRequest类，实现自定义的参数编码方式
"""


class CustomRequest(PreparedRequest):
    def __init__(self, *args, **kwargs):
        super(CustomRequest, self).__init__()

    @staticmethod
    def _encode_params(self, data):
        """
        重写_encode_params方法，实现自定义的参数编码方式
        """
        # 在这里实现自定义的参数编码逻辑
        # 例如，可以将参数名和值用冒号分隔，而不是等号
        if isinstance(data, (str, bytes)):
            return data
        elif hasattr(data, "read"):
            return data
        elif hasattr(data, "__iter__"):
            result = []
            for k, vs in to_key_val_list(data):
                if isinstance(vs, (str, bytes)) or not hasattr(vs, "__iter__"):
                    vs = [vs]
                for v in vs:
                    if v is not None:
                        result.append(
                            (
                                k.encode("utf-8") if isinstance(k, str) else k,
                                v.encode("utf-8") if isinstance(v, str) else v,
                            )
                        )
            return urlencode(result, doseq=True, safe="=")
        else:
            return data


# req = CustomRequest("GET", 'https://www.douyin.com/aweme/v1/web/aweme/post/', headers=headers, params=params)