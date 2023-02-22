# coding: utf-8
import pytest
import json
from apis.apis_device_account import Apis
from testcase.device_management.device_account_steps import ApisUtils as steps


class TestDelChoiceAssetInfo:

    def setup_class(self,):
        self.device_id = steps().add_device()

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
