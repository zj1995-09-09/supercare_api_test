# coding:utf-8
import json
import pytest
from datetime import datetime
from apis.device_management.device_phy_examination.apis_device_pyh_examination import Apis
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
@pytest.mark.temp
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_phy_get_user_manage_device_tree():
    try:
        global device_id

        params = {
            "_t": datetime.now()
        }
        data = {}

        res = Apis().api_get_user_manage_device_tree(params=params, data=data)
        assert res.status_code <= 200, "Http请求状态码错误"
        flag = False
        for i in json.loads(res.text):
            if i['id'] == device_id:
                flag = True
                break
        assert flag is True, "未查询到新建的设备信息"

    except Exception as e:
        raise e
