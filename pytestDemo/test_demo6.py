# -*- coding:utf8 -*-
"""
2020-05-12
pytest配置文件ini中配置自定义标签@pytest.mark.xxx
用纯python模式运行，pytest模式运行不行。
最好还是用命令执行，如
pytest -m "me" test_demo6.py   指定标签名
pytest -k "print" test_demo5.py  指定用例关键字
"""
import pytest
import os

@pytest.mark.me  # 框架自带的是@pytest.mark.run或stop，不用配置ini
def test_001():
    print("test_01")


@pytest.mark.you
def test_002():
    print("test_02")


@pytest.mark.me
def test_003():
    print("add_test")


def add(x, y):
    return x + y


@pytest.mark.others
def test_add():
    assert add(1, 1) == 2


@pytest.mark.others
def test_id():
    userid = 1234
    print(userid)


# if __name__ == '__main__':
#     pytest.main(["-m","me"])
    # os.system('allure generate ./temp -o ./report --clean')