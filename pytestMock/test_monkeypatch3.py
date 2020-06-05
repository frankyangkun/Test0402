# -*- coding:utf8 -*-
"""
2020-06-05 17:03:41
通过fixture跨用例共享pytest monkeypatch
(如果想让mock_response应用于所有的测试用例，可考虑将它移到conftest.py里，并标记autouse=True)
"""
from urllib import request

from pytestMock.monkeypatch2 import get
from pytestMock.test_monkeypatch2 import MockResponse
import pytest


# monkeypatch 是 function 级别作用域的，所以 mock_response 也只能是 function 级别，
# 否则会报 ScopeMismatch

@pytest.fixture
def mock_response(monkeypatch):
    def mock_urlopen(*args, **kwargs):
        return MockResponse()

    # 使用request.mock_urlopen代替request.urlopen
    monkeypatch.setattr(request, "urlopen", mock_urlopen)  # mock_urlopen不能加括号


# 使用mock_response代替原先的monkeypatch
def test_get_fixture1(mock_response):
    data = get("http://140.246.137.19:45680")
    assert data == "yangkun.com"


# 使用mock_response代替原先的monkeypatch
def test_get_fixture2(mock_response):
    data = get("http://www.baidu.com")
    assert data == "yangkun.com"


if __name__ == '__main__':
    pytest.main()
