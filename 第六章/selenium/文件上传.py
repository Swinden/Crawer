# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/17 20:06
"""
from selenium import webdriver
import os
import time
driver = webdriver.Chrome(r'D:\360��ȫ���������\chromedriver.exe')
file_path = 'file:///' + os.path.abspath('test.html')
driver.get(file_path)

# ��λ�ϴ���ť����ӱ����ļ�
driver.find_element_by_id("up_load").send_keys(r'C:\Users\hp\Pictures\test.jpg')

time.sleep(5)
driver.quit()