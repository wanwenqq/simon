'''
@Author: Anders
@Date: 2019-12-25 09:40:17
@LastEditTime : 2020-01-06 16:28:15
@LastEditors  : Anders
@FilePath: \phpd:\project\python\simon\test.py
@Description: 
'''
from slogging import logger
from sproxy import get_header
from ssettings import mysqlconfig

import random
import requests
import time
import json


def get_ip():
    PROXY_POOL_URL = 'http://localhost:5555/random'
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None


# logger.info('log test')
# print(get_header())
# print(mysqlconfig['host'])

def do_request():
    header = get_header()
    # print(header)
    ad_header = {}
    ad_header['Content-Type']='application/json'
    ad_header['User-Agent']= header
    # print(ad_header)
    # return
    while True:
        ip = get_ip()
        print(ip)
        if ip == None:
            return 
        print('----')
        proxies={'http':ip,'https':ip} 

        # req_url = 'https://httpbin.org/get'
        categoryId = 0
        instanceId = 33720
        libraryType = 1
        categoryId = random.randint(0,1000)
        instanceId = random.randint(0,100000)
        libraryType = random.randint(0,1000)
        req_url = 'http://api.bookan.com.cn/resource/categoryList'


        body = {'categoryId':categoryId,
            'instanceId':instanceId,
            'libraryType':libraryType}
        try:
            requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
            s = requests.session()
            s.keep_alive = False # 关闭多余连接
            response = s.get(req_url, data=json.dumps(body),headers = ad_header,timeout=10)
            status=response.status_code # 状态码
            print(response.text)
            print(status)
            return
        except Exception as e:
            print(e)
            # pass

if __name__ == '__main__':
    do_request()