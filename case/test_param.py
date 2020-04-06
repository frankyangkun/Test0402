# -*- coding:utf8 -*-
"""
parameterized参数化组件的使用
安装：pip install parameterized
使用：@parameterized.expand(参数)
    参数：
        单个参数格式：列表，如[值1，值2]
        多个参数格式：列表嵌套元组，如[(值1，值2)]
测试需求：输出帐号密码，数据分别为admin,123456   user2,654321
"""

#导包
import unittest
from parameterized import parameterized

#新建测试类
class TestPara(unittest.TestCase):
    @parameterized.expand([("admin","123456"),("user2","654321")])
    def test_para(self,username,password):
        print "用户名：",username
        print "密码：",password
