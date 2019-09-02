#coding=gbk
from uiautomator import device as d
from uiautomator import Device
import time
d = Device('A1CEBNA227ZK')
def screnn_on(d):
    if d.screen == "on":
        pass
    else:
        d.screen.on()
if __name__ == '__main__':
    # screnn_on(d)
    # d.click(943, 1798)
    # d.long_click(48, 1262)
    # for i in range(3):
    #     timepp=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    #     print(timepp)
    #     d.drag(100 ,1000, 100, 10,steps=100)
    #     d.screenshot("%s.png"%timepp)
    # d.open.notification()
    # d.open.quick_settings()
    d.watcher("菜单").when(text="菜单").click(text="菜单")
    d.press("back")
    # d.watchers.run()
    if d(text='Force Close').exists:
        d(text='Force Close').click()
    # or get the dumped content(unicode) from return.