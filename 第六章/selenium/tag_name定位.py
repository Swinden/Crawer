# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/15 22:33
"""
from selenium import webdriver  # ����ģ��

browser = webdriver.Chrome()  # ��ʼ��
browser.get('https://www.taobao.com')  # get�����Ա���ҳ

biao = browser.find_element_by_tag_name('input')
print(biao)
