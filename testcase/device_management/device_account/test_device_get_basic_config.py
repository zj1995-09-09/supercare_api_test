# coding:utf-8
import json,pytest
from apis.device_management.device_account.apis_device_account import Apis, CommonApis
from datetime import datetime


@pytest.mark.bvt
@pytest.mark.device
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_basic_config():
    try:
        params = {
            "key": "ProductVersion",
            "_t": datetime.now(),

        }
        res = Apis().api_get_basic_config(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        assert json.loads(res.text)['data']['ProductVersion'] == "Standard", "业务数据异常"

    except Exception as e:
        raise e
