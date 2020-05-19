# -*- coding:utf8 -*-
"""
2020-05-19
测试hook函数pytest_addoption的用法
"""
import pytest


class TestHook():
    def test_1(self):
        print("test1......")


# if __name__ == '__main__':
#     # 使用参数
#     pytest.main(['-s', '--cmdopt=98k'])