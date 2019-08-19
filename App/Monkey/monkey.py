import logging
import re
import time
import os
import subprocess
monkeycommond="adb shell CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process " \
"/system/bin tv.panda.test.monkey.Monkey -p com.quqi.browser --uiautomatormix --running-minutes 3 -v -v > .\monkey.log 2>.\err.txt"
pid="adb shell ps | grep com.tencent.mobileqq"
def getFocusedPackageAndActivity():
    pattern = re.compile(r"[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+")
    out = os.popen("adb shell dumpsys window windows | findstr \/ | findstr name=").read()
    list = pattern.findall(out)
    component = list[0]  # 输出列表中的第一条字符串
    print(component)
    return component
def monkey():
    print("开始清除手机logcat日志......")
    os.system("adb logcat -c")
    print("Monkey测试的开始时间是：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    os.system(monkeycommond)
    time.sleep(2)
    catchLogcat()
    print("日志抓取完成......")

def catchLogcat():
    path = os.path.dirname(__file__)
    Time = time.strftime('%m%d%H%M')
    subprocess.Popen("adb logcat *.E >%s\%s.log" % (path, Time), shell=True)
    print("Monkey测试的结束时间是："+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


if __name__=="__main__":

    getFocusedPackageAndActivity()