# -*- coding:utf8 -*-
"""
2020-09-30 11:38:33
测试只能用二维码登录的情况，比如企业微信
"""
from selenium import webdriver
import time
import json


class TestQRCodeLogin():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        time.sleep(5)

    def test_get_cookies(self):
        cookies = self.driver.get_cookies()
        # print("***Cookies***  ",cookies)

        with open("cookies.json", "w") as f:  # 将cookies持久化，保存在json文件
            json.dump(cookies, f)  # dump:将dict类型转换为json格式字符串，存入文件
        self.driver.close()

    def test_cookie_login(self):
        cookies = json.load(open("cookies.json"))  # load:将json格式字符串转化为dict，读取文件
        # print("***Cookies***  ", cookies)
        # print("@@@", type(cookies))  # <class 'list'>
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(5)
        self.driver.refresh()  # 刷新页面
        time.sleep(5)
