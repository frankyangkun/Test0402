# -*- coding:utf8 -*-

import pytest
import allure
import os
import unittest
from ddt import ddt, data, unpack
from ddt_excel.DDTReadExcel import ddtreadexcel
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # as起别名
from selenium.webdriver.common.by import By

list1 = ddtreadexcel().getdata()


@ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://140.246.137.19:45680/#/login")

    def tearDown(self):
        self.driver.quit()

    # @pytest.fixture(scope='function')
    # def login(self):
    #     print("登录")
    #     yield
    #     print("登录完成")
    #
    # # @allure.feature('加入购物车')
    # def test_1(login):
    #     '''将苹果加入购物车'''
    #     print("测试用例1")
    #
    # # @allure.feature('加入购物车')
    # def test_2(self):
    #     '''将橘子加入购物车'''
    #     print("测试用例2")

    @data(*list1)  # getdata()返回的是list，里面的值是dict的kv值
    @unpack
    def test1(self, **dict):  # 解包后得到的是dict类型的kv值

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[1]/input')))
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[1]/input').send_keys(dict.get('username'))

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[2]/input')))  # 重复操作，后续也需要优化
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[2]/input').send_keys(dict.get('password'))

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[3]/button')))  # 重复操作，后续也需要优化
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[3]/button').click()

        self.assertEqual(dict.get('username'), dict.get('password'))


if __name__ == "__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir', './temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./temp -o ./report --clean')
