# -*- coding:utf8 -*-
"""
2020-06-02 14:27:45
locust参数化
使用csv文件存放帐号密码
使用queue并发保证测试数据唯一性（循环/不循环取值）（python的@parameterized.expand会循环重复取值）
还有关联（登录后的token传给注销接口）
注：有个问题，用jmeter测试注销接口，无论token写什么都是成功的：但如果是正确的token，确实能移出成功，刷新页面就踢出登录了，应该是接口的bug
但是用postman执行注销接口，就算是正确的token，也是提示token失效，和代码里执行一样（不过这不是此脚本的重点）

注2：
1、性能测试中，需要大量用户账号密码数据，用来验证随机登录，所以帐号密码这类数据需单独存到csv文件；
2、而单纯的接口自动化，存放在excel或json都可以，重点是存放各种场景的用例，而不只是帐号密码这类数据；
"""
from locust import HttpUser, TaskSet, task, between
from Locust.utils import correlationtools
import queue
import os


class TestRandomLoginQueue(TaskSet):
    token2 = ""

    # 这里不能用on_start，因为它只能执行一次，而这里需要每次都去取一次csv的数据
    def on_start(self):  # locust自带的初始化方法，类似于构造方法或setup，每个线程只调用一次
        #     try:
        #         self.userinfo = self.user.userdata.get()  # 获取唯一的用户信息
        #     except queue.Empty:
        #         print("数据已取完！")
        #         exit(0)
        #
        #     self.userinfo = self.userinfo.split(",")
        #     print("xxx-userinfo-xxx", self.userinfo)
        #
        #     # self.param = [
        #     #     ({"loginAccount": "pzadmin", "password": "96E79218965EB72C92A549DD5A330112", "userType": "individual"}),
        #     #     ({"loginAccount": "201808230@sefon.com", "password": "96E79218965EB72C92A549DD5A330112","userType": "individual"}),
        #     #     ({"loginAccount": "pzadmin", "password": "123", "userType": "individual"})
        #     # ]
        #
        #     self.param = {"loginAccount": self.userinfo[0], "password": self.userinfo[1], "userType": "individual"}
        print("--------on_start---------")

    @task(1)
    def doLogin(self):
        # self.locust代表的就是用户类LoadLogin，新版本用户类不再继承HttpLocust，换成了HttpUser，所以是self.user
        # userinfo = choice(self.user.userdata)  # userdata就是读取csv的一行结果 choice随机从集合取数据
        # userinfo = userinfo.split(",")  # 按逗号分别取值
        # print("userinfo:", userinfo)

        # randInt = randint(1, 1000) % len(self.param)  # 1000对用户数据3取余，结果0，1，2
        # res = self.client.post("/interGateway/v3/user/authentication", json=self.param[randInt], catch_response=True)
        # with self.client.post("/interGateway/v3/user/authentication", json=self.param[randInt], name="登录", catch_response=True) as response:  # 同上一行含义相同

        try:
            self.userinfo = self.user.userdata.get()  # 获取唯一的用户信息
        except queue.Empty:
            print("数据已取完！")
            exit(0)

        self.userinfo = self.userinfo.split(",")
        print("xxx-userinfo-xxx", self.userinfo, type(self.userinfo))  # ['pzadmin', '123'] <class 'list'>
        self.param = {"loginAccount": self.userinfo[0], "password": self.userinfo[1], "userType": "individual"}
        print("=====param=====", self.param, type(self.param))  # <class 'dict'>


        with self.client.post("/interGateway/v3/user/authentication", json=self.param, name="登录", catch_response=True) as response:
            # print(self.param[randInt]["loginAccount"])
            # self.token = correlationtools.fetchStringByBoundary(response.json())  # 获取服务器返回的token，给其他接口使用，这里返回的是json格式，无需自定义方法
            # print("***token***", self.token)
            print("***response.json()***", response.json(),  type(response))  #之前由于ip和端口写错返回了404，所以response.json()会报错

            self.token2 = response.json()["value"]["token"]
            print("***登录token2***", self.token2)
            # assert res.json()["resultStatus"]["resultMessage"] == "登录成功！"  # 这是python自带的断言，可用于接口自动化，locust是无法识别的
            # print("###resultMessage###",type(res.json()["resultStatus"]["resultMessage"]),res.json()["resultStatus"]["resultMessage"])

            # <class 'bytes'> Python3以后，字符串和bytes类型彻底分开了。字符串是以字符为单位进行处理的，bytes类型是以字节为单位处理的
            # print("&&&response.content&&&", type(response.content), response.content)  # 这里不用response.content

            response2 = response.json()["resultStatus"]["resultMessage"]
            print("%%%登录response2.msg%%%", response2)
            if response2 == "登录成功！":
                response.success()
            else:
                response.failure("登录失败！")

    @task(1)
    def doLogout(self):
        url = "/interGateway/v3/user/logout/" + self.token2
        print("url:-----",url)
        print("***注销token2***", self.token2)
        with self.client.delete(url, name="注销") as response:
        # with requests.delete(url) as response:  # 用原生requests也是token已失效，不知道为什么
            response2 = response.json()["resultStatus"]["resultMessage"]
            print("%%%注销response2.msg%%%", response2)
            if response2 == "token移除成功！":
                response.success()
            else:
                response.failure("注销失败！")


class LoadLogin(HttpUser):
    tasks = [TestRandomLoginQueue]
    wait_time = between(3, 7)
    host = "http://182.43.224.122:8002"  # 之前写成成华区项目的ip了，导致一直提示token失效，而且后面端口写错了，一直报404

    # 读取userdata.csv
    userdata = queue.Queue()
    with open("../../data/test_login/userdata.csv", "r") as file:
        for line in file.readlines():
            userdata.put_nowait(line.strip())  # strip去掉空格，put_nowait():无阻塞的向队列中添加任务，当队列为满时，不等待，而是直接抛出full异常


if __name__ == '__main__':
    os.system("locust -f testRandomLogin3-queue.py")  # 命令行执行老会提示找不到自定义的Locust.utils包，这么写不会报错
