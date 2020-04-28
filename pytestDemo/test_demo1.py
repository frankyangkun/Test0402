# -*- coding:utf8 -*-
import pytest
import allure

def add(x):
    return x + 1


def test1():
    print ("测试一下")
    assert add(3) == 5


def test2():
    print ("test2")
    # assert 1 == 2


class TestCase(object):
    # def __init__(self):  # 使用pytest，测试类中不能有init方法
    #     pass

    def test3(self):
        print ("test3")
        assert 1 == 2

    def test4(self):
        print ("test4")
        # assert 1 == 2