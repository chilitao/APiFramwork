#coding=gbk
from appium import webdriver
import time

print("开始")
desired_caps = {}
desired_caps['platformName'] = 'Android'    #平台
desired_caps['platformVersion'] = '7.0'     #版本
desired_caps['deviceName'] = 'A1CEBNA227ZK'     #设备名字
desired_caps['appPackage'] = 'com.quqi.browser'      #需要打开的报名
desired_caps['appActivity'] = 'com.enjoy.browser.BCBrowserActivity'     #打开APP的第一个activity
#设置键盘
desired_caps['unicodeKeyboard']='True'
desired_caps['resetKeyboard']='True'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)    #打开APP
time.sleep(3)
driver.find_element_by_id("com.quqi.browser:id/vf").click()   #点击进入登录页
# driver.find_element_by_id("et_login_phone").send_keys("15172381949")   #登录页输入账号
# driver.find_element_by_id("et_login_pwd").send_keys("123456")   #登录页输入密码
# driver.find_element_by_id("com.ruixing.bbc:id/tv_login_commit").click()   #点击登录

time.sleep(2)

driver.quit()
