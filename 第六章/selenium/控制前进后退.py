# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/17 0:16
"""
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# driver = webdriver.Chrome()
#
# driver.get('https://cn.bing.com/?mkt=zh-CN')
#
# driver.find_element_by_id('sb_form_q').send_keys('��������')
#
# # click����¼�
# b = driver.find_element_by_class_name('search')
# ActionChains(driver).click(b).perform()
#
# c=driver.find_element_by_xpath('//*[@id="b_results"]/li[1]/div[1]/h2/a').click()

from selenium import webdriver
import time

driver = webdriver.Chrome()

# ����CSDN
first = 'https://www.csdn.net/'
print("���룺%s" % (first))
driver.get(first)
time.sleep(3)
# ����֪��
second = 'https://www.zhihu.com/'
print("����%s" % (second))
driver.get(second)
time.sleep(3)
# ���˵�CSDN
print("���ص���%s " % (first))
driver.back()
time.sleep(3)
# ǰ����֪��
driver.forward()
print('��ǰ������%s' % (second))

time.sleep(3)
driver.quit()
