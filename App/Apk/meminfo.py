import os,time
mem="adb shell "
def meminfo():
    # os.system("adb shell")
    # time.sleep(1)
    os.system("adb shell dumpsys meminfo com.quqi.browser ")
if __name__=="__main__":
    meminfo()