# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/17 21:01
"""
import json

from selenium import webdriver

driver = webdriver.Chrome(r'D:\360��ȫ���������\chromedriver.exe')

with open('cookie.txt', 'r', encoding='u8') as f:
    cookies = json.load(f)
driver.get("https://www.bilibili.com/")
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get("https://www.bilibili.com/")
driver.refresh()
