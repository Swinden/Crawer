# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/17 17:13
"""
from selenium import webdriver
import time
# ���� Keys ģ��
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'D:\360��ȫ���������\chromedriver.exe')
driver.get("https://cn.bing.com/?mkt=zh-CN")
time.sleep(3)
# ��������
driver.find_element_by_id('sb_form_q').send_keys('��������')
time.sleep(3)
# ����һ�Σ�ɾ�����һ����
driver.find_element_by_id('sb_form_q').send_keys(Keys.BACK_SPACE)
time.sleep(3)
# ����һ���ո��������µ�����python
driver.find_element_by_id('sb_form_q').send_keys(Keys.SPACE)
driver.find_element_by_id('sb_form_q').send_keys('python')
time.sleep(3)
# ctrl+a ȫѡ���������
driver.find_element_by_id("sb_form_q").send_keys(Keys.CONTROL, 'a')
time.sleep(3)
# ȫѡ����ctrl+c����
driver.find_element_by_id('sb_form_q').send_keys(Keys.CONTROL, 'c')
time.sleep(3)
# ���ƺú��Ȱ�����ɾ��
driver.find_element_by_id('sb_form_q').send_keys(Keys.BACK_SPACE)
time.sleep(3)
# ɾ���ú���ճ������
driver.find_element_by_id('sb_form_q').send_keys(Keys.CONTROL, 'v')
time.sleep(3)

driver.quit()  # �ر������
