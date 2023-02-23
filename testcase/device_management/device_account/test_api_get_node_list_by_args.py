# coding:utf-8
import json
import pytest
import os
from apis.apis_device_account import Apis
from testcase.device_management.device_account_steps import ApisUtils as steps


def setup():
    os.environ['company_id'] = steps().get_company_id_with_company_name()


@pytest.mark.bvt
@pytest.mark.single
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_node_list_by_args(get_global_data):

    pid = get_global_data('company_id')

    data = {
        "type": "asset",
        "parentId": pid,
        "checkedIds": [],
        "all": False,
        "openVibrationZone": False,

    }
    res = Apis().api_get_node_list_by_args(data=data)
    assert res.status_code <= 400, "Http请求状态码错误"
    assert json.loads(res.text)['success'] is True, "业务接口返回False"
    assert len(json.loads(res.text)['data']) == 1, "业务数据获取异常"
