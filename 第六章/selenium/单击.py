# coding=gbk
from selenium import webdriver
import time
# ���� ActionChains ��
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r'D:\360��ȫ���������\chromedriver.exe')
driver.get("https://cn.bing.com/?mkt=zh-CN")
driver.maximize_window()
time.sleep(3)
# ��λ��Ԫ��
su = driver.find_element_by_class_name('search')
# ��λ����ִ��
ActionChains(driver).context_click(su).perform()
