#coding:utf8
"""
PO模式实现
ps：po模式完全基于关键字驱动
"""
from selenium import webdriver
from time import sleep

class BasePage(object):

    #构造函数
    def __init__(self, driver):
        self.driver = driver

    #元素定位
    def locator(self, locator):
        return self.driver.find_element(*locator) #不要用成find_element_by_id了

    #访问
    def visit(self, url):
        self.driver.get(url)

    #关闭
    def quit_browser(self):
        sleep(2)
        self.driver.quit()

    def get_title(self):
        return self.driver.title