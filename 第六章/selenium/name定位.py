# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/15 22:11
"""
from selenium import webdriver

driver = webdriver.Chrome(r'D:\360��ȫ���������\chromedriver.exe')

driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.find_element_by_id('sb_form_q').send_keys('��������')


