#coding=gbk
import os
from AApp.UI.Base import Browser
from AApp.UI.AppPage import App
from AApp.UI.readconfig import configread as cf
class MainRead(Browser):
    def test_logout(self):
        try:
            App().test_appstart()
            if self.d(text=cf("Menu", "menu_text")).exists:
                self.log.info("在奇料新闻首页中，可以进行退出奇料新闻操作")
                os.system("adb shell input keyevent 4  ")
                if self.d(text="确定").exists:
                    self.d(text="清除浏览记录").click()
                    self.d(text="不再提醒").click()
                    self.d(text="确定").click()
                    if self.d(text="奇料新闻").exists:
                        self.log.info("退出奇料新闻测试用例成功")
                        App().appclear()
                    else:
                        self.log.error("退出奇料新闻测试用例成功")

            else:
                self.log.error("没有进入到首页，失败")
                Browser.takeshot(self)
        except Exception as e:
            print(e)






if __name__ == '__main__':
    for i in range(5):
        print("第%s测试"%i)
        App().appclear()
        MainRead().test_logout()