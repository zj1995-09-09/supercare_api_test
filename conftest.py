import os
import pytest
from common.request_module import http_request
from conf.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_env(request):
    env = getattr(settings, request.config.getoption("--env"))

    data = {
        "grant_type": "password",
        "client_id": "epm",
        "client_secret": "secret",
        "username": env.user,
        "password": env.password
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = http_request(env.login_url, method="post", data=data, headers=headers)
    os.environ["cookies"] = "{} {}".format(res.json()["token_type"], res.json()["access_token"])
    os.environ["kafka"] = env.kafka
    os.environ["company_name"] = env.company_name
    os.environ["ent_code"] = env.EntCode
    os.environ["api_url"] = env.api_url
    os.environ["company_type"] = env.company_type
    os.environ["supercare_type"] = env.supercare_type


global_data = {}


@pytest.fixture
def set_global_data():
    """
    设置全局变量，用于关联参数
    :return:
    """

    def _set_global_data(key, value):
        global_data[key] = value

    return _set_global_data


@pytest.fixture
def get_global_data():
    """
    从全局变量global_data中取值
    :return:
    """

    def _get_global_data(key):
        return global_data.get(key)

    return _get_global_data


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="s211",
                     help="test environment")
