# coding : utf-8


def data_line(name, total_equipment_num, pid):
    """
    产线
    """
    _data_line = {
            "data": {
                "name": name,
                "extraProperties": {
                    "TotalEuipmentNum": total_equipment_num
                },
                "type": 20,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Organization"
        }
    return _data_line


def data_area(name, pid):
    """
    区域
    """
    _data_area = {
            "data": {
                "name": name,
                "type": 30,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Organization"
        }
    return _data_area


def data_device(name, category, pid):
    """
    设备
    """
    _data_device = {
            "data": {
                "monitorMode": 2,
                "name": name,
                "category": category,
                # "nameplate": null,
                "partNameplates": [
                    {
                        "name": "Gearbox"
                    },
                    {
                        "name": "Alternator"
                    },
                    {
                        "name": "MainBearing"
                    }
                ],
                "extraProperties": {},
                "responsibleUserIds": [],
                "deviceType": "",
                "type": 40,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Device"
        }
    return _data_device


def data_part_device(name, category, pid):
    """
    分部设备
    """
    _data_part_device = {
            "data": {
                "monitorMode": 2,
                "name": name,
                "category": category,
                # "nameplate": null,
                "partNameplates": [
                    {
                        "name": "Gearbox"
                    },
                    {
                        "name": "Alternator"
                    },
                    {
                        "name": "MainBearing"
                    }
                ],
                "extraProperties": {},
                "responsibleUserIds": [],
                "deviceType": "",
                "type": 50,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Device"
        }
    return _data_part_device


def data_parts(name, pid):
    """
    部件
    """
    _data_parts = {
            "data": {
                "name": name,
                "type": 60,
                # "isBath": false,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Component"
        }
    return _data_parts


def data_parts_detail(name, pid):
    """
    部件细分
    """
    _data_parts_detail = {
            "data": {
                "name": name,
                "type": 70,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Component"
        }
    return _data_parts_detail


def data_points_0000(name, pid):
    """
    单个动态量
    """
    _data_points_0000 = {
            "data": {
                "type": 80,
                "pointType": "0000",
                "monitorMode": 2,
                "name": name,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Point"
        }
    return _data_points_0000


def data_points_0004(name, pid):
    """
    倾角测点（倾角测点新建时会自动带出倾角测量定义）
    """
    _data_points_0004 = {
            "data": {
                "extraProperties": {
                    "InitialAngle": 0,
                    "InitialPositionAngle": 0,
                    "SernorType": 0,
                    "Direct": ""
                },
                "monitorMode": 2,
                "name": name,
                "type": 80,
                "pointType": "0004",
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Point"
        }
    return _data_points_0004


def data_measurement_00(wave_length, l_freq, u_freq, pid):
    """
    倾角的测量定义
    """
    name = f"{wave_length} K倾角波形({l_freq}-{u_freq})"    # 16 K倾角波形(0.1-20)
    _data_measurement_00 = {
            "data": {
                "type": 90,
                "measurementType": "00",
                "isDisplayable": True,
                "dataList": [],
                "isOffLine": True,
                "hasChildren": False,
                "name": name,
                "parent": pid,
                "extraProperties": {
                    "SignalType": 5,
                    "LowerFreq": l_freq,
                    "UpperFreq": u_freq,
                    "DataLength": wave_length*1024,
                    "SamplingMode": 0
                }
            },
            "sign": "post",
            "AssetType": "Measurement"
        }
    return _data_measurement_00


def data_points_0100(name, pid):
    """
    工艺测点
    """
    _data_points_0100 = {
            "data": {
                "monitorMode": 2,
                "name": name,
                "type": 80,
                "pointType": "0100",
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Point"
        }
    return _data_points_0100


def data_points_0200(name, pid):
    """
    观察量测点
    """
    _data_points_0200 = {
            "data": {
                "type": 80,
                "pointType": "0200",
                "monitorMode": 2,
                "name": name,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Point"
        }
    return _data_points_0200


def data_points_0010(name, pid):
    """
    工况测点
    """
    _data_points_0010 = {
            "data": {
                "type": 80,
                "pointType": "0010",
                "monitorMode": 2,
                "name": name,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Point"
        }
    return _data_points_0010


def data_points_0008(name, pid):
    """
    超声测点
    """
    _data_points_0008 = {
            "data": {
                "name": name,
                "type": 80,
                "pointType": "0008",
                "monitorMode": 2,
                "extraProperties": {
                    "Azimuth": 0,
                    "UnitType": "1"
                },
                "isBath": False,
                "parent": pid
            },
            "sign": "post",
            "AssetType": "Point"
        }