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
def test_delete_images(get_global_data):
    """
    删除已设置的设备总览图
    :param get_global_data:
    :return:
    """
    guid = get_global_data("guid")
    params = {
        'ids': guid,
        '_t': datetime.now()
    }

    res = Apis().api_device_delete_images(params=params, )
    assert res.status_code <= 200, "Http请求状态码错误"
    assert json.loads(res.text)['success'] is True, "业务接口返回False"

def teardown():
    device_id = os.environ['device_id']
    steps().delete_asset(device_id)
