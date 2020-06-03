# -*- coding:utf8 -*-
"""
2020-06-02 14:27:45
locust参数化
使用csv文件存放帐号密码，读取csv文件数据，会重复读取
"""
from locust import HttpUser, TaskSet, task, between
from random import randint, choice


class TestRandomLogin(TaskSet):

    def on_start(self):  # locust自带的初始化方法，类似于构造方法或setup，每个线程只调用一次
        self.param = [
            ({"loginAccount": "pzadmin", "password": "96E79218965EB72C92A549DD5A330112", "userType": "individual"}),
            ({"loginAccount": "201808230@sefon.com", "password": "96E79218965EB72C92A549DD5A330112", "userType": "individual"}),
            ({"loginAccount": "pzadmin", "password": "123", "userType": "individual"})
        ]
        print("--------on_start---------")

    @task(1)
    def doLogin(self):
        # self.locust代表的就是用户类LoadLogin，新版本用户类不再继承HttpLocust，换成了HttpUser，所以是self.user
        userinfo = choice(self.user.userdata)  # userdata就是读取csv的一行结果 choice随机从集合取数据
        userinfo = userinfo.split(",")  # 按逗号分别取值
        print("userinfo:", userinfo)

        randInt = randint(1, 1000) % len(self.param)  # 1000对用户数据3取余，结果0，1，2
        # res = self.client.post("/interGateway/v3/user/authentication", json=self.param[randInt], catch_response=True)
        with self.client.post("/interGateway/v3/user/authentication", json=self.param[randInt], name="登录", catch_response=True) as response:  # 同上一行含义相同
            print("---userinfo---", self.param[randInt],type(self.param[randInt]))
            print("---loginAccount---",self.param[randInt]["loginAccount"])

            print("***response.json()***", response.json(),type(response))
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
    host = "http://182.43.224.122:8002"

    # 读取userdata.csv
    userdata = []
    with open("../../data/test_login/userdata.csv", "r") as file:
        for line in file.readlines():
            userdata.append(line.strip())  # strip去掉空格
