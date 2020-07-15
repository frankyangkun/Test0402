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


if __name__ == '__main__':
    # 执行pytest单元测试，生成Allure报告，需要的数据存在/temp目录
    pytest.main(['--alluredir', './temp'])
    # 执行命令allure generate ./temp -o ./report --clean，生成测试报告
    os.system('allure generate ./temp -o ./report --clean')
    # 以上两条命令在pycharm pytest模式下运行只能生成temp里的报告数据，无法生成报告
    # 必须用pycharm python模式运行才能生成报告
    # =================================================================================================
    # 总结一下用法，如果直接在pycharm里使用，上面两条命令可以直接写在main中，如果要在ci中使用，必须使用命令行执行
    # 1、先用pytest生成测试数据，pytest --alluredir=temp test_demo4.py
    # 2、有时候找不到allure命令，source ~/.bash_profile 生效一下
    # 3、生成allure报告，allure generate ./temp -o ./report --clean
    # 4、注意：jenkins中添加以上命令
    # 5、注意：不能把命令写在main中，然后用python3 xx.py的方式执行脚本