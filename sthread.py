'''
@Author: Anders
@Date: 2019-12-30 09:45:58
@LastEditTime : 2019-12-30 11:19:37
@LastEditors  : Anders
@FilePath: \phpd:\project\python\simon\sthread.py
@Description: 
'''
import time
from slogging import logger
from threading import Thread
from queue import Queue



class Mythread(Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.queue = Queue()
        self.start()

    def run(self):
        while True:
            func,args,kwargs = self.queue.get()
            func(*args,**kwargs)
            self.queue.task_done()
    
    def apple_async(self,func,args=(),kwargs={}):
        self.queue.put((func,args,kwargs))

    def join(self):
        self.queue.join()



def task1():
    time.sleep(1)
    logger.info('task1 完成')

def task2(*args,**kwargs):
    time.sleep(2)
    logger.info('task222 完成')

if __name__ == '__main__':
    logger.info('main')
    t = Mythread()
    t.apple_async(task1)
    t.apple_async(task2,args=(1,2),kwargs={"aaa":"www"})
    logger.info('任务提交完成')
    t.join()
    logger.info('任务完成')
    # args = ()
    # kwargs = {}
    # q = Queue()
    # q.put( (task2,args=(1,2),kwargs={'111':'222'}) )
    # t,args,kwargs = q.get()
    # t(*args,**kwargs)