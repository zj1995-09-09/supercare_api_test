# -*- coding: utf-8 -*-
# @Author   : qiuzixuan
# @Time     : 2023/1/12
# @Desc     : 获取路径

from pathlib import Path


class GetPath:
    """ 获取路径信息，可以是目录也可以是文件，返回 Path 对象
    """

    def __init__(self, *root: str is None):
        """
        :param root: 指定返回路径下的一级目录
        """
        self.root = root

    def get_project_path(self, *args: str is None) -> Path:
        """ 基于项目根目录返回路径
        :param args: 传入的路径
        """
        project_path = Path(Path(__file__).parents[1], *self.root)
        return project_path if not args else Path(project_path, *args)

    def get_current_path(self, *args: str is None) -> Path:
        """ 基于当前文件返回路径
        :param args: 传入的路径
        """
        current_path = Path(Path('.').absolute(), *self.root)
        return current_path if not args else Path(current_path, *args)


if __name__ == '__main__':
    import datetime
    project_log_filename = 'runtime_{}.log'.format(datetime.date.today())
    a = GetPath('logs').get_project_path(project_log_filename)
    print(str(a))
