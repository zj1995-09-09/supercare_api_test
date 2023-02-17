import pytest

from common.init_run import set_init_env
from common.global_var import set_var, get_var


@pytest.fixture(scope="session", autouse=True)
def set_env(request):
    """
    初始化运行所需环境变量
    """
    from_env = request.config.getoption("--env")
    set_init_env.set_os_env(from_env)


@pytest.fixture
def set_global_data():
    """
    设置全局变量，用于关联参数
    :return:
    """

    def _set_global_data(key, value):
        set_var()(key, value)

    return _set_global_data


@pytest.fixture
def get_global_data():
    """
    从全局变量 global_data 中取值
    :return:
    """

    def _get_global_data(key):
        return get_var()(key)

    return _get_global_data


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="s211",
                     help="test environment")
