# -*- coding:utf8 -*-
"""
公共方法,基于pytest，文件名必须叫conftest
"""
import pytest


@pytest.fixture(scope="package")
def publictest():
    print("public method...")
