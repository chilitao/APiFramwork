# -*- coding:utf-8 -*-
import pymysql
from sshtunnel import SSHTunnelForwarder
__author__ = '池立涛'
import pymysql.cursors
from Common.Log import Logger as Lg

sqlconn = None
'''连接数据库并且准备相关的sql语句，不含有ssh跳转'''
def sqlconnect(host='localhost', port=3306,user='root',password='admin',dbname='test', charset='utf8',sql=None):
    global sqlconn
    if sqlconn == None:
        sqlconn = pymysql.connect(host=host,
                               port=port,
                               user=user,
                               password=password,
                               db=dbname,
                               charset=charset,
                               cursorclass=pymysql.cursors.DictCursor)
        # Lg().info('数据库打开完成...')
    try:
        with sqlconn.cursor() as cursor:
            res = cursor.execute(sql)
        sqlconn.commit()
        data = cursor.fetchall()
        # Lg().info('数据库关闭中...')
        sqlconn.close()
        return data
    except Exception as e:
        print(e)
'''连接数据库并且准备相关的sql语句，含有ssh跳转'''
def ssh_connect_and_read_db(sqlstr):
    with SSHTunnelForwarder(
            ('101.200.43.94', 22),  # 跳板机地址
            ssh_username="TEST",  # 跳板机账号
            ssh_password="95407b!e8@b6F23aGbda0d",  # 跳板机账户密码
            remote_bind_address=('rm-2zew5502alm949f64.mysql.rds.aliyuncs.com', 3306)) as server:  # MySQL服务器
        server.start()
        conn = pymysql.connect(host='127.0.0.1',            # 此处必须是必须是127.0.0.1
                               port=server.local_bind_port,
                               user='gengye',              # MySQL服务器账户
                               passwd='5a04b78d4581dd6dA',      # MySQL服务器密码
                               charset='utf8',
                               db='bj_pre_test01'      # 可以限定，只访问特定的数据库,否则需要在mysql的查询或者操作语句中，指定好表名
                               )
        # 打开数据库
        cursor = conn.cursor()
        cursor.execute(sqlstr)
        conn.commit()
        data = cursor.fetchall()
        data1=data[0][0]
        print(type(data1))
        print(data1)
        conn.close()
        return cursor

    
if __name__ == "__main__":
    sqlres=sqlconnect(host='10.110.60.228',port=3306,user='aiparkcity',password='123456',dbname='memberdb',sql='SELECT memberid FROM t_member ORDER BY createdTime DESC LIMIT 1')[0]['memberid']
    print(sqlres)
    print(type(sqlres))
