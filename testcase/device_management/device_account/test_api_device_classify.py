# coding:utf-8
import json
import pytest
from apis.device_management.apis_device_account import Apis
from datetime import datetime


@pytest.mark.bvt
@pytest.mark.single
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_devices_classify():

    params = {
        "SkipCount": 0,
        "MaxResultCount": 99999,
        "_t": datetime.now()
    }
    res = Apis().api_device_classify(params=params)
    assert res.status_code <= 400, "Http请求状态码错误"
    assert json.loads(res.text)['totalCount'] > 0, "业务接口获取异常，设备分类数量为0"
