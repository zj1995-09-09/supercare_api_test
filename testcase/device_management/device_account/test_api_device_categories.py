# coding:utf-8
import json
import os

import pytest
from common import api_tools
from testcase.device_management.device_account_steps import ApisUtils as steps


def setup():

    # 预置创建设备资产
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

    device_id = steps().add_asset(data=data)
    os.environ["device_id"] = device_id


@pytest.mark.bvt
@pytest.mark.single
def test_get_device_info(get_global_data):
    """
    修改设备诊断记录 ----> 后续需要验证存在诊断记录后查询
    """
    device_id = os.environ["device_id"]
    res = steps().device_categories(device_id=device_id)


def teardown():
    device_id = os.environ["device_id"]
    steps().delete_asset(device_id)
