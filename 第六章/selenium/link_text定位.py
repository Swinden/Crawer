# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/15 22:25
"""
# from selenium import webdriver  # ����ģ��
#
# browser = webdriver.Chrome()  # ��ʼ��
# browser.get('https://www.taobao.com')  # get�����Ա���ҳ
#
# href = browser.find_element_by_link_text('Ůװ')  # �ı���λŮװ
# print(href)

from selenium import webdriver  # ����ģ��

browser = webdriver.Chrome()  # ��ʼ��
browser.get('https://www.taobao.com')  # get�����Ա���ҳ

href = browser.find_element_by_link_text('��ʳ')  # �ı���λ��ʳ
print(href)