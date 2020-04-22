#coding:utf8
"""
PO模式结合unittest
ps:po模式完全基于关键字驱动
"""
import unittest
from selenium import webdriver
from webui.POMode.pageObject.search_page import SarchPage
from time import sleep
from ddt import ddt, data, unpack

@ddt
class TestCases(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        self.sp = SarchPage(driver)

    def tearDown(self):
        self.sp.quit_browser()

    @data(['http://www.baidu.com', '测试1'],['http://www.baidu.com', '测试2'])
    @unpack
    def test_1(self, url, input_text):
        self.sp.check(url, input_text)
        sleep(3)
        self.assertEqual(self.sp.get_title(), '百度一下'.decode('utf-8'), msg='百度一下'.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()