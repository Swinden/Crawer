"""
���ߣ�����
@ʱ��  : 2022/3/15 15:54
"""
from lxml import etree
import requests
import urllib.request

url = 'http://sc.chinaz.com/tupian/xingganmeinvtupian.html'

response = requests.get(url=url)

response.encoding = 'utf-8'

# �������ԾͿ�����
html = response.text

html_etree = etree.HTML(html)

x = '//div[@class="box picblock col3"]/div/a/img/@src2'
src = html_etree.xpath(x)
# print(src)

i = 1
for img_url in src:
    name = str(i) + '.jpg'
    u = 'https:' + img_url
    # print(u)
    i = i + 1
    # print(name)
    urllib.request.urlretrieve(u, filename='./photo/%s' % (name))

    print('����ͼƬ%s�ɹ���' % (name))
