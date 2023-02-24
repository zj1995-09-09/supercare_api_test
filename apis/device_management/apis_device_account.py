# coding:utf-8

import os
from datetime import datetime
import urllib.parse
from apis.base import Base


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

    def api_crud_asset_operator(self, data=None, params=None, headers=None):
        """
        :return:
        """
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

    def api_get_basic_config(self, data=None, params=None, headers=None):
        """
        :return:
        """
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

    def api_get_node_list_by_args(self, data=None, params=None, headers=None):
        """
        :return:
        """
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

    def api_get_devices_and_sub_dev(self, data=None, params=None, headers=None):
        """
        :return:
        """
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

    def api_del_choice_asset_info(self, data=None, params=None, headers=None):
        """
        :return:
        """
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

    def api_by_asset_types(self, data=None, params=None, headers=None, url_params=None):
        """
        这个url_params防止相同key的入参
        获取当前系统所有设备模型
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {
            "_t": datetime.now(),
        }

        if url_params:
            url = self.url + "/api/basicService/api/app/deviceCategory/byAssetTypes?" + url_params
        else:
            url = self.url + "/api/basicService/api/app/deviceCategory/byAssetTypes"
        params = {
            "_t": datetime.now()
        }
        url = url + "&" + urllib.parse.urlencode(params)
        method = "get"

        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)

        return res

    def api_get_asset_count(self, data=None, params=None, headers=None):
        """
        copy
        :return:
        """
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

    def api_paste_assets(self, data=None, params=None, headers=None):
        """
        copy
        :return:
        """
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

    def api_device_classify(self, data=None, params=None, headers=None):
        """
        device type
        :return:
        """
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

    def api_get_asset_pictures_filter(self, data=None, params=None, headers=None):
        """
        获取设备总貌图（背景图）
        :return:
        """
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

    def api_upload_mulity_file(self, data=None, params=None, headers=None):
        """
        上传总览图（背景图）
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/Oss/UploadMulityFile"
        method = "post"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_pictures_new(self, data=None, params=None, headers=None):
        """
        获取设备总貌图（背景图）
        :return:
        """
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

    def api_set_background_picture(self, data=None, params=None, headers=None):
        """
        获取设备总貌图（背景图）
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/basicService/api/app/assetPicture/setBackgroundPicture"
        method = "post"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_device_delete_images(self, data=None, params=None, headers=None):
        """
        获取设备总貌图（背景图）
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/AssetImage/DeleteImages"
        method = "delete"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_get_dics_by_code(self, data=None, params=None, headers=None):
        """

        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/DataDic/GetDicsByCode"
        method = "get"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_device_get(self, data=None, params=None, headers=None):
        """
        device info 位置信息
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/Device/Get"
        method = "get"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_device_edit(self, data=None, params=None, headers=None):
        """
        编辑修改设备信息
        :return:
        """
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

    def api_device_get_meta_model_by_asset_id(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/DiagnosticModel/getMetaModelByAssetId"
        method = "get"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_get_device_parts_by_device_id(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/DeviceParts/GetDevicePartsByDeviceId"
        method = "get"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_get_measurement_group(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/MeasurementGroup/GetMeasurementGroup"
        method = "get"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_model_templates_by_type(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/basicService/api/app/metaModelInstance/modelTemplatesByType"
        method = "get"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_add_batch_asset(self, data=None, params=None, headers=None):
        """
        :return:
        """
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

    def api_add_device_parts(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Content-Type": "application/json",
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/DeviceParts/AddDeviceParts"
        method = "post"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_delete_range_device_parts(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Content-Type": "application/json",
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/DeviceParts/DeleteRangeDeviceParts"
        method = "post"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_diagnosis(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/alarmService/api/app/alarmStatistics/diagnosis"
        method = "get"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_fault_type_datas_by_device_type(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/basicService/api/app/newFaultComponentType/faultTypeDatasByDeviceType"
        method = "get"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_fault_types(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/basicService/api/app/faultTypes"
        method = "get"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_device_categories(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/basicService/api/app/deviceCategories"
        method = "get"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_device_resume_actions(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/basicService/api/app/deviceResume/actions"
        method = "get"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_get_spot_check_reason_type(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/AlarmManage/GetSpotCheckReasonType"
        method = "get"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_device_resume(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {}

        url = self.url + "/api/basicService/api/app/deviceResume"
        method = "get"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res
