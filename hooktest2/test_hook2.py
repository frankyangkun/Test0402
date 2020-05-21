# -*- coding:utf8 -*-
"""
2020-05-21 15:39:01
获取所依赖的用例执行结果，如果falied或skip，则不执行当前用例直接跳过。
"""
import pytest
from hooktest2.conftest import Failed
import os

class TestDemo():
    def test1(self):
        assert 1 == 11  # 断言失败，模拟用例执行失败

    def test2(self):
        # 从Failed获取test1的执行结果，如果getattr结果为True，表示依赖的用例失败或跳过
        # 必须加默认值False，否则如果用例全对，会报错Failed类没有test1属性(因为该属性是失败了才会设置的)，所以加了后if的结果就是False，就不会执行下面的skip命令了，用例照常执行
        if getattr(Failed, 'test1', False):
            # print('!!!!', getattr(Failed, 'test1'))  # 这里结果是True
            pytest.skip('所依赖用例test1执行失败或被跳过，此用例跳过！')
        print("test2....")

    def test3(self):
        print("test3...")


if __name__ == '__main__':
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir', './temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./temp -o ./report --clean')