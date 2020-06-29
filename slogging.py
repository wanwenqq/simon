'''
@Author: Anders
@Date: 2019-12-25 09:17:59
@LastEditTime : 2019-12-30 16:52:22
@LastEditors  : Anders
@FilePath: \phpd:\project\python\simon\slogging.py
@Description: 
'''
import logging

# 创建一个logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('slog.log')
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

if __name__ == '__main__':
    logger.info('错误是{}'.format('aaaaaaaaaa'))
