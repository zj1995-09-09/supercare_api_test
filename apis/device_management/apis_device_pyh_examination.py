# coding:utf-8
import os
from datetime import datetime
from apis.base import Base


class Apis(Base):
    """
    单接口
    """

    def __init__(self):

        super(Apis, self).__init__()

    def api_get_report_year(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies")
        }
        self.data_default = {}
        self.params_default = {
            "_t": datetime.now()
        }
        method = "get"
        url = self.url + "/api/PhysicalExaminationReport/GetReportYear"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_get_reports(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies")
        }
        self.data_default = {}
        self.params_default = {
            "_t": datetime.now()
        }
        method = "get"
        url = self.url + "/api/PhysicalExaminationReport/GetReports"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_get_user_manage_device_tree(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
            "Content-Type": "application/json"
        }
        self.data_default = {}
        self.params_default = {
            "_t": datetime.now()
        }
        method = "post"
        url = self.url + "/api/basicService/api/app/manageAsset/getUserManageDeviceTree"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_dispoable_plan(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
            "Content-Type": "application/json"
        }
        self.data_default = {}
        self.params_default = {
            "_t": datetime.now()
        }
        method = "post"
        url = self.url + "/api/caseService/api/app/physicalExaminationPlan/dispoablePlan"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_delete_report(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {
            "_t": datetime.now()
        }
        method = "delete"
        url = self.url + "/api/PhysicalExaminationReport/DeleteReport"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_get_plans(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {
            "_t": datetime.now()
        }
        method = "get"
        url = self.url + "/api/PhysicalExaminationPlan/GetPlans"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_get_plan_global_setting(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {
            "_t": datetime.now()
        }
        method = "get"
        url = self.url + "/api/PhysicalExaminationPlan/GetPlanGlobalSetting"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_set_plan_global_setting(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Content-Type": "application/json",
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {
            "_t": datetime.now()
        }
        method = "put"
        url = self.url + "/api/PhysicalExaminationPlan/SetPlanGlobalSetting"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_add_or_edit_plan(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Content-Type": "application/json",
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {
            "_t": datetime.now()
        }
        method = "post"
        url = self.url + "/api/PhysicalExaminationPlan/AddOrEditPlan"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res

    def api_execute_immediately(self, data=None, params=None, headers=None):
        """
        :return:
        """
        self.headers_default = {
            "Authorization": os.getenv("cookies"),
        }
        self.data_default = {}
        self.params_default = {
            "_t": datetime.now()
        }
        method = "post"
        url = self.url + f"/api/caseService/api/app/physicalExaminationPlan/{params['id']}/executeImmediately"
        res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
        return res
