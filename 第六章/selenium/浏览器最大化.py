# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/17 0:11
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.find_element_by_id('sb_form_q').send_keys('��������')
