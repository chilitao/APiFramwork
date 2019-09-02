#coding=gbk
import configparser

# secs = cf.sections()##列表格式返回
# print(secs)
# options = cf.options("MainPage")  # 获取某个section名为Mysql-Database所对应的键
# print(options)
# items = cf.items("MainPage")  # 获取section名为Mysql-Database所对应的全部键值对
# print(items)

def configread(section=None,Key=None):
    cf = configparser.ConfigParser()
    cf.read(r"D:\Pyproject\PythonFile\AApp\UI\element.ini")
    value= cf.get(section,Key)  # 获取[Mysql-Database]中host对应的值
    # print(value)
    return value
if __name__ == '__main__':
    configread("MP","search_input")