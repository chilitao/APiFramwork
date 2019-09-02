# -*- coding:utf-8 -*-
from Common.Run import *
import requests
from Common.Token import *
import unittest
from AApp.UI.Base import Browser
class App(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def test_app_start(self):
        self.d.app_start(self.package)
        self.pid = self.d.app_wait(self.package)
        self.log.info("浏览器的进程id是%s" % self.pid)
        # adb shell dumpsys activity | find "mFoc"
        # self.res=WebDriverWait(self.d,30).until(EC.presence_of_element_located(cf("Menu","menu_text")))
        self.res = self.d.wait_activity("com.enjoy.browser.BCBrowserActivity", 30)
        if self.pid and self.res:
            if self.d(text="阅读").exists:
                self.log.info("当前处于首页,App初始化成功啦")
            else:
                self.log.info("开始从阅读页面切换到首页")
                self.d(text="首页").click()
                if self.d(text="阅读").exists:
                    self.log.info("切换到首页成功")
        else:
            self.log.error("APP启动失败")
            self.d.screenshot("appstartfail.png")
