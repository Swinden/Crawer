# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/17 16:56
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(r'D:\360��ȫ���������\chromedriver.exe')

driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.find_element_by_id('sb_form_q').send_keys('��������')
time.sleep(2)
#��λ������ť
su = driver.find_element_by_class_name('search')
# ��λ����ִ��
ActionChains(driver).double_click(su).perform()
