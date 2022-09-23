# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/28 3:38
"""

import requests
from PIL import Image
# ���Ծ���
import logging

logging.captureWarnings(True)

# ʶ������������֤��
url = 'https://so.gushiwen.org/RandCode.ashx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

# ��ԭʼͼƬ����
response = requests.get(url=url, headers=headers, verify=False)
with open('./test.png', 'wb') as fp:
    fp.write(response.content)  # content�Ƕ���������


# ��д�����Բ�ɫͼƬ���лҶȻ�����
def covertimage(path):
    img = Image.open(path)
    # �ҶȻ�
    img = img.convert('L')

    # ͼƬ������������ɣ�����
    data = img.load()
    # ͼƬ��͸�
    w, h = img.size

    # ���ںڰ�ͼƬ������ֵ��0 ����
    # ����ֵ255 ����
    for i in range(w):
        for j in range(h):
            # ȡ����ͼƬ�����е�����ֵ
            if data[i, j] > 135:
                data[i, j] = 255
            else:
                data[i, j] = 0
    img.save('clean.png')


covertimage('test.png')  # ִ�к���

