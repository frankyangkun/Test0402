#encoding:utf8
"""
最基本的ui自动化demo
"""
from selenium import webdriver
from time import sleep

#生成一个ChromeDriver驱动对象driver
driver = webdriver.Chrome()

#指定访问路径并操作
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("test")
driver.find_element_by_id("su").click()
sleep(2)
#点击第一条链接
driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()