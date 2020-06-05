# -*- coding:utf8 -*-
"""
2020-06-05 14:24:49
其中一个函数依赖上一个函数的返回值，
就是mock实际项目测试过程场景中，接口中的依赖关系
"""
import requests


def mock_request(url):
    return requests.get(url).status_code


def invoke_mock_request(url):
    return mock_request(url)