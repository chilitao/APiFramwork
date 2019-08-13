# -*- coding:utf-8 -*-
import os
CASE_NUMBER = 0  # 用例编号
CASE_NAME = 1    # 用例名称
CASE_DATA = 2    # 用例参数
CASE_URL = 3     # 用例接口地址
CASE_METHOD = 4  # 用例请求类型
CASE_CODE = 5    # 用例code
CASE_HEADERS =6
CASE_MODULE=7
CASE_ASSTION=8
CASE_Result=9
SSionid=None
All=0  #全量测试开关
mail_on_off = 'on'
mail_subject = '浏览器接口自动化测试报告'
mail_content = '测试报告结果已经发送到相关人邮件中，请查阅!'
mail_host = 'smtp.qq.com'
mail_port = 465
mail_password ="ibfcrvbmayrxbbfa"
mail_sender = '853826784@qq.com'
mail_receiver = ['18103369176@163.com','chilitao@baice100.com','liuxingxing@baice100.com']
timeout=10
Basedir=os.path.abspath(os.path.join(os.getcwd(), ".."))