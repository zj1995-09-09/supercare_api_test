# coding:utf-8
import json
import pytest
from apis.device_management.device_account.apis_device_account import Apis


@pytest.mark.bvt
@pytest.mark.device
@pytest.mark.temp
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_by_asset_types():
    """
    获取设备模型
    """
    try:

        res = Apis().api_by_asset_types()
        assert res.status_code <= 200, "Http请求状态码错误"
        assert len(json.loads(res.text)) > 0, "业务接口返回类型数量为零"

    except Exception as e:
        raise e
