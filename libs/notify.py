# -*- coding: utf-8 -*-
# @Author   : qiuzixuan
# @Time     : 2023/2/13
# @Desc     : 发送钉钉消息

import time
import hmac
import hashlib
import base64
import urllib.parse
from datetime import datetime

from pathlib import Path

from common.global_var import get_var
from common.request_module import http_request
from libs.logger import logger
from libs.config import settings
from pygit2 import Repository


def get_git_branch() -> str:
    """
    获取当前分支名称
    :return:
    """
    local_path = Path(__file__).parents[1].absolute()
    repo = Repository(local_path)
    return repo.head.name.split('/')[-1]


def get_sign() -> tuple:
    """
    :return: 钉钉加签
    """
    timestamp = str(round(time.time() * 1000))
    secret = settings.dingtalk.ding_talk_secret
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp, sign


def _getattr_text(tag, res) -> tuple:
    """
    预执行步骤的文本和颜色 hex
    :param tag: pytest mark 标签
    :param res: 运行结果
    :return:
    """
    hex_dict = {
        'failed': ['失败 ❌', '#c12c1f'],
        'passed': ['成功 ✅', '#2a6e3f'],
    }

    title = f"-{datetime.now().strftime('%d-%m-%Y')}"
    txt = str()
    tag = str(tag).strip()
    _button = list()
    res = 'failed' if res > 0 else 'passed'

    api_test_name = get_var()('test_name')

    # 不是特殊标记直接返回
    if tag not in ['jenkins_login', 'jenkins_sql_migrate']:
        report_url = urllib.parse.quote(f"http://192.168.1.238:8090/{api_test_name}.html")
        _button = [{
            "title": "测试报告详情", "actionURL": f"dingtalk://dingtalkclient/page/link?url={report_url}&pc_slide=false"
        }]
        title = f"BvtTest{title}"
        return title, None, hex_dict[res][-1], _button
    if tag == 'jenkins_login':
        txt = f'**BVT 测试{hex_dict[res][0]}**'
        title = f"SuperCareApiTest"
    if tag == 'jenkins_sql_migrate':
        title = f"SuperCareDeploy"
        txt = f'**部署-SQL升级{hex_dict[res][0]}**'
        report_url = urllib.parse.quote(f"http://192.168.1.238:8090/{api_test_name}-sql.html")
        _button = [{
            "title": "详情",
            "actionURL": f"dingtalk://dingtalkclient/page/link?url={report_url}&pc_slide=false"
        }]

    return title, txt, hex_dict[res][-1], _button


def send_dingtalk(**kwargs):
    """
    发送钉钉消息
    :return:
    """
    # 获取必要字段
    cur_branch = get_git_branch()
    logger.debug(f"The current branch: {cur_branch}")
    _access_token = settings.dingtalk.ding_talk_access_token \
        if cur_branch == 'main' else settings.dingtalk.test_ding_talk_access_token
    timestamp, sign = get_sign()
    res_count = kwargs['run_count']

    fail_num = res_count[2] + res_count[3]
    selected_num = res_count[1] + fail_num

    # 组装消息内容
    res_tag = kwargs['run_tag']
    _title, t, h, button = _getattr_text(res_tag, fail_num)

    title = f"# <font color={h}> {_title} </font> \n" \
            f"---  \n"
    content = f"- 总用例数: {res_count[0]} \n" \
              f"- 运行用例数: {selected_num} \n" \
              f"- 通过用例数: {res_count[1]} \n" \
              f"- 失败用例数: {fail_num} \n"
    params = {
        "access_token": _access_token,
        "timestamp": timestamp,
        "sign": sign
    }
    text = title + content
    if t:
        text = title + t

    data = {
        "msgtype": "actionCard",
        "actionCard": {
            "title": "SuperCare Api Test Report",
            "text": text,
            "btnOrientation": "1",
            "btns": button
        },
    }
    http_request(
        request_type='POST', host=settings.dingtalk.ding_talk_url, path=settings.dingtalk.ding_talk_path,
        params=params, data=data, headers={}
    )


if __name__ == '__main__':
    logger.debug(settings.dingtalk.ding_talk_secret)
