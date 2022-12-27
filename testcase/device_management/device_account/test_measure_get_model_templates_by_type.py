# coding:utf-8
import json
import pytest
from datetime import datetime
from apis.device_management.device_account.apis_device_account import Apis


@pytest.mark.bvt
@pytest.mark.device
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_model_templates_by_type():
    """
    获取默认采集规格
    """
    try:
        params = {
            "type": 0,
            "_t": datetime.now()
        }

        res = Apis().api_measure_get_model_templates_by_type(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert len(json.loads(res.text)['catalogs']) > 0, "采集规格为空！"
        assert len(json.loads(res.text)['instances']) > 0, "采集规格为空！"

    except Exception as e:
        raise e
