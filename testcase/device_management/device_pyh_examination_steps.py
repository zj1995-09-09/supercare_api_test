# coding: utf-8
import os
from apis.device_management.apis_device_pyh_examination import Apis
from common.api_tools import retry, random_str
import json
from datetime import datetime
import time


class ApisUtils(Apis,):
    """
    由apis构成steps
    """
    @retry(3, 5)
    def get_report_year(self):
        """
        获取列表可选年份
        返回年份列表
        """
        params = {
            "_t": datetime.now()
        }
        res = self.api_get_report_year(params=params)
        assert res.status_code <= 400, "获取设备体检列表可选年份Http请求状态码错误"
        assert len(json.loads(res.text)['data']) > 0, "获取设备体检列表可选年份为空"
        return json.loads(res.text)['data']

    @retry(5, 5)
    def get_report_info_with_name(self, name) -> dict:
        """
        获取设备体检列表
        返回体检报告详情
        """
        params = {
            "Year": 0,
            "skipCount": 0,
            "maxResultCount": 10000,
            "_t": datetime.now()
        }
        res = self.api_get_reports(params=params)
        assert res.status_code <= 400, "获取设备体检列表Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "获取设备体检列表业务接口返回False"

        for i in json.loads(res.text)['data']['items']:
            if i['name'] == name:
                return i
        assert False, f"未获取到名称为{name}的体检报告"

    @retry(3, 5)
    def dispoable_plan(self, device_id, report_name):
        """
        手动添加体检报告
        """

        plan_name_x, plan_name_y = str(time.time()).split(".")
        now_data_time = datetime.now()

        params = {
            "_t": datetime.now()
        }

        data = {
            "planName": plan_name_x + plan_name_x[0:3],
            "reportName": report_name,
            "assetRange": [
                {
                    "id": device_id,
                    "name": "0"
                }
            ],
            "startTime": f"{str(now_data_time.strftime('%Y-%m-%d'))} 00:00:00",
            "endTime": f"{str(now_data_time.strftime('%Y-%m-%d'))} 23:59:59"
        }

        res = self.api_dispoable_plan(data=data, params=params)
        assert res.status_code <= 400, "手动添加设备体检报告Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "手动添加设备体检报告业务接口返回False"

        return json.loads(res.text)['data']

    @retry(3, 5)
    def delete_report(self, report_id):
        """
        删除设备体检报告
        """

        params = {
            "id": report_id,
            "_t": datetime.now()
        }

        res = self.api_delete_report(params=params)
        assert res.status_code <= 400, "删除设备体检报告Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "删除设备体检报告业务接口返回False"

    @retry(3, 5)
    def get_plans(self):
        """
        获取自动体检列表
        """
        params = {
            "_t": datetime.now()
        }
        res = self.api_get_plans(params=params)

    @retry(3, 5)
    def get_plan_global_setting(self, ):
        """
        获取自动体检截图设置
        """
        params = {
            "_t": datetime.now()
        }
        res = self.api_get_plan_global_setting(params=params)
        assert res.status_code <= 400, "获取自动体检截图设置Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "获取自动体检截图设置业务接口返回False"

        return json.loads(res.text)['data']

    @retry(3, 5)
    def set_plan_global_setting(self, definition: list, trend):
        """
        设置自动体检截图设置
        """

        data = {
            "acquisitionDefinition": definition,
            "trendRange": trend,
            "normalAnalysis": True
        }

        params = {
            "_t": datetime.now()
        }

        res = self.api_set_plan_global_setting(data=data, params=params)
        assert res.status_code <= 400, "设置自动体检截图设置Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "设置自动体检截图设置业务接口返回False"

    @retry(3, 5)
    def add_or_edit_plan(self, plan_name, report_name, asset_id, asset_name):
        """
        添加或编辑自动体检计划
        这里选择assetid，assetname时，若是产线下仅存在一个设备，那么选择此设备时，就会选择他的最上层资产传参
        """
        params = {
            "_t": datetime.now()
        }
        data = {
            "planName": plan_name,
            "genDay": 1,
            "cycle": 1,
            "assetRange": [
                {
                    "id": asset_id,
                    "name": asset_name
                }
            ],
            "reportName": report_name,
            "state": True
        }
