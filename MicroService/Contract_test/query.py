#! /usr/bin/env python
# -*- coding:utf8 -*-
"""
2020-06-25 20:19:31
公共方法
"""

import requests


# pact作为模拟生产者时，默认端口1234，做契约测试先访问的是模拟生产者服务，而不是真实的生产者服务
def get_cartoon_characters(name):
    resp = requests.get('http://localhost:1234/information', {'name': name})
    return resp
