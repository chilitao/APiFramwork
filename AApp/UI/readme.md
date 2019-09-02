1、python -m uiautomator2 init
2、d.open_notification（）
3、d.open_quick_settings（）
4、d(text="Settings").wait(timeout=3.0) # return bool
# 一直等到UI对象消失
d(text="Settings").wait_gone(timeout=1.0)
blog:https://blog.csdn.net/ricky_yangrui/article/details/81415365