# -*- coding:utf8 -*-
"""
关键字封装（selenium二次封装）
达到跟RF一样的效果（main函数中调用时）
即开源自动化测试框架
"""
from selenium import webdriver
from time import sleep

class TestKeywords(object):

    #初始化
    def __init__(self, url, browsertype):
        self.driver = self.open_browser(browsertype)
        self.driver.get(url)

    #调用浏览器
    def open_browser(self, browsertype):
        if browsertype == 'chrome':
            driver = webdriver.Chrome()
            return driver
        elif browsertype == 'firefox':
            driver = webdriver.Firefox()
            return driver
        else:
            print 'type error.'

    #元素定位
    def locator(self,locator_type,value):
        if locator_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
            return el
        elif locator_type == 'id':
            el = self.driver.find_element_by_id(value)
            return el
        elif locator_type == 'name':
            el = self.driver.find_element_by_name(value)
            return el

    #元素定位简便方法
    # def locator1(self,*value):
    #     return self.driver.find_element(value)

    #输入
    def input_text(self,locator_type, value, text):
        self.locator(locator_type, value).send_keys(text)

    #点击
    def click_element(self,locator_type, value):
        self.locator(locator_type, value).click()

    #关闭浏览器
    def close_browser(self):
        sleep(2)
        self.driver.close()

if __name__ == '__main__':
    tk = TestKeywords('http://www.baidu.com','chrome')
    tk.input_text('id','kw','test的'.decode('utf-8')) #中文问题好像只能这么解决
    tk.click_element('id','su')
    tk.close_browser()