# coding: utf-8
import os
from apis.device_management.apis_device_account import Apis
from common.api_tools import retry, random_str, get_content_type
import json
from datetime import datetime
from requests_toolbelt import MultipartEncoder
import time


class ApisUtils(Apis):
    """
    由apis构成steps
    """

    @retry(5, 3)
    def get_company_id_with_company_name(self, cname=None):
        """
        根据企业名称，获取企业id
        :param cname:
        :return:
        """
        pid = None

        if not cname:
            cname = os.getenv("company_name")

        res = self.api_get_children()
        assert res.status_code <= 400, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"

        for i in json.loads(res.text)['data']['items']:
            if i['name'] == cname:
                pid = i['id']

        assert pid, f"未查取到cname={cname}的企业id"
        return pid

    @retry(5, 3)
    def get_devices_classify(self, type_name=None):
        """
        根据设备分类名称，获取设备分类id，默认为获取‘默认分类’
        """

        params = {
            "SkipCount": 0,
            "MaxResultCount": 99999,
            "_t": datetime.now()
        }
        res = self.api_device_classify(params=params)

        if not type_name:
            return res.json()['items'][0]['code']

        for i in res.json()['items']:
            if i['name'] == type_name:
                return i['code']

        assert False, f"未查取到type_name={type_name}的设备分类id"

    @retry(5, 3)
    def delete_asset(self, asset_id):
        """
        删除资产
        """
        params = {
            "id": asset_id
        }

        res = self.api_del_choice_asset_info(params=params)
        assert res.status_code <= 400, "删除资源Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "删除资源业务接口返回False"
        assert json.loads(res.text)['data'] is True, "删除资源业务接口返回False"

    @retry(5, 3)
    def add_asset(self, **kwargs):
        """
        api_crud_asset_operator对应创建的资产类型包含有：
        1.产线
        2.区域
        3.设备
        4.分部设备
        5.部件
        6.部件细分
        7.单个动态量
        8.倾角测点
        9.工艺测点
        10.观察量测点
        11.工况测点
        12.超声测点
        13.螺栓测点（参数离谱的多，不做测试）
        """

        params = {
            "_t": datetime.now()
        }

        res = Apis().api_crud_asset_operator(data=kwargs['data'], params=params)
        assert res.status_code <= 400, "新建资产业务Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "新建资产业务接口返回False"
        assert json.loads(res.text)['data']['id'], "新建资产业务接口返回未获取到资产id"

        return json.loads(res.text)['data']['id']

    @retry(3, 5)
    def upload_device_pictures(self, file, device_id):
        """
        设备上传背景图（包含2个接口）， 返回GUID
        """

        _random_str = random_str(16)
        headers = {
            "Content-Type": "multipart/form-data;boundary=----WebKitFormBoundary{rs}".format(rs=_random_str)
        }

        file.replace("\\", "/")  # 兼容linux+win
        filename = file.split("/")[-1]
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

        res = Apis().api_upload_mulity_file(data=fields, params=params, headers=headers)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)[0]['data']['originalUrl'], "业务接口返回异常，未获取到上传后的存储地址信息."
        original_url = json.loads(res.text)[0]['data']['originalUrl']

        data = [
            {
                "group": 5,  # group含义？
                "dimession": 0,  # 1： 3D ？ 0： 2D ？
                "attachmentCreateDto": {
                    "address": original_url,
                    "name": filename,
                    "extension": "png",
                    "size": filesize,
                    "url": f"/api/Oss/File?fileName={original_url}",
                    "response": {
                        "url": f"/api/Oss/File?fileName={original_url}",
                        "originalUrl": original_url
                    },
                    "status": "done",
                    "thumbAddress": ""
                },
                "uid": f"__AUTO__{int(time.time())}_0__"
            }
        ]
        params = {
            "assetId": device_id,
            "_t": datetime.now()
        }

        headers = {
            "Content-Type": "application/json"
        }

        res = Apis().api_pictures_new(data=data, params=params, headers=headers)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)[0]['id'], "业务接口返回错误，未返回到对应上传绑定后的guid"
        sub_guid = json.loads(res.text)[0]['id']
        return sub_guid

    @retry(3, 5)
    def set_picture_background(self, guid):
        """
        设置已上传且绑定得图片为设备背景图,（guid已关联了设备与图片）
        """
        params = {
            'guid': guid,
            'isDefault': True,
            '_t': datetime.now()
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        res = Apis().api_set_background_picture(params=params, headers=headers)
        assert res.status_code <= 400, "Http请求状态码错误"

    @retry(3, 5)
    def get_device_general_view(self, device_id):
        """
        获取设备总览图信息，返回res
        """

        data = {
            "assetIds": [device_id],
            "dimessions": [0],
            "groups": []
        }
        params = {
            "_t": datetime.now()
        }

        res = Apis().api_get_asset_pictures_filter(data=data, params=params)
        assert res.status_code <= 400, "Http请求状态码错误"
        return res

    @retry(3, 5)
    def get_device_detail_info(self, device_id):
        """
        获取设备详细信息
        """
        params = {
            "id": device_id,
            "_t": datetime.now()
        }
        res = Apis().api_device_get(params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回错误"
        return res

    @retry(3, 5)
    def edit_device_info(self, data_edit):
        """
        编辑设备详细位置信息
        """

        params = {
            "_t": datetime.now()
        }
        res = Apis().api_device_edit(data=data_edit, params=params)
        assert res.status_code <= 400, "编辑设备详细位置信息Http请求状态码错误"
        assert json.loads(res.text)['success'], "编辑设备详细位置信息业务接口返回失败"
        return res

    @retry(3, 5)
    def copy_paste_asset(self, source_id, target_id):
        """
        拷贝粘贴资产，返回粘贴后的设备id
        """
        params = {
            "assetId": source_id,
            "_t": datetime.now()
        }

        res = Apis().api_get_asset_count(params=params)
        assert res.status_code <= 200, "获取拷贝资产信息Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "获取拷贝资产信息业务接口返回False"

        params = {
            "assetId": source_id,
            "targetId": target_id,
            "copy": True,
            "_t": datetime.now()
        }

        res = Apis().api_paste_assets(params=params)
        assert res.status_code <= 200, "粘贴资产Http请求状态码错误"
        assert json.loads(res.text)['assets'][0]['devices'][0]['id'], "粘贴资产业务接口返回值异常，未获取到复制粘贴后的asset id"

        return json.loads(res.text)['assets'][0]['devices'][0]['id']

    @retry(3, 5)
    def get_devices_and_sub_dev(self, pid, page=0, nums=30):
        """
        获取pid下的设备列表
        返回pid下所查询到的设备列表
        """

        params = {
            "_t": datetime.now()
        }
        data = {
            "types": [
                40
            ],
            "orgId": pid,
            "skipCount": page*nums,
            "maxResultCount": nums,
            "Filter": "{\"Logic\":\"and\",\"Filters\":[]}",
            "parent": pid
        }
        res = self.api_get_devices_and_sub_dev(data=data, params=params)
        assert res.status_code <= 400, "查询资产子设备列表业务接口HTTP请求状态码错误"
        assert json.loads(res.text)['success'] is True, "查询资产子设备列表业务接口返回False"

        return json.loads(res.text)['data']['items']

    @retry(3, 5)
    def get_device_parts_by_device_id(self, device_id):
        """
        获取设备部件
        """

        params = {
            "deviceId": device_id,
            "sorting": "SortNum",
            "_t": datetime.now()
        }

        res = self.api_get_device_parts_by_device_id(params=params)
        assert res.status_code <= 400, "获取设备部件列表业务接口HTTP请求状态码错误"
        assert json.loads(res.text)['success'] is True, "获取设备部件列表业务接口返回False"

        return json.loads(res.text)['data']['Items']

    @retry(3, 5)
    def add_device_parts(self, device_id, part_type_name, describe_name):
        """
        添加设备部件,返回对应设备部件ID
        """

        params = {
            "_t": datetime.now(),
        }

        res = self.api_by_asset_types(params=params, url_params="assetTypes=50&assetTypes=60")
        assert res.status_code <= 400, "Http请求状态码错误"
        assert len(json.loads(res.text)) > 0, "业务接口返回类型数量为零"

        part_type_code = None
        for i in json.loads(res.text):
            if i['name'] == part_type_name:
                part_type_code = i['code']
                break

        assert part_type_code, f"未查询到名称为{part_type_name}的模型编码"

        params = {
            "_t": datetime.now()
        }
        data = {
            "DeviceId": device_id,
            "PartType": part_type_code,
            "PartDescribe": describe_name,
            "PointIds": []
        }

        res = self.api_add_device_parts(data=data, params=params)
        assert res.status_code <= 400, "添加设备部件接口HTTP请求状态码错误"
        assert json.loads(res.text)['success'] is True, "添加设备部件业务接口返回False"

        return json.loads(res.text)['data'][0]['Id']

    @retry(3, 5)
    def delete_device_parts(self, parts_id):
        """
        删除设备部件,
        """

        params = {
            "_t": datetime.now(),
        }
        data = {
            "ids": [parts_id]
        }

        res = self.api_delete_range_device_parts(params=params, data=data)
        assert res.status_code <= 400, "删除设备部件Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "删除设备部件业务接口返回False"

    @retry(3, 5)
    def device_categories(self, device_id):
        """
        查看设备的诊断记录
        """

        params = {
            "assetTypes": 70,
            "_t": datetime.now(),
        }

        res = self.api_device_categories(params=params)
        assert res.status_code <= 400, "获取设备类别Http请求状态码错误"
        assert len(json.loads(res.text)['items']) > 0, "获取的设备类别数量为空"

        params = {
            "_t": datetime.now(),
        }

        res = self.api_fault_type_datas_by_device_type(params=params)
        assert res.status_code <= 400, "[api_fault_type_datas_by_device_type]获取设备异常类型Http请求状态码错误"
        assert len(json.loads(res.text)) > 0, "[api_fault_type_datas_by_device_type]获取设备异常类型数量为空"

        params = {
            "_t": datetime.now(),
        }
        res = self.api_fault_types(params=params)
        assert res.status_code <= 400, "[api_fault_types]获取设备异常类型Http请求状态码错误"
        assert len(json.loads(res.text)) > 0, "[api_fault_types]获取设备异常类型数量为空"

        params = {
            "maxResultCount": 5000,
            "skipCount": 0,
            "AssetId": device_id,
            "StartTime": "2023/01/01 00:00:00",
            "EndTime": "2023/02/24 23:59:59",
            "_t": datetime.now(),
        }

        res = self.api_diagnosis(params=params,)
        assert res.status_code <= 400, "获取诊断记录Http请求状态码错误"

        return res


if __name__ == "__main__":
    from common.init_auth import set_init
    set_init("s211").set_os_env()
