# -*- coding: utf-8 -*-
# @Author   : qiuzixuan
# @Time     : 2023/1/12
# @Desc     : 日志模块
import loguru
import datetime
from functools import wraps

from libs.config import settings
from libs.get_path import GetPath


def singleton_class_decorator(cls):
    """
    装饰器，单例类的装饰器
    """
    # 在装饰器里定义一个字典，用来存放类的实例。
    _instance = {}

    @wraps(cls)
    def wrapper_class(*args, **kwargs):
        # 判断，类实例不在类实例的字典里，就重新创建类实例
        if cls not in _instance:
            # 将新创建的类实例，存入到实例字典中
            _instance[cls] = cls(*args, **kwargs)
        # 如果实例字典中，存在类实例，直接取出返回类实例
        return _instance[cls]

    return wrapper_class


@singleton_class_decorator
class Logger:
    def __init__(self):
        self.logger_add()

    @staticmethod
    def logger_add():
        loguru.logger.add(
            sink=GetPath('logs').get_project_path(f'runtime_{datetime.date.today()}.log'),
            # 日志创建周期
            rotation='00:00',
            # 保存
            retention='1 months',
            # 文件的压缩格式
            compression='zip',
            # 编码格式
            encoding="utf-8",
            # 具有使日志记录调用非阻塞的优点
            enqueue=True,
            # 异常跟踪是否应显示变量值以简化调试
            diagnose=True,
            # 格式化消息中包含的颜色标记是否应转换为 ansi 代码以进行终端着色
            colorize=False,
            # 是否应向上扩展格式化的异常跟踪，超出捕获点，以显示生成错误的堆栈跟踪
            backtrace=True,
            # 日志级别
            level=settings.common.log_level,
        )

    @property
    def get_logger(self):
        return loguru.logger


'''
# 实例化日志类
在其他.py文件中，只需要直接导入已经实例化的logger类即可
例如导入访视如下：
from project.logger import logger
然后直接使用logger即可
'''
logger = Logger().get_logger


if __name__ == '__main__':
    logger.debug('调试代码')
    logger.info('输出信息')
    logger.success('输出成功')
    logger.warning('错误警告')
    logger.error('代码错误')
    logger.critical('崩溃输出')
