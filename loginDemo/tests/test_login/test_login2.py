# -*- coding:utf8 -*-
"""
2020-05-13
测试数据分离
"""
import requests
import pytest

param = [
    ({"Content-Type": "application/json"}, {"loginAccount": "pzadmin", "password": "96E79218965EB72C92A549DD5A330112", "userType": "individual"}),
    ({"Content-Type": "application/json"}, {"loginAccount": "201808230@sefon.com", "password": "96E79218965EB72C92A549DD5A330112", "userType": "individual"}),
    ({"Content-Type": "application/json"}, {"loginAccount": "pzadmin", "password": "123", "userType": "individual"})
]


class TestLogin(object):

    @pytest.mark.parametrize("headers,payload", param)
    def test_login(self, headers, payload):
        url = "http://182.43.224.122:8002/interGateway/v3/user/authentication"
        response = requests.request("POST", url, json=payload, headers=headers)  #json不能写成data否则 提示payloads不是json，但type(payload)显示就是dict，而加了json.loads(payload)又提示不能是dict
        # response = requests.post(url, headers=headers, json=payload)  # 这个就没有上面的问题
        print("!!!", response.json())
        assert response.json()["resultStatus"]["resultMessage"] == "登录成功！"
