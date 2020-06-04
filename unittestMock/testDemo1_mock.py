# -*- coding:utf8 -*-
"""
2020-06-04 16:19:57
补充unittest mock的另一种实现方式：@patch
"""
# from unittest.mock import patch
from unittest import mock  # 如果上面那样写，下面就直接@patch
import unittest
from unittestMock.demo1_class import Zhifu, Status


class Test_zhifu_status(unittest.TestCase):
    """单元测试用例"""

    @mock.patch("unittestMock.demo1_class.Zhifu.zhifu")  # 也可直接是@patch
    def test1(self, mock_zhifu):
        """
        支付成功的场景
        :param mock_zhifu:
        :return:
        """
        mock_zhifu.return_value = {"result": "success", "reason": "null"}
        status = Status().zhifu_status()
        print(status)
        self.assertEqual(status, "支付成功")

    @mock.patch("unittestMock.demo1_class.Zhifu.zhifu")
    def test2(self, mock_zhifu):
        """
        支付失败的场景
        :param mock_zhifu:
        :return:
        """
        mock_zhifu.return_value = {"result": "fail", "reason": "余额不足"}
        status = Status().zhifu_status()
        print(status)
        self.assertEqual(status, "支付失败")


if __name__ == '__main__':
    unittest.main()
