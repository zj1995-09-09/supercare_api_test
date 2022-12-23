# coding:utf-8
import json,pytest
from apis.device_management.device_phy_examination.apis_device_pyh_examination import Apis, CommonApis


@pytest.mark.bvt
@pytest.mark.device
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_phy_get_report_year():
    try:

        res = Apis().api_get_report_year()
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False "

    except Exception as e:
        raise e
