# coding: utf-8
import os
from apis.apis_device_account import Apis
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
            return res.json()['items'][0]['id']

        for i in res.json()['items']:
            if i['name'] == type_name:
                return i['id']

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


if __name__ == "__main__":
    from common.init_auth import set_init
    set_init("s211").set_os_env()
