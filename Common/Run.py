# -*- coding:utf-8 -*-
__author__ = '池立涛'
from Common import phone
from Common.Config import config
import requests,xlrd,json
from Common.Log import Logger
workbook = None
def get_sheet(path, module):
    open_excel(path)
    return get_sheet_bysheetname(module)
def open_excel(path):
    global workbook
    if (workbook == None):
        workbook = xlrd.open_workbook(path, on_demand=True)
def get_sheet_bysheetname(sheetName):
    global workbook
    return workbook.sheet_by_name(sheetName)
def get_content(sheet, row, col):
    return sheet.cell(row, col).value
def release(path):
    global workbook
    workbook.release_resources()
    del workbook
    workbook=None

"""项目区域，默认域名，具体测试参数位置，测试具体模块"""
def api(method, url, data=None ,headers={"Content-Type":"application/json"}):
    global results
    global respond
    try:
        if method == ("post"or"POST"):
            results = requests.post(url, data, headers=headers)
            return results.json()
        if method == ("get" or "GET"):
            results = requests.get(url, data, headers=headers)
            return results.json()
        if method == "put" or "PUT":
            results = requests.put(url, data, headers=headers)
            # print(results.json())
            return results.json()
        if method == "delete":
            results = requests.delete(url, headers=headers)
            return results.json()
    except BaseException as e:
        Logger().error(e,exc_info=1)
    # finally:
    #     pass
def runner(Casenumber,Region):
    excel_path=config(Region,'CasePath').configFactory()
    baseurl=config(Region,'url').configFactory()
    module=config(Region,'module').configFactory()
    sheet = get_sheet(excel_path,module)
    caselist = []
    testNumber = int(get_content(sheet, Casenumber, 0))
    testName = get_content(sheet, Casenumber, 1)
    testData = get_content(sheet, Casenumber, 2)
    testUrl = get_content(sheet, Casenumber, 3)
    realUrl=baseurl+testUrl
    testMethod=get_content(sheet, Casenumber, 4)
    try:
        result=api(testMethod,realUrl,testData)
        return result
    except Exception as e:
        print(e)
if __name__=='__main__':
    mobile=phone.create_phone()
    baseurl='http://10.110.60.88:8216'
    appVersionId=1630395645634797759
    headers={"Content-Type":"application/json"}
    url1='/member/appVersion/update'
    # url="http://10.110.60.88:8216/member/appVersion/create?versionName=初始版本3334&versionNo=34122&url=xxx&content=xxx&updateType=1&systemType=2&onlineTime=526894"
    # url="http://10.110.60.88:8216/member/appVersion/create?versionName={name}&versionNo={NO}&url=xxx&content=xxx&updateType=1&systemType=2&onlineTime=526894"
    # url.format(name="chilitao",NO=124678)
    url=baseurl+url1
    data1={
        "appVersionId": 1630395645634797759,
        "appVersionState": 1,
        "content": "mobile"
    }
    print(data1)
    headers={"Content-Type":"application/x-www-form-urlencoded"}
    dd=api("post",url="http://10.110.60.88:8216/member/appVersion/update?appVersionId=1630395645634797759&appVersionState=1&content=mobile",data=data1,headers=headers)
    print(dd)
