# -*- coding: utf-8 -*-
# @Author   : qiuzixuan
# @Time     : 2023/2/16
# @Desc     : 报警管理测试用例
import pytest

from testcase.alarm_manage.case_data import alarm_list_data
from apis.alarm_manage.apis_alarm_manage import alarm_manage_apis


@pytest.mark.parametrize(["count", "status", "alarm_type"], alarm_list_data)
def test_get_alarm_list(count, status, alarm_type):
    """
    获取报警列表
    :param count: 每页数量
    :param status: 报警状态
    :param alarm_type: 报警类型：智能-0，门限-1
    :return:
    """
    _data = {
        "count": count,
        "status": status,
        "alarm_type": alarm_type
    }

    response = alarm_manage_apis().get_alarm_list(data=_data)
    print(
        f"获取报警列表，请求参数：{_data}，响应结果：{response}"
    )

