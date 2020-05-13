# -*- coding:utf8 -*-
"""
2020-05-13
读取json文件获取测试数据
"""
import requests
import pytest
import os

from loginDemo.utils.get_data import get_test_data, get_data_path

case, param = get_test_data(get_data_path(__file__))

class TestLogin(object):

    @pytest.mark.parametrize("case,headers,payload,expected", param, ids=case)  # ids就是个别名
    def test_login(self, case, headers, payload, expected):
        url = "http://182.43.224.122:8002/interGateway/v3/user/authentication"
        response = requests.request("POST", url, json=payload, headers=headers)  #json不能写成data否则 提示payloads不是json，但type(payload)显示就是dict，而加了json.loads(payload)又提示不能是dict
        # response = requests.post(url, headers=headers, json=payload)  # 这个就没有上面的问题
        print("!!!", response.json())

        assert response.json()["resultStatus"]["resultMessage"] == "登录成功！"

if __name__ == "__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir', '../../temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ../../temp -o ../../report --clean')