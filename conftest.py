# coding: utf-8

import time
import pytest
from common.init_auth import set_init
import os


@pytest.fixture
def set_global_data():
    """
    此处使用os环境变量，用于关联参数
    :return:
    """
    def _set_global_data(key, value):
        os.environ[key] = value

    return _set_global_data


@pytest.fixture
def get_global_data():
    """
    从os环境变量中取值
    :return:
    """
    def _get_global_data(key):
        return os.environ[key]

    return _get_global_data


@pytest.fixture(scope="session", autouse=True)
def set_env(request):
    """
    初始化运行所需环境变量
    """
    from_env = request.config.getoption("--env")
    set_init(from_env).set_os_env()


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
        收集终端运行的结果
        :param terminalreporter:
        :param exitstatus:
        :param config:
        :return:
        """
    total_case = terminalreporter._numcollected
    passed_case = len(terminalreporter.stats.get('passed', []))
    failed_case = len(terminalreporter.stats.get('failed', []))
    error_case = len(terminalreporter.stats.get('error', []))
    skipped_case = len(terminalreporter.stats.get('skipped', []))
    deselected_case = len(terminalreporter.stats.get('deselected', []))
    duration = time.time() - terminalreporter._sessionstarttime

    terminal_tag = terminalreporter.config.getoption('-m')

    print(f"RESULT>>>{total_case},{passed_case},{failed_case}<<<")


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="s211",
                     help="test environment")
