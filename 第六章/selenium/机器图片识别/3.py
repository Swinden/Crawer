# coding=gbk
"""
���ߣ�����
@ʱ��  : 2022/3/27 23:39
"""
import pytesseract
from PIL import Image
# ��ȡͼƬ
im = Image.open('clean.png')
# ʶ������
string = pytesseract.image_to_string(im)
print(string)