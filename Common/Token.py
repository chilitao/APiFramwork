# -*- coding:utf-8 -*-
__author__ = '池立涛'
# -*- coding:utf-8 -*-
import requests
from Common.Config import config
from Common import Constant as Ct
global actualCode
"""获取登录时的token信息，需要账号和密码，post方法"""
def getToken(ProjectArea='HD'):
    T_url = config(ProjectArea, 'T_url').configFactory()
    T_data= eval(config(ProjectArea, 'T_data').configFactory())
    r = requests.post(T_url, data=T_data)
    b=eval(r.text)
    print(b)
    ssionid = b["value"]["sessionId"]
    headers = {'content-type': 'application/json','session-Id':"9ecafe34292a87b6c0f3296693b602e9"}
    headers['session-Id']=ssionid
    Ct.CASE_HEADERS=headers
    Ct.SSionid=ssionid
    print(ssionid)
if __name__=='__main__':
    getToken()