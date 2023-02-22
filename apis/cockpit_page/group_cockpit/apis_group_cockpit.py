# coding:utf-8

import json
import os
from datetime import datetime
from apis.base import Base
from common.api_tools import retry
from common.m_exceptions import DException as Exc

class Apis(Base):
    """
    单接口
    """

    def __init__(self):

        super(Apis, self).__init__()

    def api_page_layout(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:

            self.headers_default = {
                "Authorization": os.getenv("cookies")
            }
            self.data_default = {}
            self.params_default = {
                "_t": datetime.now()
            }
            method = "get"
            url = self.url + "/api/basicService/api/app/pageLayout"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e

    def api_system_layout_get_list(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:

            self.headers_default = {
                "Authorization": os.getenv("cookies")
            }
            self.data_default = {}
            self.params_default = {
                "_t": datetime.now()
            }
            method = "get"
            url = self.url + "/api/systemLayout/getList"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e

    def api_pre_main_statistics(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:

            self.headers_default = {
                "Authorization": os.getenv("cookies"),
                "Accept-Language": "zh-Hans"
            }
            self.data_default = {}
            self.params_default = {
                "_t": datetime.now()
            }
            method = "get"
            url = self.url + "/api/Case/PreMaintainStatistics"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e

    def api_fault_device_statistic_list(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:

            self.headers_default = {
                "Authorization": os.getenv("cookies"),
                "Content-Type": "application/json"
            }
            self.data_default = {}
            self.params_default = {
                "_t": datetime.now()
            }
            method = "get"
            url = self.url + "/api/alarmService/api/app/fault/faultDeviceStatisticList"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e

    def api_fault_device_mantains(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:

            self.headers_default = {
                "Authorization": os.getenv("cookies"),
                "Content-Type": "application/json"
            }
            self.data_default = {}
            self.params_default = {
                "_t": datetime.now()
            }
            method = "get"
            url = self.url + "/api/alarmService/api/app/fault/deviceMaintains"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e

class CommonApis(Apis):
    """
    常用业务方法
    """
