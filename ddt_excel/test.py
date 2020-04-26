# coding:utf8
"""
利用excel结合ddt实现数据驱动
2020-04-26
"""
from selenium import webdriver
from ddt import ddt, data, unpack
import unittest
from DDTReadExcel import ddtreadexcel
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # as起别名
from selenium.webdriver.common.by import By

list1 = ddtreadexcel().getdata()


@ddt
class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://140.246.137.19:45680/#/login")

    def tearDown(self):
        self.driver.quit()

    @data(*list1)  # getdata()返回的是list，里面的值是dict的kv值
    @unpack
    def test1(self, **dict):  # 解包后得到的是dict类型的kv值
        sleep(10)
        # self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[1]/input').send_keys(dict.get('username'))
        # self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[2]/input').send_keys(dict.get('password'))
        # self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[3]/button').click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[1]/input')))
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[1]/input').send_keys(dict.get('username'))

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[2]/input'))) #重复操作，后续也需要优化
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[2]/input').send_keys(dict.get('password'))

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[3]/button'))) #重复操作，后续也需要优化
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[3]/button').click()


        self.assertEqual(dict.get('username'), dict.get('password'))


if __name__ == '__main__':
    unittest.main()
