#coding=gbk
from AApp.UI.Base import Browser
import unittest
class App(Browser):
    def test_appstart(self):
        self.d.app_stop_all()
        self.d.app_start(self.package)
        Browser().dialo_diss()
        self.pid = self.d.app_wait(self.package)
        self.log.info("������Ľ���id��%s" % self.pid)
        # adb shell dumpsys activity | find "mFoc"
        # self.res=WebDriverWait(self.d,30).until(EC.presence_of_element_located(cf("Menu","menu_text")))
        self.res = self.d.wait_activity("com.enjoy.browser.BCBrowserActivity", 30)
        if self.pid and self.res:
            if self.d(text="�Ķ�").exists:
                self.log.info("��ǰ������ҳ,App��ʼ���ɹ���")
            elif self.d(text="�Ķ�").exists:
                self.log.info("��ǰ������ҳ,App��ʼ���ɹ���")
            else:
                self.log.error("APP����ʧ��")
                self.d.screenshot("appstartfail.png")

        else:
            self.log.error("APP����ʧ��")
            self.d.screenshot("appstartfail.png")

    def test_appstop(self):
        self.d.app_stop(self.package)
        self.pid = self.d.app_wait(self.package)
        if not self.pid:
            self.log.info("Ȥ��App�����Ѿ�������")
        else:
            self.log.info("Ȥ��App����δ��������")
    def appclear(self):
        self.d.app_clear(self.package)
        # self.log.info("Ȥ��App�����Ѿ����ɹ�ɾ��")
if __name__ == '__main__':
    # App().test_appstart()
    # App().test_appstop()
    App().appclear()