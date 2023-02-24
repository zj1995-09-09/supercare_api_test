# coding:utf-8
import time
import os
import pytest
from datetime import datetime
from testcase.device_management.device_account_steps import ApisUtils as device_account_steps
from testcase.device_management.device_pyh_examination_steps import ApisUtils as pyh_steps
from common import api_tools


def setup():

    # 预置创建设备资产
    suffix = api_tools.random_str(6)
    device_name = f"接口自动化测试-{suffix}"
    asset_device_type = 40

    pid = device_account_steps().get_company_id_with_company_name()

    category = device_account_steps().get_devices_classify()

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

    device_id = device_account_steps().add_asset(data=data)
    os.environ["device_id"] = device_id


@pytest.mark.bvt
@pytest.mark.single
def test_phy_dispoable_plan(get_global_data, set_global_data):

    device_id = get_global_data('device_id')

    suffix = api_tools.random_str(6)
    report_name = f"AT手动生成报告-{suffix}"

    pyh_steps().dispoable_plan(device_id=device_id, report_name=report_name)

    res_get_report = pyh_steps().get_report_info_with_name(name=report_name)
    print(res_get_report)
    assert res_get_report['wordFilePath'], f"对应生成的name为{report_name}的报告没有docx文件"
    assert res_get_report['pdfFilePath'], f"对应生成的name为{report_name}的报告没有pdf文件"

    set_global_data('report_id', res_get_report['id'])


def teardown():
    """
    清理设备
    """
    device_id = os.environ['device_id']
    device_account_steps().delete_asset(asset_id=device_id)
    report_id = os.environ['report_id']
    pyh_steps().delete_report(report_id=report_id)
