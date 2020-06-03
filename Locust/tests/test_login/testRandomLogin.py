# -*- coding:utf8 -*-
"""
2020-05-28 17:49:38
locust参数化
使用locust自己的断言判断请求成功与否
2020-06-02 10:36:03
验证分布式压测（locust多进程模式）
"""
from locust import HttpUser, TaskSet, task, between
from random import randint

class TestRandomLogin(TaskSet):

    def on_start(self):  # locust自带的初始化方法，类似于构造方法或setup，每个线程只调用一次
        self.param = [
            ({"loginAccount": "pzadmin", "password": "96E79218965EB72C92A549DD5A330112", "userType": "individual"}),
            ({"loginAccount": "201808230@sefon.com", "password": "96E79218965EB72C92A549DD5A330112","userType": "individual"}),
            ({"loginAccount": "pzadmin", "password": "123", "userType": "individual"})
        ]
        print("--------on_start---------")
    @task(1)
    def doLogin(self):
        randInt = randint(1,1000) % len(self.param)  # 1000对用户数据3取余，结果0，1，2
        # res = self.client.post("/interGateway/v3/user/authentication", json=self.param[randInt], catch_response=True)
        with self.client.post("/interGateway/v3/user/authentication", json=self.param[randInt], catch_response=True) as response:  # 同上一行含义相同
        # print(self.param[randInt]["loginAccount"])
            print("***response.json()***",response.json())
        # assert res.json()["resultStatus"]["resultMessage"] == "登录成功！"  # 这是python自带的断言，可用于接口自动化，locust是无法识别的
        # print("###resultMessage###",type(res.json()["resultStatus"]["resultMessage"]),res.json()["resultStatus"]["resultMessage"])

            # <class 'bytes'> Python3以后，字符串和bytes类型彻底分开了。字符串是以字符为单位进行处理的，bytes类型是以字节为单位处理的
            # print("&&&response.content&&&", type(response.content), response.content)  # 这里不用response.content

            response2 = response.json()["resultStatus"]["resultMessage"]
            print("%%%response2.msg%%%", response2)
            if response2 == "登录成功！":
                response.success()
            else:
                response.failure("登录失败！")


class LoadLogin(HttpUser):
    tasks = [TestRandomLogin]
    wait_time = between(3, 7)



