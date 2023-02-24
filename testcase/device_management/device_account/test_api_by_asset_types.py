# coding: utf-8
import json
import pytest
from apis.device_management.apis_device_account import Apis
from datetime import datetime


@pytest.mark.single
@pytest.mark.bvt
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_by_asset_types():

    params = {
        "_t": datetime.now(),
    }

    res = Apis().api_by_asset_types(params=params, url_params="assetTypes=40&assetTypes=50")
    assert res.status_code <= 400, "Http请求状态码错误"
    assert len(json.loads(res.text)) > 0, "业务接口返回类型数量为零"

