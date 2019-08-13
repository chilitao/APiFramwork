# -*- coding:utf-8 -*-
__author__ = '池立涛'
import unittest
from Common.Email import *
from Common import Constant as Ct
from Common.Report import  HTMLTestRunner
import time,os
if __name__ == '__main__':
    # 指定测试用例的位置
    test_module = os.path.join(Ct.Basedir, 'ApiTestCase')
    discover = unittest.defaultTestLoader.discover(test_module, pattern="*.py")
    # #存放报告位置
    dir_path=os.path.join(Ct.Basedir, 'Report\\')
    # #时间戳
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    report_path=dir_path +now +' result.html'
    #打开html,写入测试结果
    with open(report_path,'wb') as f:
        runner=HTMLTestRunner(stream=f,verbosity=2,title='TOG接口自动化测试报告',description='备注信息：所有Fail类型问题是接口问题，请联系开发人员排查；所有Error问题是框架问题，请联系测试组人员池立涛')
        runner.run(discover)
    f.close()
    if Ct.mail_on_off=='on':
        print('开始发送邮件')
        Email().Sendemail()
        print(Ct.CASE_HEADERS)
        print(Ct.SSionid)
    else:
        pass