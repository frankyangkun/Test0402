# -*- coding:utf8 -*-
"""
2020-06-05 14:28:03
 1. 使用的是pytest-mock 中的mocker
 2. 使用的 mock 中patch方法，是对目标函数的返回值进行替换，采用了with上下文进行管理
 3. 使用的装饰器的方式对mock对象的函数返回值进行替换

Python 目前有两个库可以使用,mock从3.3+就已经集成到unittest框架，而pytest-mock集成了mock所有功能，更加灵活强大。
注1：mock不是unittest自带的那个，需单独安装一下
注2：pytest-mock也需单独安装，import时名为pytest_mock
"""

import mock
import pytest
from pytest_mock import mocker
from pytestMock.mockRequest import invoke_mock_request


#使用pytest-mock中的mocker，ps：但这里即使不import pytest_mock也不影响，好像这个mocker是python自带的？
#并不是，如果不安装pytest-mock插件，运行会提示fixture 'mocker' not found，所以必须安装，可以不import
def test_get_foo(mocker):
    mocker.patch("pytestMock.mockRequest.mock_request", return_value=300)  # mock_request是依赖函数，将它mock掉
    assert invoke_mock_request("https://www.python.org/" == 300)


def test_get_foo2():  # 使用mock中patch方法对目标函数的返回值进行替换
    with mock.patch("pytestMock.mockRequest.mock_request", side_effetc=300) as mock_foo:  # 注意是side_effetc不是side_effect
        assert invoke_mock_request("https://www.python.org/") == mock_foo.return_value


@mock.patch("pytestMock.mockRequest.mock_request", return_value=300)  # 使用装饰器的方式对mock对象的函数返回值进行替换
def test_get_foo3(mock_request):
    assert invoke_mock_request("https://www.phthon.org/") == mock_request.return_value


if __name__ == '__main__':
    pytest.main()
