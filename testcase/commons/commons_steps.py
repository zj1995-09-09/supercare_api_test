# coding: utf-8

from apis.commons.apis_commons import Apis


class ApisUtils(Apis):

    def __init__(self):
        super(ApisUtils, self).__init__()

    def get_user_message(self):
        """
        获取用户通知
        """
        filter_params = '{"logic":"and","filters":[{"field":"isDeleted","operator":"eq","value":False},' \
                        '{"field":"userId","operator":"eq","value":"39fe8e4c-5292-d5da-a219-caa9fafa3913"}]}'

        params = {
            "skipCount": 0,
            "sorting": "creationTime desc",
            "filter": filter_params
        }