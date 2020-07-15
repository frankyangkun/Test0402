# -*- coding:utf8 -*-
"""
2020-05-19
测试hook函数pytest_addoption和pytest_runtest_makereport的用法
"""
# import null as null
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


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
        每个测试用例执行后，制作测试报告
    　　:param item:测试用例对象
    　　:param call:测试用例的测试步骤
            先执行when=’setup’ 返回setup 的执行结果
            然后执行when=’call’ 返回call 的执行结果
            最后执行when=’teardown’返回teardown 的执行结果
    　　:return:
    """
    # 获取钩子方法的调用结果,返回一个result对象
    out = yield  # 带有 yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代
    # 应该是由于一个用例的多个步骤都要调用，setup调用时out return的是null，然后返回结果get_result，接着call和teardown调用时out也是null
    # 获取调用结果的测试报告，返回一个report对象, reportd对象的属性包括when（steup, call, teardown三个值）、nodeid(测试用例的名字)、outcome(用例的执行结果，passed,failed)
    report = out.get_result()  # 必须是yield才是生成器，才有get_result去获得3次调用的结果

    print("*****out*****", out)
    print("*****report*****", report)
    print("*****report.when*****", report.when)
    print("*****report.nodeid*****", report.nodeid)
    print("*****report.outcome*****", report.outcome)
