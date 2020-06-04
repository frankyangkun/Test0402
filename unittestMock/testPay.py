# -*- coding:utf8 -*-
"""
 2020-06-04 10:47:06
 测试unittest mock模块
"""
from unittest import mock
import unittest
from unittestMock import template


class Test_zhifu_status(unittest.TestCase):
    "单元测试用例"
    def test1(self):
        """测试支付成功"""
        # mock一个支付成功的数据
        template.zhifu = mock.Mock(return_value={"result": "success", "reason": "null"})
        # 根据支付结果测试页面跳转
        status = template.zhifu_status()
        print(status)
        # self.assertEqual(status, "支付成功")
        assert status == "支付成功"

    def test2(self):
        """测试支付失败"""
        # mock一个支付失败的数据
        template.zhifu = mock.Mock(return_value={"result": "fail", "reason": "余额不足"})
        # 根据支付结果测试页面跳转
        status = template.zhifu_status()
        print(status)
        assert status == "支付失败"


if __name__ == '__main__':
    unittest.main()