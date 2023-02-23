# coding:utf-8
import os

import pytest
from common import api_tools
from testcase.device_management.device_account_steps import ApisUtils as steps


def setup():

    # 预置创建产线、设备资产
    suffix = api_tools.random_str(6)
    device_name = f"接口自动化测试-{suffix}"
    asset_device_type = 40

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
            "type": asset_device_type,
            "parent": pid
        },
        "sign": "post",
        "AssetType": "Device"
    }

    device_id = steps().add_asset(data=data)
    os.environ["device_id"] = device_id


@pytest.mark.bvt
@pytest.mark.single
def test_add_devices_part(get_global_data):
    """
    获取设备详细位置信息
    """
    device_id = get_global_data('device_id')
    part_type_name = "离合器"
    describe_name = "test离合器"
    res = steps().add_device_parts(device_id=device_id, part_type_name=part_type_name, describe_name=describe_name)

    res_get_parts_list = steps().get_device_parts_by_device_id(device_id)
    assert res in [i['Id'] for i in res_get_parts_list], f"{device_id}下创建{res}后，未查询到对应设备部件"


def teardown():
    device_id = os.environ["device_id"]
    steps().delete_asset(device_id)
