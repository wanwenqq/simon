'''
@Author: Anders
@Date: 2020-01-03 11:16:03
@LastEditTime : 2020-01-03 15:15:02
@LastEditors  : Anders
@FilePath: \phpd:\project\python\simon\sredispool.py
@Description: 
'''

'''
使用单例模式创建redis 链接池
'''
import redis
import threading
import time
class sredispool(object):
    _instance_lock = threading.Lock()
    
    def __init__(self,host,port,db):
        self.pool = redis.ConnectionPool(host=host,port=port,db=db)
        self.redis = redis.Redis(connection_pool=self.pool)

    def getRedis(self):
        return self.redis

    @classmethod
    def instance(cls,host,port,db):
        with sredispool._instance_lock:
            if not hasattr(sredispool, "_instance"):
                sredispool._instance = sredispool(host=host,port=port,db=db)
        return sredispool._instance

if __name__ == "__main__":
    # obj = sredispool.instance(host='localhost',port=6379,db=0)
    # print(obj)
    # print(obj.pool)  
    r = sredispool.instance(host='localhost',port=6379,db=0)
    a= r.getRedis().zrangebyscore('proxies',100,100)
    print(a)