# coding:utf-8
import json, pytest
from apis.device_management.apis_device_account import Apis
from datetime import datetime


@pytest.mark.bvt
@pytest.mark.single
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_dics_by_code():

    params = {
        "code": "MontiorDifficulty",    # ImportantLevel,SpecialCategory,Specialty
        "_t": datetime.now()
    }

    res = Apis().api_get_dics_by_code(params=params)
    assert res.status_code <= 400, "Http请求状态码错误"
    assert json.loads(res.text)['success'] is True, "业务接口返回False"
    assert len(json.loads(res.text)['data']) == 3, "监控难度应预置为简单，中等，困难"
