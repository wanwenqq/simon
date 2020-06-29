'''
@Author: Anders
@Date: 2019-12-30 09:00:39
@LastEditTime : 2019-12-30 09:48:53
@LastEditors  : Anders
@FilePath: \phpd:\project\python\simon\sprocess.py
@Description: 
'''
import os
import multiprocessing
import time



class sPorcess(object):
    __pool = None
    
    def __init__(self):
        self.__pool = multiprocessing.Pool()

    def do_something(self,func,*args):
        self.__pool.apply_async(func,args=(*args,))

    def sclose(self):
        self.__pool.close()
        self.__pool.join()


def write(q):
        print("write启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid()))
        for i in "python":
                q.put(i)


def read(q):
        print("read启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid()))
        for i in range(q.qsize()):
                print("read从Queue获取到消息：%s" % q.get(True))    


if __name__ == "__main__":

    print("(%s) start" % os.getpid())
    # q = multiprocessing.Manager().Queue()
    # po = multiprocessing.Pool()
    # po.apply_async(write, args=(q,))

    # time.sleep(2)   

    # po.apply_async(read, args=(q,))
    # po.close()
    # po.join()

    q = multiprocessing.Manager().Queue()
    sp = sPorcess()
    sp.do_something(write(q))
    sp.do_something(read(q))
    # sp.sclose()
    time.sleep(5)
    sp.do_something(write(q))
    sp.do_something(read(q))
    print("(%s) end" % os.getpid())       
