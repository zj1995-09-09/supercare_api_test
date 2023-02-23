# coding: utf-8
import pytest
import json
from common import api_tools
from apis.apis_device_account import Apis
from testcase.device_management.device_account_steps import ApisUtils as steps


class TestDelChoiceAssetInfo:

    def setup_class(self,):

        # 预置创建设备资产
        suffix = api_tools.random_str(6)
        device_name = f"接口自动化测试-{suffix}"
        asset_type = 40
        pid = steps().get_company_id_with_company_name()
        category = steps().get_devices_classify()

        data = {
            "data": {
                "monitorMode": 2,
                "name": device_name,
                "category": category,
                "partNameplates": [{"name": "Gearbox"}, {"name": "Alternator"}, {"name": "MainBearing"}],
                "extraProperties": {},
                "responsibleUserIds": [],
                "deviceType": "",
                "type": asset_type,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Device"
        }

        self.device_id = steps().add_asset(data=data)

    @pytest.mark.bvt
    @pytest.mark.single
    def test_delete_asset(self,):
        """
        删除资源
        """
        asset_id = self.device_id

        params = {
            "id": asset_id
        }

        res = Apis().api_del_choice_asset_info(params=params)
        assert res.status_code <= 400, "删除资源Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "删除资源业务接口返回False"
        assert json.loads(res.text)['data'] is True, "删除资源业务接口返回False"
