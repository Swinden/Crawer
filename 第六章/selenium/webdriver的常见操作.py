# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/17 1:30
"""
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

driver.get('https://www.taobao.com/')  # get����

driver.find_element_by_id('q').send_keys('��Ϊ�ֻ�')
time.sleep(3)
# driver.find_element_by_id('q').clear()
driver.find_element_by_class_name('btn-search').click()
time.sleep(2)
driver.find_element_by_name('fm-login-id').send_keys('15682448658')  # �����Ա��˺�
time.sleep(2)
driver.find_element_by_name('fm-login-password').send_keys('zxcvbnm123')  # �����Ա�����
time.sleep(2)

# try:
# �ҵ�����
hua = driver.find_element_by_id('nc_1_n1z')
# �жϻ����Ƿ�ɼ�
if hua.is_displayed():
    ActionChains(driver).click_and_hold(on_element=hua).perform()
    # ���ұ��ƶ�258��λ��
    ActionChains(driver).move_by_offset(xoffset=258, yoffset=0).perform()
    # �ɿ����
    ActionChains(driver).pause(0.5).release().perform()
else:
    print('������')
# except:
#     pass
