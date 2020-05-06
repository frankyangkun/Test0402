# -*- coding:utf8 -*-
"""
@pytest.fixture()的用法
scope="function" 默认，方法中可以使用
scope="class"  只能类中使用，类外面的方法就不能用了
scope="package"  包内的所有类都可以使用
scope="session"  所有包的所有类都可以使用
"""
import pytest


@pytest.fixture()  # 将该函数作为参数传给其他函数，默认是scope="function"
def login():
    print("login...")


@pytest.fixture(scope="class", params=[1, 2, 3])
def login2(request):
    print("login2...")
    return request.param  # 必须写成param，params是错的，也算是pytest的固定写法


@pytest.fixture(scope="class", autouse=True)  # 应用于所有测试用例，类只使用一次，其中方法不再单独使用
def login3():
    print("login3**************")


def test_01(login2):
    print(login2)


class TestDemo5(object):
    def test_03(self, login2):
        print("test03...")

    def test_04(self, publictest, login):
        print("test04...")

    def test_05(self):
        print("test05")


if __name__ == '__main__':
    pytest.main()
