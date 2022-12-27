import os
import pytest
from common.request_module import http_request
from conf.supercare_conf import Environment as ev


@pytest.fixture(scope="session", autouse=True)
def set_env(request):
    env = request.config.getoption("--env")

    data = {
        "grant_type": "password",
        "client_id": "epm",
        "client_secret": "secret",
        "username": ev(env).env_user,
        "password": ev(env).env_password
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = http_request(ev(env).env_login_url, method="post", data=data, headers=headers)
    os.environ["cookies"] = "{} {}".format(res.json()["token_type"], res.json()["access_token"])
    os.environ["kafka"] = ev(env).env_kafka
    os.environ["company_name"] = ev(env).env_company_name
    os.environ["ent_code"] = ev(env).env_ent_code
    os.environ["api_url"] = ev(env).env_api_url
    os.environ["company_type"] = ev(env).env_company_type
    os.environ["supercare_type"] = ev(env).env_supercare_type


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
    parser.addoption("--env", action="store", default="single211",
                     help="test environment")
