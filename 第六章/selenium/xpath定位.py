# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/15 22:34
"""
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://cn.bing.com/?mkt=zh-CN')  # get����

driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys('��������')
# click����¼�
b = driver.find_element_by_class_name('search')
ActionChains(driver).click(b).perform()
