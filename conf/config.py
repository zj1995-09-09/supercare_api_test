# -*- coding: utf-8 -*-
# @Author   : qiuzixuan
# @Time     : 2023/1/12
# @Desc     :

from dynaconf import Dynaconf
from libs.get_path import GetPath

project_path = GetPath('conf')

settings = Dynaconf(
    settings_files=[
        project_path.get_project_path('.secrets.toml'),
        project_path.get_project_path('settings.toml')
    ],
)

if __name__ == '__main__':
    test_func = "single211"

    send_msg = getattr(settings, test_func)
    print(send_msg.api_url)
