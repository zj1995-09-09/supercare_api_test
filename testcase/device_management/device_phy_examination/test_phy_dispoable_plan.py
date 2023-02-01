# coding:utf-8
import json
import time

import pytest
from datetime import datetime
from apis.device_management.device_phy_examination.apis_device_pyh_examination import Apis
from apis.device_management.device_phy_examination.apis_device_pyh_examination import CommonApis as PHY_CommonApis
from apis.device_management.device_account.apis_device_account import CommonApis

device_id = ""

def setup():
    """
    新建设备
    """
    global device_id
    device_id = CommonApis().add_device()


@pytest.mark.bvt
@pytest.mark.device
@pytest.mark.run(order=1)
def test_phy_dispoable_plan(set_global_data):
    try:
        global device_id

        params = {
            "_t": datetime.now()
        }
        plan_name_x,plan_name_y = str(time.time()).split(".")

        now_data_time = datetime.now()
        suffix = now_data_time.strftime('%H_%M_%S')
        report_name = f"设备体检报告-{suffix}"

        data = {
            "planName": plan_name_x+plan_name_x[0:3],
            "reportName": report_name,
            "assetRange": [
                {
                    "id": device_id,
                    "name": "0"
                }
            ],
            "startTime": f"{str(now_data_time.strftime('%Y-%m-%d'))} 00:00:00",
            "endTime": f"{str(now_data_time.strftime('%Y-%m-%d'))} 23:59:59"
        }

        res = Apis().api_dispoable_plan(params=params, data=data)
        assert res.status_code <= 200, "Http请求状态码错误"
        res = PHY_CommonApis().verify_report_exist_with_name(name=report_name)
        assert res, "未查询到对应的体检报告"

        report_info = PHY_CommonApis().get_report_info_with_name(name=report_name)
        assert report_info['pdfFilePath'], "生成的体检报告无pdf文件信息"

        set_global_data("report_id", report_info['id'])
        set_global_data("report_name", report_name)

    except Exception as e:
        raise e


@pytest.mark.bvt
@pytest.mark.device
@pytest.mark.run(order=1)
def test_phy_delete_report(get_global_data):
    """
    """
    try:
        report_id = get_global_data("report_id")
        report_name = get_global_data("report_name")

        params = {
            "id": report_id,
            "_t": datetime.now()
        }
        res = Apis().api_delete_report(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"

        res = PHY_CommonApis().verify_report_exist_with_name(name=report_name)
        assert not res, "未成功删除对应体检报告"

    except Exception as e:
        raise e

def teardown():
    """
    清理设备
    """
    global device_id, report_id
    CommonApis().delete_device(device_id)

