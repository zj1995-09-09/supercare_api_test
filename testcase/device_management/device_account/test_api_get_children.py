# coding:utf-8
import json
import pytest
from apis.apis_device_account import Apis


@pytest.mark.bvt
@pytest.mark.single
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_api_get_children():

    res = Apis().api_get_children()
    assert res.status_code <= 400, "Http请求状态码错误"
    assert json.loads(res.text)['success'] is True, "业务接口返回False"
