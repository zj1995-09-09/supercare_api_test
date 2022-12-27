# coding:utf-8
import json
import pytest
from datetime import datetime
from apis.device_management.device_phy_examination.apis_device_pyh_examination import Apis


@pytest.mark.bvt
@pytest.mark.device
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_phy_get_reports():
    try:
        params = {
            "Year": 0,
            "skipCount": 0,
            "maxResultCount": 30,
            "_t": datetime.now()
        }

        res = Apis().api_get_reports(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False "
        assert json.loads(res.text)['data']['totalCount'] > 0, "业务查询到的数据为空 "

    except Exception as e:
        raise e
