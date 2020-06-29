import pymysql
from slogging import logger
import traceback
from ssettings import mysqlconfig


class mysqlUtil(object):
    def __init__(self,dbconfig):
        self.host = dbconfig['host']
        self.port = dbconfig['port']
        self.user = dbconfig['user']
        self.passwd = dbconfig['passwd']
        self.dbname = dbconfig['dbname']
        self.charset = 'utf8'


    def connect(self):
        # 使用 connect 方法，传入数据库地址，账号密码，数据库名就可以得到你的数据库对象
        try:
            self.db = pymysql.connect(host=self.host,
            user=self.user,
            password=self.passwd,
            database=self.dbname,
            port=self.port,
            charset='utf8')
        # 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
            # self.cursor = self.db.cursor()
        except Exception as e:
            logger.error('error',e)
        

    
    def close(self):
        self.db.close()


    def queryOne(self,sql,param):
        cur = self.db.cursor()
        row = None
        try:
            cur.execute(sql,param)
            row = cur.fetchone()
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.error("[sql]:{} [param]:{}".format(sql, param))
        finally:
            cur.close()
        return row

    def queryMany(self,sql,param):
        cur = self.db.cursor()
        rows = None
        try:
            cur.execute(sql,param)
            rows = cur.fetchall()
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.error("[sql]:{} [param]:{}".format(sql, param))
        finally:
            cur.close()
        return rows

    def insertOne(self,sql,param=None):
        cur = self.db.cursor()
        lastrowid = 0
        try:
            cur.execute(sql,param)
            self.db.commit()
            lastrowid = cur.lastrowid
        except Exception as e:
            self.db.rollback()
            logger.error(traceback.format_exc())
            logger.error("[sql]:{} [param]:{}".format(sql, param))
        finally:
            cur.close()
        return lastrowid    
        
    def insertMany(self,sql,arrays):
        cur = self.db.cursor()
        count = 0
        try:
            count = cur.executemany(sql, arrays)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            logger.error(traceback.format_exc())
            logger.error("[sql]:{} [param]:{}".format(sql, param))
        finally:
            cur.close()
        
        return count


    def update(self,sql,param):
        cur  = self.db.cursor()
        count = 0
        try:
            count = cur.execute(sql,param)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            logger.error(traceback.format_exc())
            logger.error("[sql]:{} [param]:{}".format(sql, param))
        finally:
            cur.close()
        return count
        
    def delete(self,sql,param):
        cur  = self.db.cursor()
        count = 0
        try:
            count = cur.execute(sql,param)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            logger.error(traceback.format_exc())
            logger.error("[sql]:{} [param]:{}".format(sql, param))
        finally:
            cur.close()
        return count
    


if __name__ == '__main__':
    dbconfig = mysqlconfig

    mu = mysqlUtil(dbconfig)
    mu.connect()

    sql_str = "insert into user(name, mobile) values (%s, %s)"
    param = ('anders','18602736776')
    arrays = [('simon','18602736779'),('sele','18602736777')]
    # lastid = mu.insertOne(sql_str,param)
    # print('lastid',lastid)

    # count = mu.insertMany(sql_str,arrays)
    # print('count',count)
    
    row = mu.queryOne('select * from user where id=%s',2)
    print('row',row)

    # rows = mu.queryMany('select * from user where id>%s',2)
    # a = list(rows)
    # for i in a:
    #     ii = list(i)
    #     print(ii[0],ii[1],ii[2])
    # print(a)
    # print('rows',rows)

    # count = mu.update('update user set name=%s where id>%s',('update',2))
    # print('count',count)

    # count = mu.delete('delete from user where id>%s',2)
    # print('count',count)

    mu.close()
    logger.info('-----')