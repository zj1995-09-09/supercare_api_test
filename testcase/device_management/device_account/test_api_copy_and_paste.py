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

    company_id = steps().get_company_id_with_company_name()
    os.environ["company_id"] = company_id


@pytest.mark.bvt
@pytest.mark.single
def test_copy_and_paste(set_global_data, get_global_data):
    """
    获取设备详细位置信息
    """
    device_id = get_global_data('device_id')
    company_id = get_global_data('company_id')
    target_id = steps().copy_paste_asset(source_id=device_id, target_id=company_id)

    set_global_data("target_id", target_id)

    res = steps().get_device_detail_info(target_id)
    assert json.loads(res.text)['success'] is True, "复制粘贴后的设备无法查询到"


def teardown():
    device_id = os.environ["device_id"]
    target_id = os.environ["target_id"]
    steps().delete_asset(device_id)
    steps().delete_asset(target_id)
