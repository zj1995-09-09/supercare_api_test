# coding:utf-8
import json
import os
import pytest
from datetime import datetime
from apis.apis_device_account import Apis
from testcase.device_management.device_account_steps import ApisUtils as steps


class TestCrudAssetOperator:

    def setup_class(self,):
        self.company_id = steps().get_company_id_with_company_name()
        self.device_type_code = steps().get_devices_classify()

    @pytest.mark.bvt
    @pytest.mark.single
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_crud_asset_operator_get_company_info(self,):
        """
        获取企业位置信息
        """
        pid = self.company_id

        data = {
            "AssetType": "Organization",
            "sign": "get",
            "data": {
                "id": pid
            }
        }

        params = {
            "_t": datetime.now(),
        }

        res = Apis().api_crud_asset_operator(data=data, params=params)
        assert res.status_code <= 400, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        company_type = os.getenv("company_type")
        if company_type != "":  # 专业版不存在企业类型
            assert json.loads(res.text)['data']['industry'] == company_type, f"企业类型错误:{company_type}"

    @pytest.mark.bvt
    @pytest.mark.single
    def test_crud_asset_operator_add_device(self, set_global_data):
        """
        企业下新建设备
        """
        pid = self.company_id
        device_type_code = self.device_type_code

        now_data_time = datetime.now()
        suffix = now_data_time.strftime('%H_%M_%S')
        device_name = f"接口自动化测试-{suffix}"

        params = {
            "_t": datetime.now()
        }

        data = {
            "data": {
                "name": device_name,
                "category": device_type_code,
                "extraProperties": {},
                "type": 40,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Device"
        }

        res = Apis().api_crud_asset_operator(data=data, params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        assert json.loads(res.text)['data']['id'], "业务接口返回未获取到设备id"

        set_global_data("device_id", json.loads(res.text)['data']['id'])

    def teardown_class(self,):
        device_id = os.getenv("device_id")
        steps().delete_asset(asset_id=device_id)

