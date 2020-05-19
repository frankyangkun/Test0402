# -*- coding:utf8 -*-
"""
2020-05-19
测试hook函数pytest_addoption的用法
"""
import pytest


# 注册自定义参数 cmdopt 到配置对象
def pytest_addoption(parser):  # parser是用户命令行参数与ini文件值的解析器
    parser.addoption("--cmdopt", action="append_const",
                     const="常量。。。",
                     default=["这个是默认值..."],
                     help="将命令行参数 ’--cmdopt' 添加到 pytest 配置中")


# 从配置对象中读取自定义参数的值，然后任何 fixture 或测试用例都可以调用 cmdopt 来获得设备信息
@pytest.fixture(scope="session")
def cmdopt(request):  # pytestconfig通过配置对象读取参数的值，这里换成了request
    return request.config.getoption("--cmdopt")  # 这个应该就是从命令行输入的--cmdopt参数去获取它的具体值


# 将自定义参数的值打印出来
@pytest.fixture(autouse=True)
def fix_1(cmdopt):
    print('\n --cmdopt的值：', cmdopt)
