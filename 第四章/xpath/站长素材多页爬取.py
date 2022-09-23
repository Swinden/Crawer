# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/15 17:20
"""
import urllib.parse
import urllib.request
from lxml import etree
import time
import os


def qingqiu(url, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    }
    if page == 1:
        url = url.format('')  # ��д��
    else:
        url = url.format('_' + str(page))  # ��д�»��߼�ҳ��

    request = urllib.request.Request(url=url, headers=headers)
    return request


def download(image_src):
    dirpath = 'photo'
    # ����һ���ļ���
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    # �����ļ���
    filename = os.path.basename(image_src)
    # ͼƬ·��
    filepath = os.path.join(dirpath, filename)
    # �������󣬱���ͼƬ
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    }
    request = urllib.request.Request(url=image_src, headers=headers)
    response = urllib.request.urlopen(request)
    with open(filepath, 'wb') as fp:
        fp.write(response.read())


def jiexi(content):
    # ���ɶ���
    tree = etree.HTML(content)
    image_list = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    # �����б���������ͼƬ
    for image_src in image_list:
        image_src = 'http:' + image_src
        download(image_src)


if __name__ == "__main__":
    url = 'http://sc.chinaz.com/tupian/gudianmeinvtupian{}.html'

    start_page = int(input("�����뿪ʼҳ�룺"))
    end_page = int(input("���������ҳ�룺"))

    for page in range(start_page, end_page + 1):
        print("��%sҳ��ʼ���ء�����������" % page)
        request = qingqiu(url, page)
        content = urllib.request.urlopen(request).read().decode()
        # ��������
        jiexi(content)
        time.sleep(5)  # ���ⱻ������������̫��
        print("��%sҳ������ϡ�����������" % page)
    print("������ɣ�")
