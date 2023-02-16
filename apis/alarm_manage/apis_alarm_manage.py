# -*- coding: utf-8 -*-
# @Author   : qiuzixuan
# @Time     : 2023/2/15
# @Desc     : 报警管理接口定义
import os
from functools import partial

from apis.base import Base

# 接口信息
# http://192.168.1.61:31000
GetAlarmTypeAndList = ("POST", "/api/AlarmManageRevision/GetAlarmTypeAndList")
GetAlarmManageInfo = ("GET", "/api/AlarmManageRevision/GetAlarmManageInfo")
CloseAlarmEvent = ("POST", "/api/AlarmManageRevision/CloseAlarmEvent")


class Apis(Base):
    """
    单接口
    """

    def __init__(self):
        super(Apis, self).__init__()

        self._headers = dict(
            {"Authorization": os.getenv("cookies")},
            **{'Content-Type': 'application/json; charset=utf-8'}
        )
        self._apis = partial(self.apis, headers=self._headers)

    def get_alarm_list(self, data: dict = None) -> dict:
        """
        获取报警列表
        :return: 返回报警列表
        """
        return self._apis(url=GetAlarmTypeAndList[1], method=GetAlarmTypeAndList[0], data=data).json()

    def get_alarm_manage_info(self, alarm_id: str) -> dict:
        """
        获取报警详情信息
        :param alarm_id: 报警 ID
        :return:
        """
        return self._apis(
            method=GetAlarmManageInfo[0], url=GetAlarmManageInfo[1], params={"id": alarm_id}
        ).json()

    def close_alarm(self, data: dict = None) -> dict:
        """
        关闭报警
        :param data: 报警关闭理由
            alarm_id: 报警 ID
            reason: 关闭理由 [0, 1, 2, 3, 4, 5, 6]：['安装问题导致', '运行维护导到', '安装问题导致', '现场维护处理', '现场维修处理', '无异常', '其他']
            comment: 备注
        :return:
        """
        return self._apis(
            method=CloseAlarmEvent[0], url=CloseAlarmEvent[1], data=data
        ).json()


if __name__ == '__main__':
    api = Apis()
    print(api.get_alarm_manage_info('58f3d3ac-9405-c665-86e0-83551baac344'))
