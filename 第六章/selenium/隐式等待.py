# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/17 0:00
"""
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://cn.bing.com/?mkt=zh-CN')  # get����

driver.implicitly_wait(10)  # ��ʽ�ȴ�10��

driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys('��������')
