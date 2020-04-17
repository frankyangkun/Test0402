#coding:utf8
"""
UI自动化结合unittest
"""
import unittest

from webui.testKeyword import TestKeywords
from ddt import ddt,data,unpack

@ddt
class unittestforui(unittest.TestCase):
    def setUp(self):
        self.tk = TestKeywords('http://www.baidu.com', 'chrome')

    def tearDown(self):
        self.tk.close_browser()

    @data(['id', 'test1中'], ['id', 'test2'])
    @unpack
    def test_1(self, locatortype, value):
        self.tk.input_text(locatortype, 'kw', value.decode('utf-8'))  # 中文问题好像只能这么解决
        self.tk.click_element(locatortype, 'su')



if __name__ == '__main__':
        unittest.main()