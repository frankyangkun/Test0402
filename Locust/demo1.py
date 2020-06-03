# -*- coding:utf8 -*-
# 导入相关的locust的类，成员
from locust import HttpUser, TaskSet, task, between  # HttpLocust已经在1.0版本改为了HttpUser


# 任务类
class TestDemo(TaskSet):
    @task(1)
    def getDemo(self):
        self.client.get("/pengzhou/#/login")  # client是TaskSet类的成员，是一个http请求对象
        print("baidu...")


class WebSite(HttpUser):
    # task_set = TestDemo  # 声明任务集的类就是上面那个类  task_set在1.0后被弃用
    tasks = [TestDemo]
    # min_wait = 1000  # 最小请求时间1s
    # max_wait = 2000  # 最大请求时间2s
    wait_time = between(3, 7)  # locust版本0.13之后已经废除了min_wait和max_wait的使用
