#coding=gbk
from appium import webdriver
import time

print("��ʼ")
desired_caps = {}
desired_caps['platformName'] = 'Android'    #ƽ̨
desired_caps['platformVersion'] = '7.0'     #�汾
desired_caps['deviceName'] = 'A1CEBNA227ZK'     #�豸����
desired_caps['appPackage'] = 'com.quqi.browser'      #��Ҫ�򿪵ı���
desired_caps['appActivity'] = 'com.enjoy.browser.BCBrowserActivity'     #��APP�ĵ�һ��activity
#���ü���
desired_caps['unicodeKeyboard']='True'
desired_caps['resetKeyboard']='True'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)    #��APP
time.sleep(3)
driver.find_element_by_id("com.quqi.browser:id/vf").click()   #��������¼ҳ
# driver.find_element_by_id("et_login_phone").send_keys("15172381949")   #��¼ҳ�����˺�
# driver.find_element_by_id("et_login_pwd").send_keys("123456")   #��¼ҳ��������
# driver.find_element_by_id("com.ruixing.bbc:id/tv_login_commit").click()   #�����¼

time.sleep(2)

driver.quit()
