# -*- coding:utf8 -*-
"""
2020-05-26 10:08:46
因为pytest识别用例的前提是不能有__init__初始化方法，而Locust继承的TaskSet就有，所以就识别不了。
而且我的Logger模块里也有，所以看来两者是不能写在一起的
就算用纯python模式运行，也会因为无法使用pytest的参数化功能而报错，所以locust和pytest彻底无法兼容

需要和python的参数化@parameterized.expand结合使用来达到目的，实现不同用户随机登录
"""
# 导入相关的locust的类，成员
from locust import HttpUser, TaskSet, task, between  # HttpLocust已经在1.0版本改为了HttpUser
from logger.loggerDemo.logger import Logger
# from loginDemo.utils.get_data import get_test_data, get_data_path
# from Locust.utils.get_data import get_test_data, get_data_path
from parameterized import parameterized
from tools.read_json import ReadJson

import os


# case, param = get_test_data(get_data_path(__file__))  # __file__当前文件路径
# print("^^^^^^",case,param)  # 可以获取到数据
def get_data():  # 处理返回的json中字典内容，达到我们要求的[()]格式
    datas = ReadJson("test_login/login_more.json").read_json()
    arrs = []
    print("xxx", datas)
    for i in datas.values():  # 遍历获取所有value,取出'test'的内容
        print("***", len(i), i)

        for data in i:  # 遍历获取list所有值
            # append本身添加的就是[]，而我们需要的是[()]，所以里面要加上(),否则就把所有内容都添加到一个列表里了
            print("yyy", data)
            arrs.append((data.get("case"),  # data["url"]和get方式的区别是前者如果获取错误会报异常，后者则为空
                         data.get("headers"),
                         data.get("payload"),
                         data.get("expected")
                         ))
    return arrs


# 任务类
class TestLogin(TaskSet):
    # 注释部分是尝试和pytest结合，但失败了
    # logger = Logger(file_or_terminal="all", level="ERROR").getLogger()

    # def setup(self):
    #     # self.logger.info("--------%s setup-----------" % __name__)
    #     print("***setup***")

    # @task(1)
    # @pytest.mark.parametrize("case,headers,payload,expected", param, ids=case)  # ids就是个别名
    # def test_login(self, case, headers, payload, expected):
    #     url = "/interGateway/v3/user/authentication"  # http://182.43.224.122:8002在命令行用locust命令时加
    #     response = requests.request("POST", url, json=payload,
    #                                 headers=headers)  # json不能写成data否则 提示payloads不是json，但type(payload)显示就是dict，而加了json.loads(payload)又提示不能是dict
    #     # response = requests.post(url, headers=headers, json=payload)  # 这个就没有上面的问题
    #     print("!!!", response.json())
    #
    #     assert response.json()["resultStatus"]["resultMessage"] == "登录成功！"
    #     # self.logger.error("---------%s error------------" % __name__)

    logger = Logger(file_or_terminal="all", level="ERROR").getLogger()
    logger.error("---------%s ERROR------------" % __name__)

    @parameterized.expand(get_data())
    @task(1)
    def test_login(self, case, headers, payload, expected):
        url = "http://182.43.224.122:8002/interGateway/v3/user/authentication"
        # headers = {"Content-Type": "application/json"}
        # payload = {
        #     "loginAccount": "pzadmin",
        #     "password": "96E79218965EB72C92A549DD5A330112",
        #     "userType": "individual"
        # }
        response = self.client.post(url, json=payload, headers=headers)  # 注意locust请求和普通requests的区别
        # response = requests.request("POST", url, json=payload, headers=headers)  # json不能写成data否则 提示payloads不是json，但type(payload)显示就是dict，而加了json.loads(payload)又提示不能是dict
        # response = requests.post(url, headers=headers, json=payload)  # 这个就没有上面的问题
        print("!!!", response.json())
        assert response.json()["resultStatus"]["resultMessage"] == expected
        self.logger.error("---------%s Locust ERROR Info------------" % __name__)  # 这里的日志打不出来，不知道为什么

    # def tearDown(self):
    #     # self.logger.info("---------%s teardown----------" % __name__)
    #     print("***teardown***")


class WebSite(HttpUser):
    # task_set = TestDemo  # 声明任务集的类就是上面那个类  task_set在1.0后被弃用
    tasks = [TestLogin]
    # min_wait = 1000  # 最小请求时间1s
    # max_wait = 2000  # 最大请求时间2s
    wait_time = between(3, 7)  # locust版本0.13之后已经废除了min_wait和max_wait的使用


if __name__ == '__main__':
    os.system("locust -f testLogin.py --host=http://182.43.224.122:45680")