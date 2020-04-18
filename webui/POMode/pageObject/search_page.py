#coding:utf8

from selenium import webdriver
from webui.POMode.basePage.base_page import BasePage
from selenium.webdriver.common.by import By

class SarchPage(BasePage):
    input_id = (By.ID, 'kw') #搜索框元素 以元组的形式准备好
    click_id = (By.ID, 'su') #百度一下按钮 以元组的形式准备好

    #对搜索框进行内容输入
    def input_text(self, input_text):
        self.locator(self.input_id).send_keys(input_text.decode('utf-8'))

    #点击查询按钮，实现本次搜索
    def click_element(self):
        self.locator(self.click_id).click()

    #
    def check(self, url, input_text):
        self.visit(url)
        self.input_text(input_text)
        self.click_element()

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    driver = webdriver.Chrome()
    sp = SarchPage(driver)
    sp.check(url,'测试2')
    sp.quit_browser()