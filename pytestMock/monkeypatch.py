# -*- coding:utf8 -*-
"""
2020-06-05 15:59:11
有时候，测试用例需要调用某些依赖于全局配置的功能，或者这些功能本身又调用了某些不容易测试的代码（例如：网络接入）。
fixture monkeypatch可以帮助你安全的设置/删除一个属性、字典项或者环境变量，甚至改变导入模块时的sys.path路径。

使用monkeypatch.setattr()可以将函数或者属性修改为你希望的行为
使用monkeypatch.delattr()可以删除测试用例使用的函数或者属性
---------------------------------------------------------------------------
这个例子中，使用monkeypatch.setattr()修改Path.home方法，
在测试运行期间，它一直返回的是固定的Path("/abc")，这样就移除了它在不同平台上的依赖；
测试运行完成后，对Path.home的修改会被撤销
"""

from pathlib import Path

def getssh():
    print(Path.home() / ".ssh")  # 正常是/Users/yang/.ssh
    return Path.home() / ".ssh"

def test_getssh(monkeypatch):
    def mockreturn():
        return Path("/abc")  # 替换后变成了./abc/.ssh

    # 替换Path.home，需要在真正的调用之前执行
    monkeypatch.setattr(Path, "home", mockreturn)

    # 将会使用mockreturn代替Path.home
    x = getssh()
    assert x == Path("/abc/.ssh")

