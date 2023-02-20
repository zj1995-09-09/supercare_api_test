# -*- coding: utf-8 -*-
# @Author   : qiuzixuan
# @Time     : 2022/9/1
# @Desc     : 报警管理模块测试用例数据
import pytest

alarm_list_data = (
    # pytest.param(30, [0], [1], id='获取 30 个报警处理状态为全部的门限报警列表'),
    # pytest.param(50, [0], [1], id='获取 50 个报警处理状态为全部的门限报警列表'),
    # pytest.param(100, [0], [1], id='获取 100 个报警处理状态为全部的门限报警列表'),
    # pytest.param(30, [1], [1], id='获取 30 个报警处理状态为已关闭的门限报警列表'),
    # pytest.param(50, [1], [1], id='获取 50 个报警处理状态为已关闭的门限报警列表'),
    # pytest.param(100, [1], [1], id='获取 100 个报警处理状态为已关闭的门限报警列表'),
    pytest.param(30, [0], [0], id='获取 30 个报警处理状态为全部的智能报警列表', marks=pytest.mark.bvt),
    pytest.param(50, [0], [0], id='获取 50 个报警处理状态为全部的智能报警列表'),
    pytest.param(100, [0], [0], id='获取 100 个报警处理状态为全部的智能报警列表'),
    pytest.param(30, [1], [0], id='获取 30 个报警处理状态为已关闭的智能报警列表'),
    pytest.param(50, [1], [0], id='获取 50 个报警处理状态为已关闭的智能报警列表'),
    pytest.param(100, [1], [0], id='获取 100 个报警处理状态为已关闭的智能报警列表'),
)

alarm_info_data = (
    pytest.param(0, id='获取未处理的报警详情'),
    pytest.param(1, id='获取已处理的报警详情'),
    pytest.param(2, id='获取已关闭的报警详情'),
)

close_alarm_data = (
    pytest.param(0, id='关闭报警-原因：安装问题导致'),
    pytest.param(1, id='关闭报警-原因：运行维护导致'),
    pytest.param(2, id='关闭报警-原因：安装问题导致'),
    pytest.param(3, id='关闭报警-原因：现场维护处理'),
    pytest.param(4, id='关闭报警-原因：现场维修处理'),
    pytest.param(5, id='关闭报警-原因：无异常'),
    pytest.param(6, id='关闭报警-原因：其他'),
)

get_threshold_data = (
    pytest.param(0, id='获取通用指标门限'),
    pytest.param(1, id='获取采样值指标门限'),
)


if __name__ == '__main__':
    ...
