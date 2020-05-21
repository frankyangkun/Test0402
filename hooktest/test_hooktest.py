# -*- coding:utf8 -*-
"""
2020-05-19
测试hook函数pytest_addoption和pytest_runtest_makereport的用法
注意：测试用例文件必须是test_开头，否则纯python模式运行后，pytest识别不了用例，allure里就没内容
而pytest模式直接在pycharm运行的话，是可以识别的，即使文件名不以test_开头
"""
import pytest
import os


class TestHook(object):

    def setup(self):
        print("setup...")

    def test_1(self):
        print("test1......")
        assert 1 == 1

    def test_2(self):
        print("test2...")
        assert 2 == 3

    def teardown(self):
        print("teardown...")


if __name__ == '__main__':
    #     # 使用参数
    #     pytest.main(['-s', '--cmdopt=98k'])

    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir', './temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./temp -o ./report --clean')
