# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/16 22:16
"""
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://cn.bing.com/?mkt=zh-CN')

# driver.find_element_by_css_selector('[name=q]').send_keys('��������')

driver.find_element_by_css_selector('.gLFyf').send_keys('��������')

# driver.find_element_by_css_selector('#tsf > div:nth-child(1) > div.A7Yvie.Epl37.emcav.Sl6fgd > div.zGVn2e > div.SDkEP > div > input')
