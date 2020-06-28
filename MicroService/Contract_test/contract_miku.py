#! /usr/bin/env python
# -*- coding:utf8 -*-
"""
2020-06-25 20:26:40
Miku消费者服务和生产者服务之间的契约测试

注：这里不需要启动consumer_miku，因为它访问的是8080真实生产者服务
在此脚本里已经调用了query中的模拟消费者服务，访问的是1234pact模拟生产者服务
"""

import atexit  # 退出时资源自动释放,一般用来做一些资源清理的操作
# from atexit import register  # 有时候重启pycharm后会找不到atexit模块，也搜不到，需要重新安装一下register
import unittest
from pact import Consumer, Provider
from MicroService.Contract_test.query import get_cartoon_characters

# 构造pact对象，定义消费者服务的名字并给它绑定一个生产者服务
pact = Consumer('Consumer Miku').has_pact_with(Provider('Provider'))  # 为消费者绑定一个生产者，名字可随便取
pact.start_service()  # 启动pact服务(Start the external Mock Service.)
atexit.register(pact.stop_service)  # 注册退出时，关闭pact服务,stop_service不能要括号


class GetMikuInfoContract(unittest.TestCase):
    def test_miku(self):
        # 定义响应的期望结果
        expected = {
            "salary": 45000,
            "name": "Hatsune Miku",
            "nationality": "Japan",
            "contact": {
                "Email": "hatsune.miku@woniuxy.com",
                "Phone Number": "13982739999"
            }
        }
        # 定义响应头
        headers = {
            "Content-Type": "application/json"
        }
        # 定义模拟生产者接受请求以及响应方式
        (pact
         .upon_receiving('a request for Miku')
         .with_request(
            method='GET',
            path='/information',
            query={'name': 'miku'})  # 如果是post请求，就是body=
         .will_respond_with(200, headers, expected))
        # 定义消费者服务向模拟生产者发出请求并获得响应
        with pact:  # 让pact去做请求
            result = get_cartoon_characters('miku')
        # 断言
        self.assertEqual(result.json(), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行前要先启动消费者服务，因为pact是模拟生产者
