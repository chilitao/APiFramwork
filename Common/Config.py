# -*- coding:utf-8 -*-
__author__ = '池立涛'
import os,sys
import configparser
'''配置工厂类：读取同目录下的config.txt文件，类参数中传入section:模块 和 name 具体数据名称,使用configFactory方法，可以直接得到具体值'''
class config:
    global con_path
    def __init__(self,section,name):
        self.section=section
        self.name=name
    def configFactory(self):
        con_path=os.path.join(os.path.join(os.path.dirname("__file__"),os.path.pardir),'Config/config.txt')
        conf = configparser.ConfigParser()
        conf.read(con_path)
        return conf.get(self.section,self.name)
if __name__ == "__main__":
    conf=config('HD','filepath')
    excel=conf.configFactory()
    print(excel)