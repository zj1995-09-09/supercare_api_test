# coding:utf-8
import json
import pytest
import os
from datetime import datetime
from apis.apis_device_account import Apis
from common import api_tools
from requests_toolbelt import MultipartEncoder


@pytest.mark.bvt
@pytest.mark.single
def test_upload_pictures():

    _random_str = api_tools.random_str(16)
    headers = {
        "Content-Type": "multipart/form-data;boundary=----WebKitFormBoundary{rs}".format(rs=_random_str)
    }

    file = r"{}\files\设备图片.png".format(os.getcwd())
    file.replace("\\", "/")  # 兼容linux+win
    filename = file.split("/")[-1]

    r = api_tools.get_content_type(file)

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
