# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/17 0:31
"""
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
import time

driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.find_element_by_id('sb_form_q').send_keys('��������')

# click����¼�
b = driver.find_element_by_class_name('search')
ActionChains(driver).click(b).perform()

c = driver.find_element_by_xpath('//*[@id="b_results"]/li[1]/div[1]/h2/a').click()

driver.refresh()  # ˢ��ҳ��

time.sleep(5)  # ǿ����Ϣ����

driver.quit()  # �ر������
