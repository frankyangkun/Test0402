#coding:utf8
"""
PO模式实现
ps:po模式完全基于关键字驱动
"""
from selenium import webdriver
from webui.POMode.basePage.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class SarchPage(BasePage):
    # input_id = (By.ID, 'kw') #搜索框元素 以元组的形式准备好
    # click_id = (By.ID, 'su') #百度一下按钮 以元组的形式准备好

    input_id = (By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[1]/input')
    click_id = (By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[2]/input')

    #对搜索框进行内容输入
    def input_text(self, input_text):
        self.locator(self.input_id).send_keys(input_text.decode('utf-8'))

    #点击查询按钮，实现本次搜索
    def click_element(self):
        self.locator(self.click_id).click()

    #
    def check(self, url, input_text):
        self.visit(url)
        time.sleep(10) #如果是测试locman，必须在这里等待10s，因为加载较慢
        self.input_text(input_text)
        self.click_element()

if __name__ == '__main__':
    url = 'http://140.246.137.19:45680/#/login'
    driver = webdriver.Chrome()
    sp = SarchPage(driver)
    sp.check(url,'测试2')
    sp.quit_browser()