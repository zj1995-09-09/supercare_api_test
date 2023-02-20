# coding:utf-8
import json
import pytest
import os
from apis.cockpit_page.group_cockpit.apis_group_cockpit import Apis
from apis.device_management.device_account.apis_device_account import CommonApis as DeviceCA
from datetime import datetime

pid = ""


def setup():
    """
    根据企业名称获取pid
    :return:
    """
    try:
        global pid
        company_name = os.getenv("company_name")
        pid = DeviceCA().get_company_id_with_company_name(company_name)
        assert pid is not None, "根据企业名称获取企业ID失败"

    except Exception as e:
        raise e


@pytest.mark.temp
@pytest.mark.cockpit
@pytest.mark.flaky(reruns=3, reruns_delay=3)
@pytest.mark.run(order=1)
def test_get_pre_statistics(set_global_data):
    """
    预测维护统计
    """
    try:

        params = {
            "assetId": pid,
            "_t": datetime.now()
        }

        res = Apis().api_pre_main_statistics(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"

        res_dict = json.loads(res.text)
        assert res_dict['success'], "业务接口返回False"

        expect_name_dict = {
            '预测维护': 0,
            '预测维修': 0,
            '缺陷总数': 0,
            '智能报警': 0,
            '智能诊断': 0,
            '智能体检': 0
        }

        for i in res_dict['data']:
            assert i['name'] in expect_name_dict.keys(), f"{i['name']}值不存在预期项中"

        for i in res_dict['data']:
            expect_name_dict[i['name']] = i['value']

        set_global_data("pre_statistics_dict", expect_name_dict)

    except Exception as e:
        raise e


# @pytest.mark.temp
# @pytest.mark.cockpit
# @pytest.mark.flaky(reruns=3, reruns_delay=3)
# @pytest.mark.run(order=2)
# def test_get_detail_statistics(get_global_data):
#     """
#     共有6个值请求，不想写，关键存在一个恶心参数，很蠢！更不想写了
#     """
#     pre_statistics_dict = get_global_data("pre_statistics_dict")
#     print(pre_statistics_dict)
