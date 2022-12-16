# coding:utf-8
import json, pytest
from apis.device_management.device_account.apis_device_account import Apis, CommonApis
from datetime import datetime


@pytest.mark.bvt
@pytest.mark.single
@pytest.mark.device
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_dics_by_code_montior():
    try:

        params = {
            "code": "MontiorDifficulty",
            "_t": datetime.now()
        }

        res = Apis().api_device_get_dics_by_code(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        assert len(json.loads(res.text)['data']) == 3, "监控难度应预置为简单，中等，困难"

    except Exception as e:
        raise e


@pytest.mark.bvt
@pytest.mark.single
@pytest.mark.device
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_dics_by_code_important():
    try:

        params = {
            "code": "ImportantLevel",
            "_t": datetime.now()
        }

        res = Apis().api_device_get_dics_by_code(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        assert len(json.loads(res.text)['data']) == 4, "重要等级应预置为A，B，C，D"

    except Exception as e:
        raise e


@pytest.mark.bvt
@pytest.mark.single
@pytest.mark.device
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_dics_by_code_spec_type():
    try:

        params = {
            "code": "SpecialCategory",
            "_t": datetime.now()
        }

        res = Apis().api_device_get_dics_by_code(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        assert len(json.loads(res.text)['data']) == 8, "专业类别应预置为8类"

    except Exception as e:
        raise e


@pytest.mark.bvt
@pytest.mark.single
@pytest.mark.device
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_dics_by_code_spec():
    try:

        params = {
            "code": "Specialty",
            "_t": datetime.now()
        }

        res = Apis().api_device_get_dics_by_code(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        assert len(json.loads(res.text)['data']) == 28, "专业类别应预置为8类"

    except Exception as e:
        raise e
