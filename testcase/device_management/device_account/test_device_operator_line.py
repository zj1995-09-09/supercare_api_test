# coding:utf-8
import json, pytest
from apis.device_management.device_account.apis_device_account import Apis, CommonApis
from datetime import datetime

pid = ""


class TestLine:

    def setup_class(self,):
        """
        根据企业名称获取pid
        :return:
        """

        try:

            company_name = '111'
            self.pid = CommonApis().get_company_id_with_company_name(company_name)
            assert self.pid is not None, "根据企业名称获取企业ID失败"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.line
    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_add_factory_line(self, set_global_data, get_global_data):
        try:

            now_data_time = datetime.now()
            suffix = now_data_time.strftime('%H_%M_%S')

            line_name = f"产线xxx-{suffix}"
            contacter = "Admin管理员"
            telephone = "13199999999"

            set_global_data("line_info", {
                "line_name": line_name,
                "contacter": contacter,
                "telephone": telephone
            })

            data = {
                "data": {
                    "name": line_name,
                    "contacter": contacter,
                    "telephone": telephone,
                    "extraProperties": {
                        "TotalEuipmentNum": 100
                    },
                    "type": 20,
                    "parent": self.pid
                },
                "sign": "post",
                "AssetType": "Organization"
            }

            res = Apis().api_crud_asset_operator(data=data)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回False"
            assert json.loads(res.text)['data']['id'], "业务接口返回未获取到产线id"
            set_global_data('factory_line_id', json.loads(res.text)['data']['id'])

            assert CommonApis().verify_nodes_exist(pid=self.pid, asset_name=line_name), "设备树中未查询到资产"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.line
    @pytest.mark.run(order=2)
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_get_line_detail(self, get_global_data):
        try:

            factory_line_id = get_global_data('factory_line_id')
            data = {
                "data": {
                    "id": factory_line_id
                },
                "AssetType": "Organization",
                "sign": "get"
            }

            res = Apis().api_crud_asset_operator(data=data, )
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回False"

            line_info = get_global_data("line_info")
            assert json.loads(res.text)['data']['name'] == line_info['line_name'], "业务接口信息返回错误"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.line
    @pytest.mark.run(order=3)
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_modify_line_detail(self, get_global_data):
        try:

            factory_line_id = get_global_data('factory_line_id')

            line_name_new = "产线-New"
            contacter_new = "Admin管理员111"
            telephone_new = "13199999998"

            data = {
                "data": {
                    "name": line_name_new,
                    "contacter": contacter_new,
                    "telephone": telephone_new,
                    "id": factory_line_id,
                    "parent": self.pid,  # *
                    "type": 20  # *
                },
                "AssetType": "Organization",
                "sign": "post"
            }

            params = {
                "_t": datetime.now()
            }

            res = Apis().api_crud_asset_operator(data=data, params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回False"
            assert json.loads(res.text)['data']['name'] == line_name_new, "业务接口信息修改返回错误"
            assert json.loads(res.text)['data']['contacter'] == contacter_new, "业务接口信息修改返回错误"
            assert json.loads(res.text)['data']['telephone'] == telephone_new, "业务接口信息修改返回错误"
            assert CommonApis().verify_nodes_exist(pid=self.pid, asset_name=line_name_new), "设备树中未查询到资产"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.line
    @pytest.mark.run(order=4)
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_copy_line(self, get_global_data):
        try:

            factory_line_id = get_global_data('factory_line_id')

            params = {
                "assetId": factory_line_id,
                "_t": datetime.now()
            }

            res = Apis().api_get_asset_count(params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回False"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.line
    @pytest.mark.run(order=5)
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_paste_line(self, set_global_data, get_global_data):
        try:

            factory_line_id = get_global_data('factory_line_id')

            params = {
                "assetId": factory_line_id,
                "targetId": self.pid,
                "copy": True,
                "_t": datetime.now()
            }

            res = Apis().api_paste_assets(params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['assets'][0]['organizations'][0]['id'], "业务接口返回值异常，未获取到复制后的asset id"

            copy_line_id = json.loads(res.text)['assets'][0]['organizations'][0]['id']
            assert CommonApis().verify_nodes_exist(pid=self.pid, asset_id=copy_line_id), "设备树中未查询到资产"

            set_global_data("copy_line_id", copy_line_id)

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.line
    @pytest.mark.run(order=100)
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_delete_factory_line(self, get_global_data):
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

    @pytest.mark.bvt
    @pytest.mark.line
    @pytest.mark.run(order=100)
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_delete_copied_line(self, get_global_data):
        try:

            copy_line_id = get_global_data('copy_line_id')
            params = {
                "id": copy_line_id
            }

            res = Apis().api_del_choice_asset_info(params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回False"
            assert json.loads(res.text)['data'] is True, "业务接口返回False"

        except Exception as e:
            raise e
