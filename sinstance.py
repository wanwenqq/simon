'''
@Author: Anders
@Date: 2020-02-17 15:31:28
@LastEditTime : 2020-02-17 15:41:26
@LastEditors  : Anders
@FilePath: \python\simon\sinstance.py
@Description: 
'''
import threading
import time

class sInstance(object):
    _threading_lock = threading.Lock()

    def __init__(self,x):
        self.x = x
        time.sleep(1)

    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(sInstance,cls).__new__(cls)

        return cls._instance


def task(arg):
    obj = sInstance(arg)
    print(obj)
 
 

    

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=task, args=(i,))
        t.start()