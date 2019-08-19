apkpath=r"C:\Users\clt\Downloads"

import subprocess,os

import time

# def uninstall(p="cn"):
#     os.system("adb uninstall com.quqi.browser")
# def install():apkpath
#     apkpath = r"C:\Users\clt\Downloads" #
#     d=[]
#     f=[]
#     for i,j,k in os.walk(apkpath):
#         # print(k)
#         for i in k:
#             if os.path.splitext(i)[1]==".apk":
#                 d.append(i)
#                 f.append(os.path.splitext(i)[0][-15:])
#                 f.sort(key=lambda x: int(''.join(x.split('-'))))
#                 cc = (f[::-1][0])
#         for ii in d:
#             if os.path.splitext(ii)[0][-15:]==cc:
#                 ii=apkpath+"\\"+ii
#                 print("要安装的apk是%s"%ii)
#                 res=subprocess.Popen("adb install -r %s"%ii,shell=True, stdout=subprocess.PIPE)
#                 print(res.stdout.read())
#                 print(type(res.stdout.read()))# 打印结果
#
# path = u"D:\VPN\代码\数据仓库存储过程修改备份"
for root, dir, files in os.walk(apkpath):
    d = []
    for file in files:
        full_path = os.path.join(root, file)

        mtime = os.stat(full_path).st_mtime

        file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        d.append(file_modify_time)
        print("{0} 修改时间是: {1}".format(full_path,file_modify_time))

print(d)
# if __name__=="__main__":
#     # install()
#     uninstall()