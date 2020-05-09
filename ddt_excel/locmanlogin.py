# -*- coding:utf8 -*-
"""
    目标：实现登录接口对象封装
"""
# 导包 requests
import requests
from ddt_excel.DDTReadExcel import ddtreadexcel
import json

# 新建类 登录接口对象
class LocmanLogin(object):
    # 新建方法 登录方法
    def locman_login(self, url, body):
        # headers，data 定义，调用post并返回响应对象
        headers = {"Content-Type": "application/json"}
        resp = requests.post(url, headers=headers, json=body)
        return resp.json()  # 返回的是个对象，必须.json()显示


if __name__ == '__main__':
    cases = ddtreadexcel().getdata2()
    # print("*******", cases, type(cases))  # list
    for data in cases:
        body = data['请求参数']
        # print("XXXXX", body, type(body))  # 目前的body是str类型，需转换为json格式
        j = json.loads(body)  # 将str类型的body转换为json类型
        # print("jsonXXXXX", j, type(j))

        result = LocmanLogin().locman_login("http://182.43.224.122:8002/interGateway/v3/user/authentication", j)
        # print("result&&&", result)
        actualAssert = result['resultStatus']
        # print("actualAssert---", actualAssert, type(actualAssert))

        actualCode = result['resultStatus']['resultCode']  # 必须是json格式才能这样获取
        actualMsg = result['resultStatus']['resultMessage']

        expect = data['断言']
        # print("expect----", expect,type(expect)) # 不能写成 data['断言']['resultCode']，因为不是json
        expect1 = json.loads(expect)
        expectCode = expect1['resultCode']
        expectMsg = expect1['resultMessage']

        # print("yyyyyy",expectCode,expectMsg)
        assert actualCode == expectCode
        assert actualMsg == expectMsg
