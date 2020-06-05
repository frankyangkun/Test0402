# -*- coding:utf8 -*-
"""
2020-06-05 16:13:37
使用monkeypatch.setattr()结合类，模拟函数的返回对象
"""

# 现在要去模拟r，它需要一个.read()方法返回的是bytes的数据类型；我们可以在测试模块中定义一个类来代替r
from urllib import request
from pytestMock.monkeypatch2 import get

# 自定义类模拟urlopen的返回值
class MockResponse:
    # 永远返回一个固定的bytes类型的数据
    @staticmethod
    def read():
        return b'yangkun.com'


def test_get(monkeypatch):
    def mock_urlopen(*args, **kwargs):  # 将网页返回内容mock掉
        return MockResponse()

    # 使用request.mock_urlopen代替request.urlopen
    monkeypatch.setattr(request, "urlopen", mock_urlopen)

    data = get("http://140.246.137.19:45680")
    assert data == "yangkun.com"
