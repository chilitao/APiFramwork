#encoding=utf-8
import os
def countLine(fname):
    count = 0
    single_quotes_flag = False
    double_quotes_flag = False
    with open(fname, 'rb') as f:
        for file_line in f:
            file_line = file_line.strip()
            # print(file_line)
            # 空行
            if file_line == b'':
                pass

            # 注释 # 开头
            elif file_line.startswith(b'#'):
                pass

            # 注释 单引号 ''' 开头
            elif file_line.startswith(b"'''") and not single_quotes_flag:
                single_quotes_flag = True
            # 注释 中间 和 ''' 结尾
            elif single_quotes_flag == True:
                if file_line.endswith(b"'''"):
                    single_quotes_flag = False

            # 注释 双引号 """ 开头
            elif file_line.startswith(b'"""') and not double_quotes_flag:
                double_quotes_flag = True
            # 注释 中间 和 """  结尾
            elif double_quotes_flag == True:
                if (file_line.endswith(b'"""')):
                    double_quotes_flag = False

            # 代码
            else:
                count += 1
        print(fname + '----', count)
        # 单个文件行数
        # print(fname,'----count:',count)
        return count
countLine("D:\Pyproject\PythonFile\Fileread\ltao.txt")