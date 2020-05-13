# -*- coding:utf8 -*-
"""
2020-05-13
原始请求
"""
import requests



class TestLogin(object):

    def test_login(self):
        url = "http://182.43.224.122:8002/interGateway/v3/user/authentication"
        headers = {"Content-Type": "application/json"}
        payload = {
            "loginAccount": "pzadmin",
            "password": "96E79218965EB72C92A549DD5A330112",
            "userType": "individual"
        }

        response = requests.request("POST", url, json=payload, headers=headers)  #json不能写成data否则 提示payloads不是json，但type(payload)显示就是dict，而加了json.loads(payload)又提示不能是dict
        # response = requests.post(url, headers=headers, json=payload)  # 这个就没有上面的问题
        print("!!!", response.json())
        assert response.json()["resultStatus"]["resultMessage"] == "登录成功！"
