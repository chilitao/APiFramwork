#coding=gbk
from AApp.UI.Base import Browser
import unittest
class App(Browser):
    def test_appstart(self):
        self.d.app_stop_all()
        self.d.app_start(self.package)
        Browser().dialo_diss()
        self.pid = self.d.app_wait(self.package)
        self.log.info("浏览器的进程id是%s" % self.pid)
        # adb shell dumpsys activity | find "mFoc"
        # self.res=WebDriverWait(self.d,30).until(EC.presence_of_element_located(cf("Menu","menu_text")))
        self.res = self.d.wait_activity("com.enjoy.browser.BCBrowserActivity", 30)
        if self.pid and self.res:
            if self.d(text="阅读").exists:
                self.log.info("当前处于首页,App初始化成功啦")
            elif self.d(text="阅读").exists:
                self.log.info("当前处于首页,App初始化成功啦")
            else:
                self.log.error("APP启动失败")
                self.d.screenshot("appstartfail.png")

        else:
            self.log.error("APP启动失败")
            self.d.screenshot("appstartfail.png")

    def test_appstop(self):
        self.d.app_stop(self.package)
        self.pid = self.d.app_wait(self.package)
        if not self.pid:
            self.log.info("趣奇App进程已经被销毁")
        else:
            self.log.info("趣奇App进程未被被销毁")
    def appclear(self):
        self.d.app_clear(self.package)
        # self.log.info("趣奇App缓存已经被成功删除")
if __name__ == '__main__':
    # App().test_appstart()
    # App().test_appstop()
    App().appclear()