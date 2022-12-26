# coding:utf-8


class Environment:

    _env = {
        "single211": {
            "company_name": '111',
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
            "EntCode": "SUPERCARE251",
            "log_level": 'DEBUG',
            "kafka": '192.168.1.251:9092',
            "user": "admin",
            "password": "1q2w3E*",
            "api_url": "http://192.168.1.251:31000",
            "login_url": "http://192.168.1.251:5000/connect/token"
        },
        "cluster248": {
            "host": '192.168.0.248',
            "port": '9999',
            "api_port": '31000',
            "company_name": '110',
            "EntCode": "SUPERCARE248SQL",
            "log_level": 'warning',
            "kafka": '192.168.0.248:9092',
            "user": "admin",
            "password": "1q2w3E*"
        }
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

