# coding:utf8

from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # as起别名
from selenium.webdriver.common.by import By
from login_page import LoginPage
from common import InitBrowser


class TestCases(unittest.TestCase, InitBrowser):
    def setUp(self):
        # self.driver = webdriver.Chrome()
        # self.driver.get('http://140.246.137.19:45680/#/login')
        # self.driver = InitBrowser() #实例化封装的类，也可直接继承该类，就无需实例化了
        InitBrowser.__init__(self)  # 继承后只需调用其初始化方法即可

    def tearDown(self):
        # self.driver.quit_browser()
        self.quit_browser()  # 继承后直接使用该类的方法，无需再用实例化出来的对象driver去调用了

    def test01(self):
        # 等待元素出现再后续操作，超时时间10s
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[1]/input')))
        # self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[1]/input').send_keys("chqadmin")
        #
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[2]/input'))) #重复操作，后续也需要优化
        # self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[2]/input').send_keys("111111")
        #
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[3]/button'))) #重复操作，后续也需要优化
        # self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[3]/button').click()

        """
        第一次优化：引入PO模式
        """
        # 由于传入的参数是元组，加上*（可变参数，会自动解析元组成2个参数）
        # self.driver.find_element(*LoginPage.username_input).send_keys('chqadmin')
        # self.driver.find_element(*LoginPage.pwd_input).send_keys('111111')
        # self.driver.find_element(*LoginPage.login_button).click()

        """
        第二次优化
        就不需要find_element去发现元素了，因为【等待元素出现】方法已经返回了该元素
        """
        # self.driver.sendkeys_until_visable(LoginPage.username_input, 'chqadmin')
        # self.driver.sendkeys_until_visable(LoginPage.pwd_input, '111111')
        # self.driver.click_until_visable(LoginPage.login_button)

        """
        第三次优化
        不再实例化InitBrowser类，直接继承它即可使用它的方法，无需再用实例化对象driver调用
        """
        self.sendkeys_until_visable(LoginPage.username_input, 'chqadmin')
        self.sendkeys_until_visable(LoginPage.pwd_input, '111111')
        self.click_until_visable(LoginPage.login_button)


if __name__ == '__main__':
    unittest.main()
