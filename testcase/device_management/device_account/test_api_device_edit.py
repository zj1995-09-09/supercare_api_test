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
    修改设备详细位置信息
    """
    device_id = get_global_data('device_id')

    res = steps().get_device_detail_info(device_id)
    data = json.loads(res.text)['data']
    data['name'] = "修改后的设备名称-test"
    data['note'] = "添加一行备注信息-test"
    data['nameplate']['note'] = "添加另外一行备注信息-test"

    res = steps().edit_device_info(data_edit=data)
    assert json.loads(res.text)['data']['data']['name'] == "修改后的设备名称-test", "修改设备详细位置信息name错误"
    assert json.loads(res.text)['data']['data']['note'] == "添加一行备注信息-test", "修改设备详细位置信息note错误"
    assert json.loads(res.text)['data']['data']['nameplate']['note'] == "添加另外一行备注信息-test", "修改设备详细位置信息nameplate.note错误"


def teardown():
    device_id = os.environ["device_id"]
    steps().delete_asset(device_id)
