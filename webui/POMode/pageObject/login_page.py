#coding:utf8
"""
PO模式结合unittest
ps:po模式完全基于关键字驱动
"""
from webui.POMode.basePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class LoginPage(BasePage):
    url = 'http://140.246.137.19:45680/#/login'
    login_name = (By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[1]/input')
    pwd = (By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[2]/input')
    login_button = (By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[3]/button')

    def input_username(self, username):
        self.locator(self.login_name).send_keys(username)

    def input_pwd(self, pwd):
        self.locator(self.pwd).send_keys(pwd)

    def login(self):
        self.locator(self.login_button).click()


    # #调试函数，测试函数，正式运行需要结合unittest来管理测试用例
    # def check(self, username, pwd):
    #     self.visit(self.url)
    #     sleep(10) #如果是测试locman，必须在这里等待10s，因为加载较慢
    #     self.input_username(username)
    #     self.input_pwd(pwd)
    #     self.login()
    #     self.quit_browser()

# if __name__ == '__main__':
#         driver = webdriver.Firefox()
#         name = 'chqadmin'
#         pwd = '111111'
#
#         lp = LoginPage(driver)
#         lp.check(name, pwd)
