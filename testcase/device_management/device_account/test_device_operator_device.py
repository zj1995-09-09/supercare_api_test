# coding:utf-8
import json
import pytest
from datetime import datetime
from common.tools import get_content_type
from apis.device_management.device_account.apis_device_account import Apis, CommonApis
from requests_toolbelt import MultipartEncoder
import random
import string
import os
import time

pid = ""


class TestDevice:

    def setup_class(self, ):
        """
        根据企业名称获取pid
        :return:
        """

        try:

            company_name = os.getenv("company_name")
            self.pid = CommonApis().get_company_id_with_company_name(company_name)
            assert self.pid is not None, "根据企业名称获取企业ID失败"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    # @pytest.mark.temp
    @pytest.mark.run(order=1)
    def test_get_devices_classify(self, set_global_data, ):
        """
        获取设备分类
        :param set_global_data: 首个设备分类类型（默认分类）
        :return:
        """
        try:

            params = {
                "SkipCount": 0,
                "MaxResultCount": 99999,
                "_t": datetime.now()
            }
            res = Apis().api_device_classify(params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['totalCount'] > 0, "业务接口获取异常，设备分类数量为0"
            code = json.loads(res.text)['items'][0]['code']
            set_global_data('device_type_code', code)

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=2)
    def test_add_factory_device(self, set_global_data, get_global_data):
        """
        企业下新建设备
        set_global_data:
        factory_device_id   设备id
        """
        try:

            now_data_time = datetime.now()
            suffix = now_data_time.strftime('%H_%M_%S')

            device_name = f"设备xxx-{suffix}"

            device_type_code = get_global_data('device_type_code')

            params = {
                "_t": datetime.now()
            }

            data = {
                "data": {
                    "name": device_name,
                    "category": device_type_code,
                    "extraProperties": {},
                    "type": 40,
                    "parent": self.pid
                },
                "sign": "post",
                "AssetType": "Device"
            }

            res = Apis().api_crud_asset_operator(data=data, params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回False"
            assert json.loads(res.text)['data']['id'], "业务接口返回未获取到设备id"
            set_global_data('factory_device_id', json.loads(res.text)['data']['id'])

            assert CommonApis().verify_nodes_exist(pid=self.pid, asset_name=device_name), "设备树中未查询到资产"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=3)
    def test_add_sub_device(self, set_global_data, get_global_data):
        """
        (分部设备)企业-设备下新建分部设备
        :param set_global_data:
        :param get_global_data:
        :return:
        """
        try:

            now_data_time = datetime.now()
            suffix = now_data_time.strftime('%H_%M_%S')

            sun_device_name = f"分部设备xxx-{suffix}"

            device_type_code = get_global_data('device_type_code')
            factory_device_id = get_global_data('factory_device_id')

            params = {
                "_t": datetime.now()
            }

            data = {
                "data": {
                    "name": sun_device_name,
                    "category": device_type_code,
                    "extraProperties": {},
                    "type": 50,
                    "monitorMode": 2,
                    "parent": factory_device_id
                },
                "sign": "post",
                "AssetType": "Device"
            }

            res = Apis().api_crud_asset_operator(data=data, params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回False"
            assert json.loads(res.text)['data']['id'], "业务接口返回未获取到设备id"
            set_global_data('sub_device_id', json.loads(res.text)['data']['id'])

            assert CommonApis().verify_nodes_exist(pid=factory_device_id, asset_name=sun_device_name), "设备树中未查询到资产"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=4)
    def test_get_device_general_view_get_asset_pictures_filter(self, get_global_data):
        """
        获取设备总览图信息
        （若不设置总览图，则返回为空）
        :param get_global_data:
        :return:
        """
        try:

            factory_device_id = get_global_data('factory_device_id')
            data = {
                "assetIds": [factory_device_id],
                "dimessions": [0],
                "groups": []
            }
            params = {
                "_t": datetime.now()
            }

            res = Apis().api_device_get_asset_pictures_filter(data=data, params=params)
            assert res.status_code <= 200, "Http请求状态码错误"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=5)
    def test_get_sub_device_general_view_get_asset_pictures_filter(self, get_global_data):
        """
        获取分部设备总览图信息
        （若不设置总览图，则返回为空）
        :param get_global_data:
        :return:
        """
        try:

            sub_device_id = get_global_data('sub_device_id')
            data = {
                "assetIds": [sub_device_id],
                "dimessions": [0],
                "groups": []
            }
            params = {
                "_t": datetime.now()
            }

            res = Apis().api_device_get_asset_pictures_filter(data=data, params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text) == []

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=6)
    def test_upload_pictures(self, get_global_data, set_global_data):
        """
        上传设备总览图
        :param get_global_data:
        :return:
        """
        try:
            randomStr = ''.join(random.sample(string.ascii_letters + string.digits, 16))
            headers = {
                "Content-Type": "multipart/form-data;boundary=----WebKitFormBoundary{rs}".format(rs=randomStr)
            }
            file_path = os.getcwd()

            file = r"{}\files\设备图片.png".format(file_path)
            filename = file.split("\\")[-1]
            filesize = os.path.getsize(file)

            r = get_content_type(file)

            fields = MultipartEncoder(
                fields={"formFiles": ("{}".format(filename), open(r"{}".format(file), "rb"), r)},
                # 新接口为formFiles，老接口为：formFile
                boundary="----WebKitFormBoundary{}".format(randomStr)
            )

            params = {
                "_t": datetime.now(),
                "groupName": "file"
            }

            res = Apis().api_device_oss_upload_mulity_file(data=fields, params=params, headers=headers)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)[0]['data']['originalUrl'], "业务接口返回异常，未获取到上传后的存储地址信息."
            originalUrl = json.loads(res.text)[0]['data']['originalUrl']
            set_global_data("originalUrl", originalUrl)
            set_global_data("picture_name", filename)
            set_global_data("picture_size", filesize)

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=7)
    def test_asset_picture_new(self, get_global_data, set_global_data):
        """
        设备总览图中，绑定上传得图片与设备
        :param get_global_data:
        :return:
        """
        try:

            factory_device_id = get_global_data('factory_device_id')
            originalUrl = get_global_data('originalUrl')
            picture_name = get_global_data('picture_name')
            picture_size = get_global_data('picture_size')

            data = [
                {
                    "group": 5,  # group含义？
                    "dimession": 0,  # 1： 3D ？ 0： 2D ？
                    "attachmentCreateDto": {
                        "address": originalUrl,
                        "name": picture_name,
                        "extension": "png",
                        "size": picture_size,
                        "url": f"/api/Oss/File?fileName={originalUrl}",
                        "response": {
                            "url": f"/api/Oss/File?fileName={originalUrl}",
                            "originalUrl": originalUrl
                        },
                        "status": "done",
                        "thumbAddress": ""
                    },
                    "uid": f"__AUTO__{int(time.time())}_0__"
                }
            ]
            params = {
                "assetId": factory_device_id,
                "_t": datetime.now()
            }

            headers = {
                "Content-Type": "application/json"
            }

            res = Apis().api_device_asset_picture_new(data=data, params=params, headers=headers)
            assert res.status_code <= 200, f"设备总览图中，绑定上传得图片与设备，Http请求状态码错误:{res.status_code}"
            assert json.loads(res.text)[0]['id'], "业务接口返回错误，未返回到对应上传绑定后的guid"
            guid = json.loads(res.text)[0]['id']
            set_global_data("guid", guid)

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=8)
    def test_set_picture_background(self, get_global_data, set_global_data):
        """
        设置已上传且绑定得图片为设备背景图
        :param get_global_data:
        :return:
        """
        try:
            guid = get_global_data("guid")
            factory_device_id = get_global_data('factory_device_id')
            params = {
                'guid': guid,
                'isDefault': True,
                '_t': datetime.now()
            }

            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }
            res = Apis().api_device_set_background_picture(params=params, headers=headers)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert CommonApis().verify_device_picture_exist(device_id=factory_device_id), "业务请求失败，背景图address" \
                                                                                          "不存在或背景图字段错误！ "

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=9)
    def test_sub_device_asset_picture_new(self, get_global_data, set_global_data):
        """
        (分部设备)设备总览图中，绑定上传得图片与设备
        :param get_global_data:
        :return:
        """
        try:
            pic_info = CommonApis().upload_pictures()
            assert pic_info, "上传图片出错！"

            originalUrl = pic_info['originalUrl']
            picture_name = pic_info['picture_name']
            picture_size = pic_info['picture_size']

            sub_device_id = get_global_data('sub_device_id')

            data = [
                {
                    "group": 5,  # group含义？
                    "dimession": 0,  # 1： 3D ？ 0： 2D ？
                    "attachmentCreateDto": {
                        "address": originalUrl,
                        "name": picture_name,
                        "extension": "png",
                        "size": picture_size,
                        "url": f"/api/Oss/File?fileName={originalUrl}",
                        "response": {
                            "url": f"/api/Oss/File?fileName={originalUrl}",
                            "originalUrl": originalUrl
                        },
                        "status": "done",
                        "thumbAddress": ""
                    },
                    "uid": f"__AUTO__{int(time.time())}_0__"
                }
            ]
            params = {
                "assetId": sub_device_id,
                "_t": datetime.now()
            }

            headers = {
                "Content-Type": "application/json"
            }

            res = Apis().api_device_asset_picture_new(data=data, params=params, headers=headers)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)[0]['id'], "业务接口返回错误，未返回到对应上传绑定后的guid"
            sub_guid = json.loads(res.text)[0]['id']
            set_global_data("sub_guid", sub_guid)

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=10)
    def test_sub_device_set_picture_background(self, get_global_data, set_global_data):
        """
        (分部设备)设置已上传且绑定得图片为设备背景图
        :param get_global_data:
        :return:
        """
        try:
            sub_guid = get_global_data("sub_guid")
            sub_device_id = get_global_data('sub_device_id')
            params = {
                'guid': sub_guid,
                'isDefault': True,
                '_t': datetime.now()
            }

            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }
            res = Apis().api_device_set_background_picture(params=params, headers=headers)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert CommonApis().verify_device_picture_exist(device_id=sub_device_id), "业务请求失败，背景图address" \
                                                                                      "不存在或背景图字段错误！ "
        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=11)
    def test_get_device_info(self, get_global_data, set_global_data):
        """
        获取设备详细位置信息
        :param get_global_data:
        :param set_global_data:
        :return:
        """
        try:
            factory_device_id = get_global_data('factory_device_id')
            params = {
                "id": factory_device_id,
                "_t": datetime.now()
            }
            res = Apis().api_device_get(params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回错误"
            set_global_data("device_detail_info_dict", json.loads(res.text)['data'])

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=12)
    def test_edit_device_info(self, get_global_data):
        """
        编辑设备详细位置信息
        :param get_global_data:
        :return:
        """
        try:

            device_detail_info_dict = get_global_data("device_detail_info_dict")
            data_edit = {
                "note": "修改添加备注1",
                "nameplate": {
                    "note": "修改添加备注2"
                }
            }
            data = dict(device_detail_info_dict, **data_edit)
            params = {
                "_t": datetime.now()
            }
            res = Apis().api_device_edit(data=data, params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'], "业务接口返回失败"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=13)
    def test_get_meta_model_by_asset_id(self, get_global_data):
        """
        获取设备模型
        :param get_global_data:
        :return:
        """
        try:
            factory_device_id = get_global_data('factory_device_id')
            params = {
                "assetId": factory_device_id,
                "_t": datetime.now()
            }
            res = Apis().api_device_get_meta_model_by_asset_id(params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'], "业务接口返回失败"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=14)
    def test_get_device_parts_by_device_id(self, get_global_data):
        """
        获取设备部件
        :param get_global_data:
        :return:
        """
        try:
            factory_device_id = get_global_data('factory_device_id')
            params = {
                "deviceId": factory_device_id,
                "sorting": "SortNum",
                "_t": datetime.now()
            }
            res = Apis().api_device_get_device_parts_by_device_id(params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'], "业务接口返回失败"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=15)
    def test_copy_device(self, get_global_data):
        """
        拷贝设备
        :param get_global_data:
        :return:
        """
        try:

            factory_device_id = get_global_data('factory_device_id')

            params = {
                "assetId": factory_device_id,
                "_t": datetime.now()
            }

            res = Apis().api_get_asset_count(params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回False"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=16)
    def test_paste_device(self, set_global_data, get_global_data):
        """
        粘贴所拷贝的设备
        :param set_global_data:
        :param get_global_data:
        :return:
        """
        try:

            factory_device_id = get_global_data('factory_device_id')

            params = {
                "assetId": factory_device_id,
                "targetId": self.pid,
                "copy": True,
                "_t": datetime.now()
            }

            res = Apis().api_paste_assets(params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['assets'][0]['devices'][0]['id'], "业务接口返回值异常，未获取到复制后的asset id"

            copy_device_id = json.loads(res.text)['assets'][0]['devices'][0]['id']
            assert CommonApis().verify_nodes_exist(pid=self.pid, asset_id=copy_device_id), "设备树中未查询到资产"
            set_global_data("copy_device_id", copy_device_id)

            res = CommonApis().verify_nodes_exist(pid=copy_device_id)
            assert len(res) > 0, "拷贝后的设备未查询到对应的子设备信息！"

            assert CommonApis().verify_device_picture_exist(device_id=copy_device_id), " 拷贝后的设备未查询到对应的背景图信息！"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=17)
    def test_unset_picture_background(self, get_global_data, set_global_data):
        """
        取消已设置的设备背景图
        :param get_global_data:
        :return:
        """
        try:
            guid = get_global_data("guid")
            factory_device_id = get_global_data('factory_device_id')
            params = {
                'guid': guid,
                'isDefault': False,
                '_t': datetime.now()
            }

            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }
            res = Apis().api_device_set_background_picture(params=params, headers=headers)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert CommonApis().verify_device_picture_exist(device_id=factory_device_id) is False, "业务请求失败，背景图address" \
                                                                                                   "不存在或背景图字段错误！ "

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=18)
    def test_delete_images(self, get_global_data, set_global_data):
        """
        删除已设置的设备总览图
        :param get_global_data:
        :return:
        """
        try:
            guid = get_global_data("guid")
            factory_device_id = get_global_data('factory_device_id')
            params = {
                'ids': guid,
                '_t': datetime.now()
            }

            res = Apis().api_device_delete_images(params=params, )
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回False"
            assert CommonApis().verify_device_picture_exist(device_id=factory_device_id) is False, "业务接口错误，删除image" \
                                                                                                   "后，依然可查询到对应image！ "
        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=19)
    def test_sub_device_unset_picture_background(self, get_global_data, set_global_data):
        """
        取消已设置的设备背景图
        :param get_global_data:
        :return:
        """
        try:
            sub_guid = get_global_data("sub_guid")
            sub_device_id = get_global_data('sub_device_id')
            params = {
                'guid': sub_guid,
                'isDefault': False,
                '_t': datetime.now()
            }

            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }
            res = Apis().api_device_set_background_picture(params=params, headers=headers)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert CommonApis().verify_device_picture_exist(device_id=sub_device_id) is False, "业务请求失败，背景图address" \
                                                                                               "不存在或背景图字段错误！ "

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=20)
    def test_sub_device_delete_images(self, get_global_data, set_global_data):
        """
        删除已设置的设备总览图
        :param get_global_data:
        :return:
        """
        try:
            sub_guid = get_global_data("sub_guid")
            sub_device_id = get_global_data('sub_device_id')
            params = {
                'ids': sub_guid,
                '_t': datetime.now()
            }

            res = Apis().api_device_delete_images(params=params, )
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回False"
            assert CommonApis().verify_device_picture_exist(device_id=sub_device_id) is False, "业务接口错误，删除image" \
                                                                                               "后，依然可查询到对应image！ "
        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=100)
    def test_delete_copied_device(self, get_global_data):
        """
        删除拷贝粘贴后的设备
        :param get_global_data:
        :return:
        """
        try:

            copy_device_id = get_global_data('copy_device_id')
            params = {
                "id": copy_device_id
            }

            res = Apis().api_del_choice_asset_info(params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回False"
            assert json.loads(res.text)['data'] is True, "业务接口返回False"

        except Exception as e:
            raise e

    @pytest.mark.bvt
    @pytest.mark.device
    @pytest.mark.run(order=100)
    def test_delete_factory_device(self, get_global_data):
        """
        删除企业下新建的设备
        :param get_global_data:
        :return:
        """
        try:

            factory_device_id = get_global_data('factory_device_id')
            params = {
                "id": factory_device_id
            }

            res = Apis().api_del_choice_asset_info(params=params)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回False"
            assert json.loads(res.text)['data'] is True, "业务接口返回False"
            assert CommonApis().verify_nodes_exist(pid=self.pid, asset_id=factory_device_id) is False, "删除设备异常，设备依然可查询"

        except Exception as e:
            raise e
