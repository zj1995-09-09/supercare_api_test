# coding:utf-8
import json
import os

import pytest
from datetime import datetime
from common import api_tools
from apis.device_management.apis_device_account import Apis
from testcase.device_management.device_account_steps import ApisUtils as steps


class TestAddBatchAsset:

    def setup_class(self):

        # 预置创建设备资产(type=40)
        suffix = api_tools.random_str(6)
        device_name = f"接口自动化测试-{suffix}"
        asset_type = 40
        pid = steps().get_company_id_with_company_name()
        category = steps().get_devices_classify()

        data = {
            "data": {
                "monitorMode": 2,
                "name": device_name,
                "category": category,
                "partNameplates": [{"name": "Gearbox"}, {"name": "Alternator"}, {"name": "MainBearing"}],
                "extraProperties": {},
                "responsibleUserIds": [],
                "deviceType": "",
                "type": asset_type,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Device"
        }

        self.device_id = steps().add_asset(data=data)
        os.environ['device_id'] = self.device_id

        # 预置在上述设备下创建一个动态量资产(type=40)
        suffix = api_tools.get_time_suffix()
        point_name = f"接口自动化测试-{suffix}"
        asset_type = 80
        pid = self.device_id

        data = {
            "data": {
                "type": asset_type,
                "pointType": "0000",
                "monitorMode": 2,
                "name": point_name,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Point"
        }

        self.point_id = steps().add_asset(data=data)

    @pytest.mark.bvt
    @pytest.mark.single
    def test_add_batch_asset(self):
        """
        动态量下添加测量定义
        """
        point_id = self.point_id
        asset_type = 90

        lower_freq = 2
        upper_freq = 10
        data_length = 1024
        wave_type = 0

        wave_type_dict = {
            0: "加速度",   # Accelerated speed
            1: "速度",    # Speed
            2: "位移"  # Displacement
        }
        wave_unit_dict = {
            0: "Accelerated speed",
            1: "Speed",
            2: "Displacement"
        }

        name = f"{data_length/1024}k {wave_type_dict[wave_type]}波形({lower_freq}-{upper_freq})"

        params = {
            "_t": datetime.now()
        }
        data = {
            "measurements": [
                {
                    "type": asset_type,
                    "isDisplayable": True,
                    "engineerUnitFamily": wave_unit_dict[wave_type],
                    "name": name,
                    "parent": point_id,
                    "extraProperties": {
                        "SignalType": 0,
                        "LowerFreq": lower_freq,
                        "UpperFreq": upper_freq,
                        "DataLength": data_length,
                        "SamplingMode": 0
                    }
                }
            ]
        }

        res = Apis().api_add_batch_asset(data=data, params=params)
        assert res.status_code <= 400, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"

    def teardown_class(self):
        device_id = os.getenv("device_id")
        steps().delete_asset(asset_id=device_id)
