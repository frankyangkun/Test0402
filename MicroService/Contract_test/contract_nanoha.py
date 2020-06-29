#! /usr/bin/env python
# -*- coding:utf8 -*-
"""
2020-06-28 16:25:28
Nanoha消费者服务和生产者服务之间的契约测试
模拟了消费者服务可能有『国家』字段，也可能没有该字段的场景，两种场景都通过
"""

import atexit  # 退出时资源自动释放,一般用来做一些资源清理的操作（网上说最好不用它）
# from atexit import register  # 有时候重启pycharm后会找不到atexit模块，也搜不到，需要重新安装一下register
import unittest
from pact import Consumer, Provider
from MicroService.Contract_test.query import get_cartoon_characters

# 构造pact对象，定义消费者服务的名字并给它绑定一个生产者服务
pact = Consumer('Consumer Nanoha').has_pact_with(Provider('Provider'))  # 为消费者绑定一个生产者，名字可随便取
pact.start_service()  # 启动pact服务(Start the external Mock Service.)
atexit.register(pact.stop_service)  # 注册退出时，关闭pact服务,stop_service不能要括号（register的固定写法）


class GetNanohaInfoContract(unittest.TestCase):
    def test_nanoha_with_nationality(self):  # 消费者服务有"国家"字段的情况
        expected = {
            "salary": 80000,
            "name": "Takamachi Nahoha",
            "nationality": "Japan",
            "contact": {
                "Email": "takamachi.nahoha@woniuxy.com",
                "Phone Number": "18783723445"
            }
        }
        headers = {
            "Content-Type": "application/json"
        }
        # 通过given去切换ProviderState状态的变化，从而控制Provider端运行测试之前修改对应nationality字段的值
        (
            pact
            .given('')  # 表示生产者服务有国家字段，消费者服务也有用到该字段时，就不需要设置given的值
            .upon_receiving('a request for Nanoha')
            .with_request(
                method='GET',
                path='/information',
                query={'name': 'nanoha'}
            )
            .will_respond_with(200, headers, expected))
        with pact:
            result = get_cartoon_characters('nanoha')
        self.assertEqual(result.json(), expected)

    def test_nanoha_no_nationality(self):  # 消费者服务没有"国家"字段的情况
        expected = {
            "salary": 80000,
            "name": "Takamachi Nahoha",
            "nationality": None,
            "contact": {
                "Email": "takamachi.nahoha@woniuxy.com",
                "Phone Number": "18783723445"
            }
        }
        headers = {
            "Content-Type": "application/json"
        }
        # 通过given去切换ProviderState状态的变化，从而控制Provider端运行测试之前修改对应nationality字段的值
        (
            pact
            .given('No nationality')  # 表示生产者服务有国家字段，但消费者服务没有用到该字段时，expected返回的是None
            .upon_receiving('a request for Nanoha')
            .with_request(
                method='GET',
                path='/information',
                query={'name': 'nanoha'}
            )
            .will_respond_with(200, headers, expected)
        )
        with pact:
            result = get_cartoon_characters('nanoha')
        self.assertEqual(result.json(), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
