# coding=gbk
"""
���ߣ�����
@ʱ��  : 2021/11/10 10:50
Ⱥ��970353786
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# д����һ��ͨ�õĺ����ӿڣ���ֱ���õĻ����Ѳ�����ע��ȥ���ͺ�
def send_email(msg_from, passwd, msg_to, text_content, file_path=None):
    msg = MIMEMultipart()
    subject = "python ʵ�����䷢���ʼ�"  # ����
    text = MIMEText(text_content)
    msg.attach(text)


    if file_path:  # �ʼ�ĺ���������Ĭ��������None ������Ӹ��������и���һ�¾ͺ�
        docFile = file_path
        docApart = MIMEApplication(open(docFile, 'rb').read())
        docApart.add_header('Content-Disposition', 'attachment', filename=docFile)
        msg.attach(docApart)
        print('���͸�����')
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("���ͳɹ�")
    except smtplib.SMTPException as e:
        print("����ʧ��")
    finally:
        s.quit()


msg_from = '28....579@qq.com'  # ���ͷ�����
passwd = 'dw....igrodhda'  # ���뷢�ͷ��������Ȩ�루���Ǹո����õ����Ǹ���Ȩ�룩
msg_to = '28....9579@qq.com'  # �ռ������䣬�����Լ������Լ�
text_content = "����һ������!"  # ���͵��ʼ�����
file_path = 'log.text'  # ��Ҫ���͵ĸ���Ŀ¼
send_email(msg_from, passwd, msg_to, text_content, file_path)
