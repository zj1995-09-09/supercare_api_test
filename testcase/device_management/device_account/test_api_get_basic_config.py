# coding:utf-8
import json
import pytest
import os
from datetime import datetime
from apis.apis_device_account import Apis


@pytest.mark.bvt
@pytest.mark.single
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_basic_config():
    """
    获取当前系统版本类型（标准版，专业版）Professional
    """
    params = {
        "key": "ProductVersion",
        "_t": datetime.now(),
    }
    res = Apis().api_get_basic_config(params=params)
    assert res.status_code <= 400, "Http请求状态码错误"
    assert json.loads(res.text)['success'] is True, "业务接口返回False"
    assert json.loads(res.text)['data']['ProductVersion'] == os.getenv("supercare_type"), f"系统版本数据异常:{os.getenv('supercare_type')}"

