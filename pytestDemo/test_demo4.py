# -*- coding:utf8 -*-
'''
pytest各种前后置的用法
'''

import pytest

def setup_module():
    print("模块级别的setup")


def teardown_module():
    print("模块级别的teardown")


def setup_function():
    print("函数级别的setup")


def teardown_function():
    print("函数级别的teardown")


def test_one():
    print("这是test_one...........")


class TestDemo4():  # 测试类必须是Test开头，必须是大写，否则pytest识别不了

    def setup_class(self):
        print("类级别的setup")

    def teardown_class(self):
        print("类级别的teardown")

    def setup_method(self):
        print("方法级别的setup")

    def teardown_method(self):
        print("方法级别的teardown")

    def setup(self):
        print("普通的setup")

    def teardown(self):
        print("普通的teardown")

    def test_4(self):
        print("这是测试用例..............")


if __name__ == '__main__':
    pytest.main()



