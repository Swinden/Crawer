# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/17 22:49
"""
from selenium import webdriver
import time

driver = webdriver.Chrome(r'D:\360��ȫ���������\chromedriver.exe')

driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.save_screenshot('ȫ����ͼ.png')  # ȫ����ͼ
time.sleep(2)
driver.find_element_by_id('sb_form_q').screenshot('Ԫ�ؽ�ͼ.png')  # Ԫ�ؽ�ͼ
time.sleep(2)

driver.quit()
