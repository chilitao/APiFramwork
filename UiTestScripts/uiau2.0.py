import uiautomator2 as u2
from App.UI.LogFactory import Logger as Logger
import uiautomator2.ext.htmlreport as htmlreport
log=Logger().logger
import unittest
class Browser(unittest.TestCase):
    """"浏览器Ui自动化测试
        author:chilitao
        Version:1.0"""
    def __init__(self):
        self.d = u2.connect_usb('A1CEBNA227ZK')
        self.d.click_post_delay = 1.5
        Testreport = htmlreport.HTMLReport(self.d)
        Testreport.patch_click()

    # 连接测试
    def __call__(self):
        try:
            if self.d.info['naturalOrientation'] == True:
                log.debug('测试设备已经连接上')
        except Exception as e:
                log.error(e)

    def test_login_app(self):
        try:
            self.d.app_start("com.quqi.browser")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    unittest.main()

