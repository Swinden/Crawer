# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/17 2:51
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://cn.bing.com/?mkt=zh-CN')  # get����

driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys('��������')
driver.find_element_by_id('sb_form_q').submit()  # �ύ
time.sleep(2)
# �����������
driver.find_element_by_id('sb_form_q').clear()
driver.find_element_by_id('sb_form_q').send_keys('python')

time.sleep(2)
# ��λԪ�ز���ִ�в���
driver.find_element_by_id('sb_form_q').submit()
