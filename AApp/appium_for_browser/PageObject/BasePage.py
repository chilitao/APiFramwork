#encoding=utf-8
import time
import os
from appium import webdriver
from selenium import *
from selenium.webdriver.support.ui import WebDriverWait
class Base:
    driver=None
    capabilities={'platformName':"Android",
                  'platformVersion':'7.0',
                  'deviceName':'A1CEBNA227ZK',
                  'appPackage':'com.quqi.browser',
                  'appActivity':'com.enjoy.browser.BCBrowserActivity',
                  'unicodeKeyboard':True,
                  'resetKeyboard':True,}
    def __init__(self,driver):
        self.driver=driver
    def find_element(self,loc):
        try:
            WebDriverWait(self.driver,3000).until(lambda driver:driver.find_element)
            return self.driver.driver.find_elment(loc)
        except:
            print("%s元素在%s页面中未能找到"%(loc,self))
    # def wait_element_miss(self):
    #     try:
    #         # 在 60s 每隔 0.5s 检查是否 view 消失
    #         WebDriverWait(self, 60, 0.5, ElementNotVisibleException).until_not(
    #             lambda x: x.find_element_by_accessibility_id(view).is_displayed())
    #     except TimeoutException, e:
    #         print("time out message")
    #         raise e


