# coding:utf-8
import os
from datetime import datetime
from apis.base import Base


class Apis(Base):
    """
    单接口
    """

    def __init__(self):

        super(Apis, self).__init__()

    def api_user_message(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies")
        }
        self.data_default = {}
        self.params_default = {
            "_t": datetime.now()
        }
        method = "get"
        url = self.url + "/api/CheckNoticeController/userMessage"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res
