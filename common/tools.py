# coding:utf-8

import time
from loguru import logger
import mimetypes


def retry(times=1, wait_time=1):
    def in_fun(fun):

        def testfn(*args, **kwargs):
            count = 1
            while count < times + 1:
                try:
                    r = fun(*args, **kwargs)
                    return r
                except Exception as e:
                    logger.info("Retry Times：{},Retry Reason：{}".format(count, e))
                    time.sleep(wait_time)
                    count += 1
            logger.error("Retry More than %s Times!" % times)
            return False

        return testfn
    return in_fun


def get_content_type(filename):
    """
    获取到文件的content类型
    :param filename:
    :return:
    """
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
