# -*- coding:utf8 -*-
"""
@pytest.fixture()的用法
scope="function" 默认，方法中可以使用
scope="class"  只能类中使用，类外面的方法就不能用了
scope="package"  包内的所有类都可以使用
scope="session"  所有包的所有类都可以使用
"""
import pytest
import os

@pytest.fixture()  # 将该函数作为参数传给其他函数，默认是scope="function"
def login():
    print("setup login...")
    yield  # 起到一个等待的作用，前面的执行完后，等待，去执行调用者的内容，然后再回来执行后面的内容
    print("teardown login...")


@pytest.fixture(scope="class", params=[1, 2, 3])
def login2(request):
    print("login2...")
    return request.param  # 必须写成param，params是错的，也算是pytest的固定写法


@pytest.fixture(scope="class", autouse=True)  # 应用于所有测试用例，类只使用一次，其中方法不再单独使用
def login3():
    print("login3**************")


class TestDemo5(object):
    @pytest.mark.others
    def test_01(login2):
        print(login2)

    def test_print_03(self, login2):
        print("test03...")

    def test_print_04(self, publictest, login):
        print("test04...")

    def test_print_05(self):
        print("test05")




if __name__ == '__main__':
    pytest.main(["-m","others"])
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