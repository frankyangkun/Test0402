# -*- coding:utf8 -*-
'''
pytest各种前后置的用法
'''

import pytest
import os
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

    # # 执行pytest单元测试，生成Allure报告，需要的数据存在/temp目录
    # pytest.main(['--alluredir', './temp'])
    # # 执行命令allure generate ./temp -o ./report --clean，生成测试报告
    # os.system('allure generate ./temp -o ./report --clean')
    # # 以上两条命令在pycharm pytest模式下运行只能生成temp里的报告数据，无法生成报告
    # # 必须用pycharm python模式运行才能生成报告
    # =================================================================================================
    # 总结一下用法，如果直接在pycharm里使用，上面两条命令可以直接写在main中，如果要在ci中使用，必须使用命令行执行
    # 1、先用pytest生成测试数据，pytest --alluredir=temp test_demo4.py
    # 2、有时候找不到allure命令，source ~/.bash_profile 生效一下
    # 3、生成allure报告，allure generate ./temp -o ./report --clean
    # 4、注意：jenkins中添加以上命令
    # 5、注意：不能把命令写在main中，然后用python3 xx.py的方式执行脚本