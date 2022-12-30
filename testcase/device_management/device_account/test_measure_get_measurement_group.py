# coding:utf-8
import json
import pytest
from datetime import datetime
from apis.device_management.device_account.apis_device_account import Apis


@pytest.mark.bvt
@pytest.mark.device
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_measurement_group():
    """
    获取默认采集定义信息
    """
    try:
        params = {
            "skipCount": 0,
            "maxResultCount": 99999,
            "_t": datetime.now()
        }

        res = Apis().api_measure_get_measurement_group(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['data']['totalCount'] > 0, "预置的采集定义数量为零！ "
        for i in json.loads(res.text)['data']['items']:
            assert i['type'] == 90, "存在type不等于90的预置采集定义"

    except Exception as e:
        raise e
