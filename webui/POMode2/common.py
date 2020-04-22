# coding:utf8
"""
封装常用方法
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # as起别名


class InitBrowser(object):
    """
    浏览器常用操作封装
    """
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://140.246.137.19:45680/#/login')

    def wait_element_visialbe(self, locate):
        """
        等待元素出现
        :return: 返回这个元素
        """
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locate))
        print "等待元素出现。。"
        return ele

    def click_until_visable(self, locate):
        """
        点击之前，自动调用等待方法
        :return:
        """
        self.wait_element_visialbe(locate).click()  # 因为返回了ele，所以直接click

    def sendkeys_until_visable(self, locate, value):
        """
        输入之前，自动调用等待方法
        :return:
        """
        self.wait_element_visialbe(locate).send_keys(value)  # 因为返回了ele，所以直接sendkeys

    def quit_browser(self):
        """
        退出浏览器
        :return:
        """
        self.driver.quit()