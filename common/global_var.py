# -*- coding: utf-8 -*-
# @Author   : qiuzixuan
# @Time     : 2023/2/13
# @Desc     :

import time
from datetime import datetime
# from common.auth import auth
# from libs.logger import logger


global_var_dict = dict()


def set_var():
    """
    :return:
    """
    def _set_var(key, value):
        global_var_dict[key] = value
    return _set_var


def get_var():
    def _get_var(key):
        try:
            # 对 test_name 做特殊处理，保证一次运行的名称是同一个
            if key not in global_var_dict and key == "test_name":
                test_name_daemo = datetime.now().strftime('%Y%m%d%H')
                set_var()('test_name', test_name_daemo)
                return test_name_daemo

            # 直接获取 login token
            # if key not in global_var_dict and key == "login":
            #     logger.warning(f"当前全局变量没有 login token，开始自动获取...")
            #     login_token = login()
            #     set_var()('login', login_token)
            #     return login_token
            return global_var_dict[key]
        except KeyError:
            return None
    return _get_var


if __name__ == '__main__':
    set_var()('token', '123')
    print(get_var()('test_name'))
    time.sleep(2)
    print(get_var()('test_name'))
    print(get_var()('token'))
    print(get_var()('login'))

