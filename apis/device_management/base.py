# coding:utf-8

import json
from common.request_module import http_request
from common.tools import retry
import os


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
    def apis(self, data=None, params=None, headers=None, method=None, url=None, ):
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

            print(f"METHOD:  {method}")
            print(f"PARAMS:  {params}")
            print(f"DATA:  {data}")
            print(f"URL:  {url}")

            res = http_request(url, method, data=data, params=params, headers=headers, )

            # print(f"RESULT:  {res.text}")

            return res

        except Exception as e:
            raise e
