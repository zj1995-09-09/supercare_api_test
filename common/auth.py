# -*- coding: utf-8 -*-
# @Author   : qiuzixuan
# @Time     : 2023/1/13
# @Desc     : 登录鉴权
import os

from common.request_module import http_request
from conf.config import settings


def auth(from_env: str):
    env = getattr(settings, from_env)
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

    res = http_request(env.login_url, method="post", data=data, headers=headers).json()
    env_cookies = f'Bearer {res["access_token"]}'
    os.environ["cookies"] = env_cookies
    env.cookies = env_cookies

    return env_cookies


if __name__ == '__main__':
    print(auth("s211"))
