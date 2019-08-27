# 互斥锁
import threading
# 创建锁对象
lock = threading.Lock()
num = 0

def run(n):
    global num
    for i in range(1000000):
        # 加锁  为了确保下面代码只能由一个线程从头到尾的执行
        # 会阻止多线程的并发执行，所以效率会大大降低
        """
        lock.acquire()
        try:
            num = num - n
            num = num + n
        finally:
            # 解锁
            lock.release()
        """
        with lock:
            num = num + n
            num = num - n

if __name__ == '__main__':
    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("num = %s"%(num))