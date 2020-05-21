# -*- coding:utf8 -*-

import pytest
# from utils.common import collect_static_data  # 提示找不到utils.common
import utils  # 这么写可以


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    所有的测试用例收集完毕后调用，可以再次过滤或者对它们重新排序
    items（收集的测试项目列表）
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def pytest_generate_tests(metafunc):
    """
    generate(multiple)parametrized calls to a test function.
    """
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param", metafunc.module.par_to_test, ids=metafunc.module.case, scope="function")


def pytest_addoption(parser):
    group = parser.getgroup('yangkun auto test')
    group.addoption(
        "--env",
        default="test",
        dest="env",
        help="set test run env")
    group.addoption(
        "--env1",
        default="test1",
        dest="env1",
        help="set test run env")


# @pytest.fixture(scope="session")
# def cmdopt(request):  # pytestconfig通过配置对象读取参数的值，这里换成了request
#     return request.config.yml.getoption("--env", default='test')  # 这里应该就是从yaml文件中读取--env的值
#
#
# @pytest.fixture(scope="session", autouse=True)
# def env(request, cmdopt):  # 这里的cmdopt就是yaml中的--env  request就是和cmdopt的作用一样，读取数据用的
#     # load remote config.yml settings
#     request.config.yml.base_data = collect_static_data(cmdopt, str(request.config.yml.rootdir))  # 找不到collect_static_data
#     return request.config.yml.base_data
