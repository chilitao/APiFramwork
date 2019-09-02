# coding: utf-8
import unittest
from AApp.UI.Base import Browser
from AApp.UI.readconfig import configread as cf
class TestCloudMusic(Browser):
    def test_app_logout(self):
        self.d.app_start(self.package)
        if self.d(text=cf("Menu", "menu_text")).exists:
            self.log.info("在浏览器首页中，可以进行退出浏览器操作")
            self.d.press("back")  # 返回到上一级
            # os.system("adb shell input keyevent 4")
            if self.d(text="确定").exists:
                self.d(text="确定").click()
                self.log.info("退出浏览器成功")
            else:
                self.log.error("退出浏览器失败")
        else:
            self.d.app_start()
            raise AssertionError("浏览器退出测试用例失败")

    def test_clear_cache(self):
        self.d.app_clear(self.package)
        self.log.info("清除浏览器缓存")

    """进入到首页"""

    def test_mainpage(self):
        if self.d(text="阅读").exists:
            self.log.info("当前处于首页")
            self.d.screenshot("mainpage.png")
        elif self.d(text="首页").exists:
            self.log.info("当前处于阅读")
            self.d(text="首页").click()
            if self.d(text="阅读").exists:
                self.log.info("切换到首页成功")

    """进入到阅读页面"""

    def test_readpage(self):
        if self.d(text="首页").exists:
            self.log.info("当前处于阅读")
            self.d.screenshot("mainpage.png")
        elif self.d(text="阅读").exists:
            self.log.info("当前处于首页")
            self.d(text="阅读").click()
            if self.d(text="首页").exists:
                self.log.info("切换到阅读页面成功")
        else:
            self.log.error("启动App进入到了未知的错误页面，请查看日志和截图")
            self.d.screenshot("test_mainpage.png")

    def test_search(self):
        if self.d(resourceId=self.search_input_id).exists:
            self.log.info("出现放大镜按钮，可以进行搜索测试")
            self.d(resourceId=self.search_input_id).click()
            self.d.send_keys("百度", clear=True)
            self.d(resourceId="com.quqi.browser:id/adn").click()
            assert (self.d(text="百度 - Google 搜索")).exists

        else:
            self.log.error("放大镜按钮没有找到出错了，不能搜索啦")

    def test_stop_app(self):
        self.d.app_stop(self.package)

    if __name__ == '__main__':
        M