# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/17 23:56
"""
from selenium import webdriver

options = webdriver.ChromeOptions()
# �������ͷ
options.add_argument(
    'User-Agent="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36"')
options.add_argument(f"--proxy-server=http://127.0.0.1:7890")  # ��Ӵ���
options.add_argument('--headless')   # ��ͷģʽ
options.add_argument('--incognito') # ʹ���޺�ģʽ
options.add_argument('--disable-javascript')  # ����javascript
options.add_argument('blink-settings=imagesEnabled=false') # ���������ͼƬ, ��վ���ؿ�һЩ
prefs = {"":""}
prefs["credentials_enable_service"] = False
prefs["profile.password_manager_enabled"] = False
options.add_experimental_option("prefs", prefs)  # ����'��������'��ʾ��

driver = webdriver.Chrome(r'D:\360��ȫ���������\chromedriver.exe', options=options)  # ����ʱ��������
driver.get('https://cn.bing.com/?mkt=zh-CN')

driver.find_element_by_id('sb_form_q').send_keys('��������')