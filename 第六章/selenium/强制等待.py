# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/16 23:38
"""
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.find_element_by_id('sb_form_q').send_keys('��������')

time.sleep(2)

b = driver.find_element_by_class_name('search')
ActionChains(driver).click(b).perform()
