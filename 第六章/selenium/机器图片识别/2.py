# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/27 23:19
"""
import pytesseract
from PIL import Image
# ��ȡͼƬ
im = Image.open('img_1.png')
# ʶ�����֣���ָ������
string = pytesseract.image_to_string(im, lang='chi_sim')
print(string)