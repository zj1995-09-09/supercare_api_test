# coding:utf-8
import json,pytest
from apis.device_management.device_account.apis_device_account import Apis, CommonApis
from datetime import datetime
import os


pid = ""


def setup():
    '''
    根据企业名称获取pid
    :return:
    '''
    try:
        global pid
        company_name = os.getenv("company_name")
        pid = CommonApis().get_company_id_with_company_name(company_name)
        assert pid is not None, "根据企业名称获取企业ID失败"

    except Exception as e:
        raise e


@pytest.mark.bvt
@pytest.mark.device
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_children1():
    try:
        res = Apis().api_get_children()
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
    except Exception as e:
        raise e


@pytest.mark.bvt
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_children2():
    try:
        global pid
        data = {
            "pid": pid,
            "isBack": False
        }
        res = Apis().api_get_children(data=data)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"

    except Exception as e:
        raise e


@pytest.mark.bvt
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_children3():
    try:
        global pid
        params = {
            "type": "asset",
            "pid": pid,
            "isBack": False,
            "_t": datetime.now()
        }
        res = Apis().api_get_children(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        assert json.loads(res.text)['data']['totalCount'] > 0
        print(f"totalCount: {json.loads(res.text)['data']['totalCount']}")

    except Exception as e:
        raise e