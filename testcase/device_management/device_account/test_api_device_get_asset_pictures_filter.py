# coding:utf-8

import pytest
import os
from datetime import datetime
from apis.apis_device_account import Apis
from common import api_tools
from testcase.device_management.device_account_steps import ApisUtils as steps


def setup():
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

    device_id = steps().add_asset(data=data)
    os.environ['device_id'] = device_id


@pytest.mark.single
@pytest.mark.bvt
def test_get_device_general_view_get_asset_pictures_filter(get_global_data):
    """
    获取设备总览图信息
    :param get_global_data:
    :return:
    """

    device_id = get_global_data('device_id')
    data = {
        "assetIds": [device_id],
        "dimessions": [0],
        "groups": []
    }
    params = {
        "_t": datetime.now()
    }

    res = Apis().api_get_asset_pictures_filter(data=data, params=params)
    assert res.status_code <= 400, "Http请求状态码错误"


def teardown():
    device_id = os.environ['device_id']
    steps().delete_asset(device_id)
