#coding=gbk
import configparser

# secs = cf.sections()##�б��ʽ����
# print(secs)
# options = cf.options("MainPage")  # ��ȡĳ��section��ΪMysql-Database����Ӧ�ļ�
# print(options)
# items = cf.items("MainPage")  # ��ȡsection��ΪMysql-Database����Ӧ��ȫ����ֵ��
# print(items)

def configread(section=None,Key=None):
    cf = configparser.ConfigParser()
    cf.read(r"D:\Pyproject\PythonFile\AApp\UI\element.ini")
    value= cf.get(section,Key)  # ��ȡ[Mysql-Database]��host��Ӧ��ֵ
    # print(value)
    return value
if __name__ == '__main__':
    configread("MP","search_input")