# coding:utf-8
import json
import pytest
from datetime import datetime
from apis.device_management.apis_device_account import Apis


@pytest.mark.bvt
@pytest.mark.single
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_model_templates_by_type():

    params = {
        "type": 0,
        "_t": datetime.now()
    }

    res = Apis().api_model_templates_by_type(params=params)
    assert res.status_code <= 400, "Http请求状态码错误"
    assert len(json.loads(res.text)['instances']) > 0, "采集规格为空！"
