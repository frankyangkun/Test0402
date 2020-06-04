# -*- coding:utf8 -*-
"""
2020-06-04 14:44:37
测试unittest mock模块2
注：
add_add_multiply()和测试用例没有修改，但外部依赖函数multiply()发生修改，
会导致运行错误，所以需要把 multiply()函数mock掉
"""
import unittest
from unittest.mock import patch
from unittestMock.demo2_math import TestMath

class MyTestDemo2(unittest.TestCase):
    @patch("unittestMock.demo2_math.TestMath.multiply")  # 上下文管理器可以很容易地模拟类或对象在模块测试，类名必须写全
    def test_add_and_multiply(self, mock_multiply):
        x = 3
        y = 5
        mock_multiply.return_value = 15  # 重点：比之前多的这一行 （此时外部依赖函数multiply()已经发生了修改，之前的方法会报错）
        add, multiple = TestMath().add_add_multiply(x, y)  # 不要忘了实例化TestMath()，写成TestMath是不行的
        # self.assertEqual(8, add)  #unittest自带断言
        # self.assertEqual(15, multiple)

        mock_multiply.assert_called_once_with(3, 5)  # 比之前多的这一行 检查mock_multiply方法的参数是否正确
        assert add == 8  # python3自带断言
        assert multiple == 15


if __name__ == '__main__':
    unittest.main()