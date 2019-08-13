# -*- coding:utf-8 -*-
__author__ = '池立涛'
import os,time,smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Common import Constant as Ct
'''邮件模块'''
class Email():
    def Sendemail(self):
        try:
            reportpath = os.path.join(Ct.Basedir, 'Report')
            lists = os.listdir(reportpath)
            lists.sort(key=lambda x: os.path.getatime(reportpath + '\\' + x))
            file = os.path.join(reportpath, lists[-1])

            msg = MIMEMultipart()
            msg['Subject'] = 'Tog接口自动化测试'  #
            msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

            with open(file, 'rb') as f:
                mailbody = f.read()
                html = MIMEText(mailbody, _subtype='html', _charset='utf-8')  # 将测试报告的内容放在 邮件的正文当中
                msg.attach(html)  # 将html附加在msg里

        # html附件    下面是将测试报告放在附件中发送
            att1 = MIMEText(mailbody, 'base64', 'gb2312')
            att1["Content-Type"] = 'application/octet-stream'
            att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'  # 这里的filename可以任意写，写什么名字，附件的名字就是什么
            msg.attach(att1)

        ######################################################################################################
            server=smtplib.SMTP_SSL("smtp.qq.com", 465)
            server.login(Ct.mail_sender,Ct.mail_password)
            server.sendmail(Ct.mail_sender, Ct.mail_receiver, msg.as_string())
            server.close()
            print('发送邮件成功')
        except Exception as e:
            print ('Exception: 发送邮件失败', e)
if __name__ == "__main__":
    email=Email()
    email.Sendemail()