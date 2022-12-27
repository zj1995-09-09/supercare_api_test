# coding:utf-8
import json, pytest
from apis.device_management.device_account.apis_device_account import Apis, CommonApis
from datetime import datetime
import os

device_id = ""


def setup():
    """
    根据企业名称获取pid
    :return:
    """
    try:
        global device_id
        device_id = CommonApis().add_device()

    except Exception as e:
        raise e


@pytest.mark.device
@pytest.mark.temp
@pytest.mark.run(order=1)
def test_add_measurement(set_global_data):
    """
    添加动态量
    """
    try:

        global device_id

        now_data_time = datetime.now()
        suffix = now_data_time.strftime('%H_%M_%S')

        point_name = f"动态量-{suffix}"

        data = {
            "data": {
                "monitorMode": 2,   # 离线，在线，第三方在线，第三方离线
                "name": point_name,
                "parent": device_id,
                "pointType": "0000",
                "type": 80,
            },
            "sign": "post",
            "AssetType": "Point"
        }
        params = {
            "_t": datetime.now()
        }

        res = Apis().api_crud_asset_operator(data=data, params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        assert json.loads(res.text)['data']['id'], "业务接口返回未获取到测点id"
        set_global_data('point_id', json.loads(res.text)['data']['id'])

        CommonApis().verify_nodes_exist(pid=device_id,asset_name=point_name)

    except Exception as e:
        raise e


@pytest.mark.device
@pytest.mark.temp
@pytest.mark.run(order=2)
def test_add_batch_asset(set_global_data, get_global_data):
    """
    动态量下添加测量定义
    """
    try:
        point_id = get_global_data('point_id')

        lower_freq = 2
        upper_freq = 10
        data_length = 1024
        wave_type_dict = {
            "Accelerated speed": "加速度",
            "Speed": "速度"
        }
        wave_type = "Accelerated speed"
        name = f"{data_length/1024}k {wave_type_dict[wave_type]}波形({lower_freq}-{upper_freq})"

        params = {
            "_t": datetime.now()
        }
        data = {
            "measurements": [
                {
                    "type": 90,
                    "isDisplayable": True,
                    "engineerUnitFamily": "Accelerated speed",
                    "name": "1k 加速度波形(2-10)",
                    "parent": point_id,
                    "extraProperties": {
                        "SignalType": 0,
                        "LowerFreq": 2,
                        "UpperFreq": 10,
                        "DataLength": 1024,
                        "SamplingMode": 0
                    }
                }
            ]
        }

        res = Apis().api_measure_add_batch_asset(data=data, params=params)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        # assert json.loads(res.text)['data']['id'], "业务接口返回未获取到测点id"
        # set_global_data('point_id', json.loads(res.text)['data']['id'])

    except Exception as e:
        raise e

