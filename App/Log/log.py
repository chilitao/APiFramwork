import os
import time
import subprocess

def catchLogcat():
    path=os.path.dirname(__file__)
    Time = time.strftime('%m%d%H%M')
    subprocess.Popen("adb logcat *.E >%s\%s.log" % (path,Time),shell=True)
if __name__=="__main__":
    catchLogcat()