# coding:utf-8


class Environment:

    _env = {
        "single211": {
            "company_name": '111',
            "company_type": "IndustryType_GT",
            "supercare_type": "Standard",  # Professional
            "EntCode": "SUPINTERFACE",
            "log_level": 'DEBUG',
            "kafka": '192.168.1.211:9092',
            "user": "admin",
            "password": "1q2w3E*",
            "api_url": "http://192.168.1.211:31000",
            "login_url": "http://192.168.1.211:5000/connect/token"
        },
        "single251": {
            "company_name": 'supercare251',
            "company_type": "IndustryType_FD",
            "supercare_type": "Standard",  # Professional
            "EntCode": "SUPERCARE251",
            "log_level": 'DEBUG',
            "kafka": '192.168.1.251:9092',
            "user": "admin",
            "password": "1q2w3E*",
            "api_url": "http://192.168.1.251:31000",
            "login_url": "http://192.168.1.251:5000/connect/token"
        },
        "cluster138": {
            "company_name": '138企业',
            "company_type": '',
            "supercare_type": "Professional",  # Standard
            "EntCode": "Supercare138testall",
            "log_level": 'DEBUG',
            "kafka": '192.168.1.251:9092',
            "user": "admin",
            "password": "1q2w3E*",
            "api_url": "http://192.168.1.138:31000",
            "login_url": "http://192.168.1.138:9999/identityserver/connect/token"
        },
    }

    def __init__(self, env):
        if env:
            self.env = env
        else:
            raise "FATAL ERROR!"

    @property
    def env_company_name(self):
        return self._env[self.env]['company_name']

    @property
    def env_ent_code(self):
        return self._env[self.env]['EntCode']

    @property
    def env_kafka(self):
        return self._env[self.env]['kafka']

    @property
    def env_user(self):
        return self._env[self.env]['user']

    @property
    def env_password(self):
        return self._env[self.env]['password']

    @property
    def env_login_url(self):
        return self._env[self.env]['login_url']

    @property
    def env_api_url(self):
        return self._env[self.env]['api_url']

    @property
    def env_company_type(self):
        return self._env[self.env]['company_type']

    @property
    def env_supercare_type(self):
        return self._env[self.env]['supercare_type']