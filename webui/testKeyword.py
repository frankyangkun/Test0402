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
        # 运行时，disable-infobars参数可去掉浏览器的"Chrome正受自动测试软件的控制"提示条，但我的没起作用
        option = webdriver.ChromeOptions()
        option.add_argument('headless') #headless浏览器静默运行(在后台运行，不打开浏览器)

        if browsertype == 'chrome':
            driver = webdriver.Chrome(chrome_options=option)
            print "*************",driver.title #不知为啥没打印出「百度一下，你就知道」，可能是baidu做了限制

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
        self.driver.quit() #self.driver.close()也可以，close不会关闭chromedriver进程，只是关闭当前标签页

if __name__ == '__main__':
    tk = TestKeywords('http://www.baidu.com','chrome')
    tk.input_text('id','kw','test的'.decode('utf-8')) #中文问题好像只能这么解决
    tk.click_element('id','su')
    tk.close_browser()