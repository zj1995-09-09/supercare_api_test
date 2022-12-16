# coding:utf-8
import json, pytest
from apis.device_management.device_account.apis_device_account import Apis, CommonApis
from datetime import datetime

pid = ""


def setup():
    '''
    根据企业名称获取pid
    :return:
    '''
    try:
        global pid

        company_name = '111'
        pid = CommonApis().get_company_id_with_company_name(company_name)
        assert pid is not None, "根据企业名称获取企业ID失败"

    except Exception as e:
        raise e


@pytest.mark.pro
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_add_branch_factory(set_global_data):
    try:

        global pid

        now_data_time = datetime.now()
        suffix = now_data_time.strftime('%H_%M_%S')

        industry = "IndustryType_FD"
        branch_factory_name = f"分厂-{suffix}"
        contacter = "Admin管理员"
        telephone = "13199999999"

        data = {
            "data": {
                "industry": industry,
                "name": branch_factory_name,
                "contacter": contacter,
                "telephone": telephone,
                "type": 10,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Organization"
        }

        res = Apis().api_crud_asset_operator(data=data)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        assert json.loads(res.text)['data']['id'], "业务接口返回未获取到分厂id"
        set_global_data('branch_factory_id', json.loads(res.text)['data']['id'])

    except Exception as e:
        raise e


@pytest.mark.pro
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_add_factory_line(set_global_data, get_global_data):
    try:

        branch_factory_id = get_global_data("branch_factory_id")

        now_data_time = datetime.now()
        suffix = now_data_time.strftime('%H_%M_%S')

        line_name = f"产线-{suffix}"
        contacter = "Admin管理员"
        telephone = "13199999999"

        data = {
            "data": {
                "name": line_name,
                "contacter": contacter,
                "telephone": telephone,
                "extraProperties": {
                    "TotalEuipmentNum": 100
                },
                "type": 10,
                "parent": branch_factory_id
            },
            "sign": "post",
            "AssetType": "Organization"
        }

        res = Apis().api_crud_asset_operator(data=data)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        assert json.loads(res.text)['data']['id'], "业务接口返回未获取到产线id"
        set_global_data('factory_line_id', json.loads(res.text)['data']['id'])

    except Exception as e:
        raise e


@pytest.mark.pro
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_delete_factory_line(get_global_data):
    try:

        factory_line_id = get_global_data('factory_line_id')
        params = {
            "id": factory_line_id
        }

        res = Apis().api_del_choice_asset_info(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        assert json.loads(res.text)['data'] is True, "业务接口返回False"

    except Exception as e:
        raise e


@pytest.mark.pro
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_delete_branch_factory(get_global_data):
    try:

        branch_factory_id = get_global_data('branch_factory_id')

        params = {
            "id": branch_factory_id
        }

        res = Apis().api_del_choice_asset_info(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        assert json.loads(res.text)['data'] is True, "业务接口返回False"

    except Exception as e:
        raise e
