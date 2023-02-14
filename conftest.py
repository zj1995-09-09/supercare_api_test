import os
import pytest

from common.auth import auth
from common.global_var import set_var, get_var
from libs.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_env(request):
    from_env = request.config.getoption("--env")
    env = getattr(settings, from_env)
    auth(from_env)  # 设置 cookies

    os.environ["kafka"] = env.kafka
    os.environ["company_name"] = env.company_name
    os.environ["ent_code"] = env.EntCode
    os.environ["api_url"] = env.api_url
    os.environ["company_type"] = env.company_type
    os.environ["supercare_type"] = env.supercare_type


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


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="s211",
                     help="test environment")
