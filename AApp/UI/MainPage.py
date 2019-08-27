#coding=gbk
from AApp.UI.Base import Browser
import uiautomator2 as u2
import time
class MainPage(Browser):
    def __init__(self):
        super(Browser,self).__init__()
        self.d=u2.connect_usb("A1CEBNA227ZK")
        self.search_icon_id="com.quqi.browser:id/search_icon"
        self.search_box_id="com.quqi.browser:id/search_text_switcher"
        self.commit_search_id="com.quqi.browser:id/view_right"
    """mainpage"""
    def reaserch(self):
        self.d(resourceId="com.quqi.browser:id/search_text_switcher").click()
        self.d.send_keys("apple", clear=True)
        self.d(text=u"搜索").click()
if __name__ == '__main__':
   Browser().test_start_app()
   MainPage().reaserch()
