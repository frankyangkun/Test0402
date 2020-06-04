# -*- coding:utf8 -*-
"""
2020-06-04 14:44:37
测试unittest mock模块2
这里是正常用例，没有mock的情况
"""
import unittest
from unittestMock.demo2_math import TestMath

class MyTestDemo2(unittest.TestCase):
    def test_add_and_multiply(self):
        x = 3
        y = 5
        add, multiple = TestMath().add_add_multiply(x, y)  # 不要忘了实例化TestMath()，写成TestMath是不行的
        # self.assertEqual(8, add)  #unittest自带断言
        # self.assertEqual(15, multiple)

        assert add == 8  # python3自带断言
        assert multiple == 15


if __name__ == '__main__':
    unittest.main()