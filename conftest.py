import os
import pytest
from common.request_module import http_request



@pytest.fixture(scope="session", autouse=True)
def set_cookies(username="admin", password="1q2w3E*"):
    data = {
        "grant_type": "password",
        "client_id": "epm",
        "client_secret": "secret",
        "username": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = http_request("http://192.168.1.211:5000/connect/token", method="post", data=data, headers=headers)
    os.environ["cookies"] = "{} {}".format(res.json()["token_type"], res.json()["access_token"])


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