# coding:utf-8

import json
from common.api_request import http_request
from common.api_tools import retry
import os
from common.m_exceptions import DException as Exc


class Base(object):
    """
    统一请求格式
    """

    def __init__(self):
        self.headers_default = {}
        self.data_default = {}
        self.params_default = {}

        self.url = os.getenv("api_url")

    @retry(5, 3)
    def apis(self, url=None, data=None, params=None, headers=None, method=None, path=None):
        """
        :return:
        """
        try:

            headers = dict(self.headers_default, **headers) if headers else self.headers_default
            params = dict(self.params_default, **params) if params else self.params_default

            if "Content-Type" in headers:
                if "multipart/form-data" in headers['Content-Type']:
                    data = data
                else:
                    if type(data) == list:
                        data = data
                    else:
                        data = dict(self.data_default, **data) if data else self.data_default

            if "Content-Type" in headers:
                if "application/json" in headers['Content-Type']:
                    data = json.dumps(data)

            url = url if url else os.getenv('api_url') + path

            res = http_request(url, method, data=data, params=params, headers=headers, )

            return res

        except Exception as e:
            raise f"{url}:接口请求抛出异常：{e}"
