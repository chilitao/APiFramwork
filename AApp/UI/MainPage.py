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
                self.log.info("������������ҳ�У����Խ����˳��������Ų���")
                os.system("adb shell input keyevent 4  ")
                if self.d(text="ȷ��").exists:
                    self.d(text="��������¼").click()
                    self.d(text="��������").click()
                    self.d(text="ȷ��").click()
                    if self.d(text="��������").exists:
                        self.log.info("�˳��������Ų��������ɹ�")
                        App().appclear()
                    else:
                        self.log.error("�˳��������Ų��������ɹ�")

            else:
                self.log.error("û�н��뵽��ҳ��ʧ��")
                Browser.takeshot(self)
        except Exception as e:
            print(e)






if __name__ == '__main__':
    for i in range(5):
        print("��%s����"%i)
        App().appclear()
        MainRead().test_logout()