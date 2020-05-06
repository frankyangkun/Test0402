# -*- coding:utf8 -*-
"""
@pytest.mark.parametrize不能和unittest混用（不能unittest.TestCase）
否则报missing 2 required positional arguments: 'a' and 'b'
由于继承了unittest.TestCase，就要用unittets模式运行，unittest没法直接调用pytest的这两个参数
所以如果继承了unittest.TestCase，就用ddt，或者@parameterized.expand
如果想用pytest的参数化，就继承obecjt，而不是unittest.TestCase
"""
import pytest
import unittest


@pytest.mark.parametrize('a,b', [(1, 1), (2, 2)])
class TestDDT(object):  # class必须大写Test开头
    def test1(self, a, b):
        assert a == b


if __name__ == '__main__':
    pytest.main()
