# coding:utf-8
import os

import pytest
from common import api_tools
from testcase.device_management.device_account_steps import ApisUtils as steps


def setup():

    # 预置创建产线、设备资产
    suffix = api_tools.random_str(6)
    line_name = f"接口自动化测试-{suffix}"
    asset_line_type = 20
    device_name = f"接口自动化测试-{suffix}"
    asset_device_type = 40

    pid = steps().get_company_id_with_company_name()

    data = {
        "data": {
            "name": line_name,
            "extraProperties": {
                "TotalEuipmentNum": 1000
            },
            "type": asset_line_type,
            "parent": pid
        },
        "sign": "post",
        "AssetType": "Organization"
    }
    line_id = steps().add_asset(data=data)

    os.environ["line_id"] = line_id

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
            "type": asset_device_type,
            "parent": line_id
        },
        "sign": "post",
        "AssetType": "Device"
    }

    device_id = steps().add_asset(data=data)
    os.environ["device_id"] = device_id


@pytest.mark.bvt
@pytest.mark.single
def test_get_devices_and_sub_dev(get_global_data):
    """
    获取设备详细位置信息
    """
    device_id = get_global_data('device_id')
    line_id = get_global_data('line_id')
    res = steps().get_devices_and_sub_dev(pid=line_id,)
    assert device_id in [i['id'] for i in res], f"{line_id}下创建{device_id}后，未查取到对应资产"


def teardown():
    line_id = os.environ["line_id"]
    steps().delete_asset(line_id)
