# -*- coding:utf-8 -*-


import subprocess,time,sys,os,threading


# def getDevicesList():
    # return map(lambda x: x.split('\t')[0], os.popen('adb devices').readlines()[1:-1])
def runMonkey(logpath=r"C:\Users\clt\Desktop\12.txt"):
    os.system("adb shell monkey -v -v -v -s 8888 --throttle 300 --pct-touch 30 --pct-motion 25 --pct-appswitch 25 --pct-majornav 5 --pct-nav 0 --pct-trackball 0 -p com.quqi.browser 100>tao.txt")

def mult_run_Monkey(devicelist):
    threads = []
    for device in devicelist:
        threads.append(threading.Thread(target=runMonkey, args=(device,)))
    for t in threads:
        t.start()
        time.sleep(2)
    for t in threads:
        t.join()
    time.sleep(2)

def catchLogcat():
    path = os.path.join(os.path.dirname(__file__))
    Time = time.strftime('%Y%m%d%H%M%S')
    subprocess.Popen("adb logcat >%s\logcat_%s.txt" % (path,Time),shell=True)

# def mult_run_Logcat(devicelist):
    # threads = []
    # for device in devicelist:
        # threads.append(threading.Thread(target=catchLogcat, args=(device,)))
    # for t in threads:
        # t.start()
        # time.sleep(2)
    # for t in threads:
        # t.join()
    # time.sleep(2)

if __name__ =="__main__":
    # devicelist = getDevicesList()
    # print(devicelist)
    # mult_run_Logcat(devicelist)    #批量执行抓logcat
    runMonkey()    #批量执行跑monkey
    catchLogcat()  
    print("monkey测试已经结束了，请查看")    




