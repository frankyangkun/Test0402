# -*- coding:utf8 -*-
"""
必须在运行模式中用纯python运行，才能生成allure报告
用unittest和pytest模式运行都不能生成allure报告。
"""
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

@allure.feature('Locman登录')  # 用feature说明产品需求，可以理解为JIRA中的Epic
@ddt
class TestDemo3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://140.246.137.19:45680/#/login")

    def tearDown(self):
        self.driver.quit()

    @allure.story('登录')  # 用story说明用户场景，可以理解为JIRA中的Story
    @data(*list1)  # getdata()返回的是list，里面的值是dict的kv值
    @unpack
    def test1(self, **dict):  # 解包后得到的是dict类型的kv值
        '''这里是登录操作'''
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

    @pytest.mark.skipif(reason='本次不执行')
    def test2(self):
        print ("test2...")


if __name__ == "__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir', './temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./temp -o ./report --clean')
