# -*- coding: utf-8 -*-
# @Author   : qiuzixuan
# @Time     : 2023/1/13
# @Desc     : 登录鉴权
import os

from common.request_module import http_request
from libs.config import settings


class InitRun:
    """
    初始化运行环境
    """

    def __init__(self, from_env: str):
        self.from_env = from_env
        self._env = getattr(settings, self.from_env)

    def auth(self):
        """
        登录鉴权
        """
        data = {
            "grant_type": "password",
            "client_id": "epm",
            "client_secret": "secret",
            "username": self._env.user,
            "password": self._env.password
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        res = http_request(self._env.login_url, method="post", data=data, headers=headers).json()
        env_cookies = f'Bearer {res["access_token"]}'

        return env_cookies

    def set_os_env(self):
        """
        设置环境变量
        """
        self._env.cookies = self.auth()

        os.environ["cookies"] = self._env.cookies
        os.environ["kafka"] = self._env.kafka
        os.environ["company_name"] = self._env.company_name
        os.environ["ent_code"] = self._env.EntCode
        os.environ["api_url"] = self._env.api_url
        os.environ["company_type"] = self._env.company_type
        os.environ["supercare_type"] = self._env.supercare_type


set_init = InitRun

if __name__ == '__main__':
    set_init("s211").set_os_env()
    print(settings.s211.cookies)
