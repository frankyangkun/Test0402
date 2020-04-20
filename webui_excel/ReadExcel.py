# -*- coding:utf8 -*-
"""
关键字驱动测试(Keyword driver testing)，结合excel
python操作excel主要用到xlrd和xlwt这两个库，即xlrd是读excel，xlwt是写excel的库。
"""
from selenium import webdriver
import unittest
import xlrd
import time

global driver


# 1、完成第一个action，打开浏览器：open_broswer
def open_broswer(browserName):
    global driver
    if browserName == "Chrome":
        driver = webdriver.Chrome()
    elif browserName == "firefox":
        driver = webdriver.Firefox()

# 2、打开指定url地址的方法：open_url
def open_url(url):
    global driver
    driver.get(url)

# 3、定一个识别元素并能返回元素的方法
def get_element(type1, type_value):
    global driver
    if type1 == "XPATH":
        element = driver.find_element_by_xpath(type_value)
    elif type1 == "ID":
        element = driver.find_element_by_id(type_value)
    return element

# 4、实现点击动作：click_button
def click_button(type1, type_value):
    ele = get_element(type1, type_value)
    ele.click()

# 5、实现输入数据动作：input_str
def input_str(type1, type_value, value1):
    ele = get_element(type1, type_value)
    ele.send_keys(value1)

# 6、实现时间等待动作：wait_time
def wait_time(value1):
    time.sleep(int(value1))

# 7、实现断言动作：assert_result
def assert_result(type1, type_value, value1):
    ele = get_element(type1, type_value)
    expectValue = ele.text
    if expectValue == value1:
        print("测试用例通过")
    else:
        print("测试用例不通过")

# 8、关闭浏览器：close_broswer
def close_browser():
    time.sleep(2)
    global driver
    driver.quit()

class kdtExcel(unittest.TestCase):
    def readExcel(self, filename):
        # 打开excel文件中的用例
        dataa = xlrd.open_workbook(filename)
        table = dataa.sheets()[0]
        for i in range(1, table.nrows):
            stepNo = table.row_values(i)[0]
            stepDes = table.row_values(i)[1]
            actionN = table.row_values(i)[2]
            type1 = table.row_values(i)[3]
            type_value = table.row_values(i)[4]
            value1 = table.row_values(i)[5]

            if actionN == "open_broswer":
                command = "%s('%s')" % (actionN, value1)
            elif actionN == "open_url":
                command = "%s('%s')" % (actionN, type_value)
            elif actionN == "click_button":
                command = "%s('%s','%s')" % (actionN, type1, type_value)
            elif actionN == "input_str":
                command = "%s('%s','%s','%s')" % (actionN, type1, type_value, value1)
            elif actionN == "wait_time":
                command = "%s('%s')" % (actionN, value1)
            elif actionN == "assert_result":
                command = "%s('%s','%s','%s')" % (actionN, type1, type_value, value1)
            elif actionN == "close_browser":
                command = "%s()" % (actionN)
                # print(command)
            eval(command)

    def test_cases(self):
        self.readExcel(r"./testcase.xlsx") #ps：可以利用unittest管理不同类型的测试用例，分别存放在不同的excel


if __name__ == '__main__':
    unittest.main()