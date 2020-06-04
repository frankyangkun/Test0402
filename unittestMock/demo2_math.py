# -*- coding:utf8 -*-
"""
2020-06-04 14:40:14
测试unittest mock模块2

"""
class TestMath():
    def add_add_multiply(self, x, y):
        add = x + y
        multiply = self.multiply(x, y)
        return add, multiply


    def multiply(self, x, y):
        return x * y


