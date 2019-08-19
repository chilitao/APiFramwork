import uiautomator2 as u2
import time
sn="A1CEBNA227ZK"
d = u2.connect("172.21.53.134")
print(d.info)

d.app_start("com.quqi.browser")
time.sleep(3)
# 搜索
d(resourceId="com.quqi.browser:id/u9").click()  #阅读

# 输入关键字
d(resourceId="com.quqi.browser:id/a1q").set_text("apple")

# 搜索按钮
d(resourceId="com.quqi.browser:id/ac9").click()

time.sleep(2)
d.press("back")
d.press("home") # press the home key, with key name

# 停止app
d.app_stop("com.quqi.browser")