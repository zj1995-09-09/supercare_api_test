#coding:utf-8
from common.tools import retry
import requests
import urllib.parse


@retry()
def http_request(url,method,data=None,params=None,headers=None,):

    res = None

    if str(method).upper() == 'GET':
        if params:
            res = requests.get(url, params=params, headers=headers)
        else:
            res = requests.get(url, headers=headers)

    if str(method).upper() == 'POST':

        if params:
            url = url + "?" + urllib.parse.urlencode(params)
        if data:
            res = requests.post(url=url, data=data, headers=headers)
        else:
            res = requests.post(url=url, headers=headers)

    if str(method).upper() == 'PUT':

        if params:
            url = url + "?" + urllib.parse.urlencode(params)
        if data:
            res = requests.put(url=url, data=data, headers=headers)
        else:
            res = requests.put(url=url, headers=headers)

    if str(method).upper() == 'DELETE':

        if params:
            res = requests.delete(url, params=params, headers=headers)
        else:
            res = requests.delete(url, headers=headers)

    return res

