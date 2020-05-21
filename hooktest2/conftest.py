# -*- coding:utf8 -*-
"""
2020-05-21
pytest_runtest_makereport的实际应用
实际应用：获取用例执行结果处理用例依赖：
因为部分用例必须依赖前面某个用例，当前置用例失败后，后续用例必定会失败并且非常耗时，所以我们可以用这个钩子方法来处理这个问题，跳过依赖的用例。
"""
import pytest


# 定义一个类，用来存储用例执行失败的结果
class Failed():
    skip = False


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport():
    result = yield
    report = result.get_result()

    # 当前用例名
    case_name = report.nodeid.split('::')[-1]

    # 当某个用例失败（setup失败也算）或被跳过时，将这个用例执行结果存放在Failed类中
    # report结果类似 <TestReport 'test_hooktest.py::TestHook::test_1' when='setup' outcome='passed'>
    if report.when in ('setup', 'call') and report.outcome in ('failed', 'skipped'):
        setattr(Failed, case_name, True)  # setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的。这里就是设置了一个暂不存在的属性case_name
        # print('@@@@@', getattr(Failed, case_name))  # 结果为True


# if __name__ == '__main__':
#     pytest.main(['-s','-q'])
