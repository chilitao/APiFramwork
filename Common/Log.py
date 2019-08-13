# -*- coding:utf-8 -*-
import logging
'''Log装饰器，可以修饰函数，具体格式为：函数前面+@log_funcname'''
def log_funcname(func):
        def wrapper(*s):
            log=Logger()
            log.info("开始执行函数: %s" % func.__name__)
            func()
            log.info("结束执行函数: %s" % func.__name__)
        return wrapper
"""本期未做文件型日志，具体日志可以保存到每个HTML报告中，只有控制台型日志，具体类型如下"""
class Logger(logging.Logger):
    def __init__(self,fn=None):
        super(Logger, self).__init__(self)
        ch = logging.StreamHandler() 
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s] : %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[process:%(process)s] - %(message)s')  
        ch.setFormatter(formatter)
        self.addHandler(ch)
if __name__ == "__main__":
    Logger().info('简单的测试一下日志接口')