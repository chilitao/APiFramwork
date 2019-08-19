import os
import time
import uiautomator2 as u2
d = u2.connect("172.21.53.134")
def clearche():
    os.system("adb shell pm clear com.quqi.browser")
    time.sleep(2)
    os.system("adb shell am start com.quqi.browser/com.enjoy.browser.BCBrowserActivity")
if __name__=="__main__":
    clearche()