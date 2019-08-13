# -*- coding:utf-8 -*-
__author__ = '池立涛'
from Common.Excel import *

def asstion(a,s,m):
    Value=a
    ss = []
    for i in Value:
        for j in i.keys():
            if s in j:
                ss.append(i[s])
            else:
                pass
    if m in ss:
        return 1
    else:
        return 0
if __name__=='__main__':
    dd=[{'memberCarId': '1611559073866317825', 'carId': '1968641354808888832', 'memberId': '1611559002511876113', 'plateNumber': '冀A11111', 'memberCarState': 0, 'carType': 0, 'plateColor': 0, 'bindTime': '2018-09-15 11:48:23', 'authStatus': 1, 'mobile': '18103369176'}, {'memberCarId': '1612759940171829259', 'carId': '1976592641967802496', 'memberId': '1611559002511876113', 'plateNumber': '粤QQQQQQ', 'memberCarState': 0, 'carType': 0, 'plateColor': 0, 'bindTime': '2018-09-27 19:29:04', 'authStatus': 1, 'mobile': '18103369176'}, {'memberCarId': '1618890486705819658', 'carId': '1976619549701181440', 'memberId': '1611559002511876113', 'plateNumber': '粤W55555', 'memberCarState': 0, 'carType': 0, 'plateColor': 0, 'bindTime': '2018-12-04 11:31:57', 'authStatus': 1, 'mobile': '18103369176'}]
    cc=asstion(dd,'plateNumber','粤W55555')
    print(cc)
