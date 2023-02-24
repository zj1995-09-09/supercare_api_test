# coding:utf-8
import json
import pytest
from apis.device_management.apis_device_account import Apis
from datetime import datetime
import os
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

    # 设置设备背景图
    file = r"{}\files\设备图片.png".format(os.getcwd())

    guid = steps().upload_device_pictures(file=file, device_id=device_id)

    os.environ["guid"] = guid


@pytest.mark.bvt
@pytest.mark.single
def test_set_picture_background(get_global_data):
    """
    设置背景
    """
    guid = get_global_data("guid")
    device_id = get_global_data("device_id")
    params = {
        'guid': guid,
        'isDefault': True,
        '_t': datetime.now()
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = Apis().api_set_background_picture(params=params, headers=headers)
    assert res.status_code <= 400, "设备设置背景Http请求状态码错误"

    res = steps().get_device_general_view(device_id)
    assert json.loads(res.text)[0]['isDefault'], "设备设置背景后isDefault字段为False"

def teardown():
    device_id = os.environ["device_id"]
    steps().delete_asset(device_id)
