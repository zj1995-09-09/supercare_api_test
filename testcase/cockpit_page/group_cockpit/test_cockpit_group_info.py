# coding:utf-8
import json
import pytest
from apis.cockpit_page.group_cockpit.apis_group_cockpit import Apis
from datetime import datetime


@pytest.mark.temp
@pytest.mark.cockpit
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_page_layout():
    """
    页面布局？
    """
    try:
        params = {
            "skipCount": 0,
            "maxResultCount": 99999,
            "_t": datetime.now()
        }

        res = Apis().api_page_layout(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"

    except Exception as e:
        raise e


@pytest.mark.temp
@pytest.mark.cockpit
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_system_layout_get_list():
    """
    不晓得这个接口是获取什么的
    """
    try:
        params = {
            "pageCode": "system.overview.group",
            "maxResultCount": 1,
            "skipCount": 0,
            "_t": datetime.now()
        }

        res = Apis().api_system_layout_get_list(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'], "接口业务返回False"

    except Exception as e:
        raise e
