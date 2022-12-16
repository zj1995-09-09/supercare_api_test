# coding:utf-8
import json
import pytest
from apis.device_management.device_account.apis_device_account import Apis, CommonApis
from datetime import datetime


@pytest.mark.bvt
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_devices_classify():
    try:

        params = {
            "SkipCount": 0,
            "MaxResultCount": 99999,
            "_t": datetime.now()
        }
        res = Apis().api_device_classify(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['totalCount'] > 0, "业务接口获取异常，设备分类数量为0"
        # assert len(json.loads(res.text)['data']['items']) > 1 or len(
        #     json.loads(res.text)['data']['items']) == 60, "业务数据获取异常"

    except Exception as e:
        raise e
