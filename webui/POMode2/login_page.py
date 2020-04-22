#coding:utf8
"""
管理页面所有的元素，操作这些元素的方法
"""
from selenium.webdriver.common.by import By

class LoginPage(object):
    #元组形式保存，方便find_element调用
    username_input = (By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[1]/input')
    pwd_input = (By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[2]/input')
    login_button = (By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[3]/button')


