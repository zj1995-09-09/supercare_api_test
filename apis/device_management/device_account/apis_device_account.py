# coding:utf-8

import json
import os
from datetime import datetime
import urllib.parse
from apis.base import Base
from common.tools import get_time_suffix, random_str
from common.tools import get_content_type
from common.tools import retry
from common.define_exception import DException as Exc
from requests_toolbelt import MultipartEncoder


class Apis(Base):
    """
    单接口
    """

    def __init__(self):

        super(Apis, self).__init__()

    def api_get_children(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:

            self.headers_default = {
                "Authorization": os.getenv("cookies")
            }
            self.data_default = {}
            self.params_default = {
                "type": "asset",
                "_t": datetime.now()
            }
            method = "get"
            url = self.url + "/api/Tree/getChildren"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e

    def api_crud_asset_operator(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
                "Content-Type": "application/json"
            }
            self.data_default = {
                "AssetType": "Organization",
                "sign": "get",
                "data": {
                    "id": None
                }
            }
            self.params_default = {
                "_t": datetime.now(),
            }
            url = self.url + "/api/Asset/CrudAssetOperator"
            method = "post"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e

    def api_get_basic_config(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {
                "key": "ProductVersion",
                "_t": datetime.now(),
            }
            url = self.url + "/api/systemConfig/getBasicConfig"
            method = "get"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e

    def api_get_node_list_by_args(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {
                "type": "asset",
                "parentId": "",
                "checkedIds": [],
                "all": False,
                "openVibrationZone": False,
            }
            self.params_default = {
                "_t": datetime.now(),
            }
            url = self.url + "/api/Tree/getNodeListByArgs"
            method = "post"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e

    def api_get_devices_and_sub_dev(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
                "Content-Type": "application/json"
            }
            self.data_default = {
                "Filter": "{\"Logic\":\"and\",\"Filters\":[]}",
                "deviceTypes": "",
                "maxResultCount": 30,
                "orgId": False,
                "parent": False,
                "skipCount": 0,
                "types": [40]
            }
            self.params_default = {
                "_t": datetime.now(),
            }
            url = self.url + "/api/Device/GetDevicesAndSubDev"
            method = "post"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e

    def api_del_choice_asset_info(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {
                "id": None,
                "_t": datetime.now(),
            }
            url = self.url + "/api/Asset/DelChoiceAssetInfo"
            method = "delete"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e

    def api_by_asset_types(self, data=None, headers=None):
        """
        获取当前系统所有设备模型
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {
                "_t": datetime.now(),
            }
            url = self.url + "/api/basicService/api/app/deviceCategory/byAssetTypes?assetTypes=40&assetTypes=50&"
            params = {
                "_t": datetime.now()
            }
            url = url + "&" + urllib.parse.urlencode(params)
            method = "get"

            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)

            return res

        except Exception as e:
            raise e

    def api_get_asset_count(self, data=None, params=None, headers=None):
        """
        copy
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {
                "_t": datetime.now(),
            }
            url = self.url + "/api/Asset/getAssetCount"
            method = "get"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_paste_assets(self, data=None, params=None, headers=None):
        """
        copy
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {
                "_t": datetime.now(),
            }
            url = self.url + "/api/basicService/api/app/assetCopy/pasteAssets"
            method = "get"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_device_classify(self, data=None, params=None, headers=None):
        """
        device type
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {
                "_t": datetime.now(),
            }
            url = self.url + "/api/basicService/api/app/deviceClassify"
            method = "get"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_device_get_asset_pictures_filter(self, data=None, params=None, headers=None):
        """
        获取设备总貌图（背景图）
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
                "Content-Type": "application/json"
            }
            self.data_default = {}
            self.params_default = {}
            url = self.url + "/api/basicService/api/app/assetPicture/getAssetPicturesFilter"
            method = "post"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_device_oss_upload_mulity_file(self, data=None, params=None, headers=None):
        """
        上传总览图（背景图）
        :return:
        """
        try:

            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {}

            url = self.url + "/api/Oss/UploadMulityFile"
            method = "post"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_device_asset_picture_new(self, data=None, params=None, headers=None):
        """
        获取设备总貌图（背景图）
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {}
            asset_id = params['assetId']

            url = self.url + "/api/basicService/api/app/assetPicture/picturesNew/{}".format(asset_id)
            method = "post"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_device_set_background_picture(self, data=None, params=None, headers=None):
        """
        获取设备总貌图（背景图）
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {}

            url = self.url + "/api/basicService/api/app/assetPicture/setBackgroundPicture"
            method = "post"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_device_delete_images(self, data=None, params=None, headers=None):
        """
        获取设备总貌图（背景图）
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {}

            url = self.url + "/api/AssetImage/DeleteImages"
            method = "delete"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_device_get_dics_by_code(self, data=None, params=None, headers=None):
        """

        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {}

            url = self.url + "/api/DataDic/GetDicsByCode"
            method = "get"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    # def api_device_asset_device_label(self, data=None, params=None, headers=None):
    #     """
    #     设备标签
    #     :return:
    #     """
    #     try:
    #         self.headers_default = {
    #             "Authorization": os.getenv("cookies"),
    #         }
    #         self.data_default = {}
    #         self.params_default = {}
    #
    #         url = self.url + "/api/basicService/api/app/asset/deviceLabel"
    #         method = "get"
    #         res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
    #         return res
    #     except Exception as e:
    #         raise e

    def api_device_get(self, data=None, params=None, headers=None):
        """
        device info 位置信息
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {}

            url = self.url + "/api/Device/Get"
            method = "get"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_device_edit(self, data=None, params=None, headers=None):
        """
        编辑修改设备信息
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
                "Content-Type": "application/json"
            }
            self.data_default = {}
            self.params_default = {}

            url = self.url + "/api/Device/Edit"
            method = "put"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_device_get_meta_model_by_asset_id(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {}

            url = self.url + "/api/DiagnosticModel/getMetaModelByAssetId"
            method = "get"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_device_get_device_parts_by_device_id(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {}

            url = self.url + "/api/DeviceParts/GetDevicePartsByDeviceId"
            method = "get"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_measure_get_measurement_group(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {}

            url = self.url + "/api/MeasurementGroup/GetMeasurementGroup"
            method = "get"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_measure_get_model_templates_by_type(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:
            self.headers_default = {
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {}

            url = self.url + "/api/basicService/api/app/metaModelInstance/modelTemplatesByType"
            method = "get"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e

    def api_measure_add_batch_asset(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:
            self.headers_default = {
                "Content-Type": "application/json",
                "Authorization": os.getenv("cookies"),
            }
            self.data_default = {}
            self.params_default = {}

            url = self.url + "/api/Asset/AddBatchAsset"
            method = "post"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res

        except Exception as e:
            raise e


class CommonApis(Apis):
    """
    常用业务方法
    """

    @retry(5, 3)
    def get_company_id_with_company_name(self, cname):
        """
        根据企业名称，获取企业id
        :param cname:
        :return:
        """
        pid = None
        res = self.api_get_children()
        for i in json.loads(res.text)['data']['items']:
            if i['name'] == cname:
                pid = i['id']

        return pid

    @retry(5, 3)
    def verify_nodes_exist(self, pid, asset_name=None, asset_id=None):
        """
        获取资产树并根据pid验证asset_name或者asset_id是否存在
        :return:
        """
        params = {
            "type": "asset",
            "pid": pid,
            "isBack": False,
            "_t": datetime.now()
        }
        res = Apis().api_get_children(params=params)
        asset_list = json.loads(res.text)['data']['items']
        if asset_name:
            for i in asset_list:
                if i['name'] == asset_name:
                    return True
            raise Exc(f" {asset_name} Cannot Found")

        if asset_id:
            for i in asset_list:
                if i['id'] == asset_id:
                    return True
            raise Exc(f" {asset_id} Cannot Found")

        return asset_list

    @retry(5, 3)
    def verify_device_picture_exist(self, device_id):
        """
        验证对应device_id的设备下是否有过上传总貌图，若有，则根据是否为背景图进行返回，True：背景图，false：非背景图
        :param device_id:
        :return:
        """
        data = {
            "assetIds": [device_id],
            "dimessions": [0],
            "groups": []
        }
        params = {
            "_t": datetime.now()
        }

        res = Apis().api_device_get_asset_pictures_filter(data=data, params=params)

        if len(json.loads(res.text)):
            if json.loads(res.text)[0]['attachment']['address']:
                return json.loads(res.text)[0]['isDefault']
        raise Exc("fun[verify_device_picture_exist] error!!!")

    @retry(5, 3)
    def upload_pictures(self, ) -> dict:
        """
        上传设备总览图,并返回相关图片信息
        :param:
        :return:
        """
        try:
            _random_str = random_str()
            headers = {
                "Content-Type": "multipart/form-data;boundary=----WebKitFormBoundary{rs}".format(rs=_random_str)
            }

            file = r"{}\files\设备图片.png".format(os.getcwd())
            filename = file.split("\\")[-1]
            filesize = os.path.getsize(file)

            r = get_content_type(file)

            fields = MultipartEncoder(
                fields={"formFiles": ("{}".format(filename), open(r"{}".format(file), "rb"), r)},
                # 新接口为formFiles，老接口为：formFile
                boundary="----WebKitFormBoundary{}".format(_random_str)
            )

            params = {
                "_t": datetime.now(),
                "groupName": "file"
            }

            res = Apis().api_device_oss_upload_mulity_file(data=fields, params=params, headers=headers)
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)[0]['data']['originalUrl'], "业务接口返回异常，未获取到上传后的存储地址信息."
            original_url = json.loads(res.text)[0]['data']['originalUrl']

            return {
                "originalUrl": original_url,
                "picture_name": filename,
                "picture_size": filesize
            }
        except Exception:
            raise Exc(f"upload pictures Error!")

    def add_device(self, pid=None, device_name=None):
        """
        添加设备
        return: device_id
        """
        try:
            if not device_name:
                now_data_time = datetime.now()
                suffix = now_data_time.strftime('%H_%M_%S')
                device_name = f"设备xxx-{suffix}"

            if not pid:
                company_name = os.getenv("company_name")
                pid = self.get_company_id_with_company_name(company_name)

            params = {
                "_t": datetime.now()
            }

            data = {
                "data": {
                    "name": device_name,
                    "category": "NUM001",
                    "extraProperties": {},
                    "type": 40,
                    "parent": pid
                },
                "sign": "post",
                "AssetType": "Device"
            }
            res = Apis().api_crud_asset_operator(data=data, params=params)
            device_id = json.loads(res.text)['data']['id']
            return device_id
        except Exception:
            raise Exc(f"create new device Error!")

    def add_measurements(self) -> tuple:
        """
        添加动态量测点 - 测量定义
        """
        # 添加设备
        _device_id = self.add_device()

        # 添加动态量测点
        point_name = f"动态量-{get_time_suffix()}"

        point_data = {
            "data": {
                "monitorMode": 2,  # 离线，在线，第三方在线，第三方离线
                "name": point_name,
                "parent": _device_id,
                "pointType": "0000",
                "type": 80,
            },
            "sign": "post",
            "AssetType": "Point"
        }

        point_res = self.api_crud_asset_operator(data=point_data, params={"_t": datetime.now()})

        _point_id = json.loads(point_res.text)['data']['id']

        # 添加测量定义
        lower_freq = 2
        upper_freq = 10
        data_length = 1024

        name = f"{data_length / 1024}k 加速度波形({lower_freq}-{upper_freq})"

        measure_data = {
            "measurements": [
                {
                    "type": 90,
                    "isDisplayable": True,
                    "engineerUnitFamily": "Accelerated speed",
                    "name": name,
                    "parent": _point_id,
                    "extraProperties": {
                        "SignalType": 0,
                        "LowerFreq": lower_freq,
                        "UpperFreq": upper_freq,
                        "DataLength": data_length,
                        "SamplingMode": 0
                    }
                }
            ]
        }

        measure_res = self.api_measure_add_batch_asset(data=measure_data, params={"_t": datetime.now()}).json()
        _measure_id = measure_res["data"]["measurements"][0]["id"]

        return _device_id, _point_id, _measure_id

    @staticmethod
    def delete_device(device_id):
        """
        删除设备
        """
        try:
            res = Apis().api_del_choice_asset_info(params={"id": device_id})
            assert res.status_code <= 200, "Http请求状态码错误"
            assert json.loads(res.text)['success'] is True, "业务接口返回False"
            assert json.loads(res.text)['data'] is True, "业务接口返回False"

        except Exception as e:
            raise e


if __name__ == '__main__':
    # from common.init_run import set_init
    # set_init('s211').set_os_env()
    # print(CommonApis().add_measurements())
    print()
