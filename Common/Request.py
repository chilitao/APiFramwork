# -*- coding:utf-8 -*-
import json
from Common import phone
__author__ = '池立涛'
import requests,json
from Common.Log import *
import Common.Constant as t
from Common.Token import *
from Common.Config import config
from Common import Excel as excel
from Common.Log import Logger
import json
'''封装了四大请求方法，json格式返回'''
def api(method, url, data=None ,headers=None):
    global results
    global respond
    try:
        if method == ("post"or"POST"):
            results = requests.post(url, data, headers=headers,timeout=t.timeout)
            print(results.json())
            return results.json()
        if method == ("get" or "GET"):
            results = requests.get(url, data, headers=headers,timeout=t.timeout)
            print(results.json())
            return results.json()
        if method == "put":
            results = requests.put(url, data, headers=headers)
            print(results.json())
            return results.json()
        if method == "delete":
            results = requests.delete(url, headers=headers,timeout=t.timeout)

            print(results.json())
            return results.json()
    except BaseException as e:
        Logger().error(e,exc_info=1)
    finally:
        pass
if __name__ == "__main__":
    url="/mpage/page/video_site_list?timestamp=1565936394447&code=CN&language=zh&versionCode=7&versionName=1.0.6.105&signCode=2ee777b7e0c0ca39c592b375d5bed179"
    baseurl='https://browser-test.antuzhi.com'
    # routee='/mpage/page/nav_list?code=CN'
    headers={"Content-Type":"application/json"}
    url=baseurl+url
    dd=api('get',url,data=None, headers=headers)

