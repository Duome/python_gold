# -*- coding: utf-8 -*-
__author__ = 'Duome'
"""三方库 MySQLdb 基本使用
   内容：新建库、新增表数据、新增表、删除表、修改表数据、删除表数据、显示表数据
"""
import MySQLdb

def MySQLdb_test():
    pass


def create_database():
    """新建库
    """
    conn = MySQLdb.Connect(
            host='localhost',
            port=3306,
            user='Duome',
            # passwd='123456',
            db='test',
            )               # 函数中有默认参数的，等号两边不用空格

    conn.commit()
    conn.close()

def create_table():
    """新建表
    """
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='admin',
            # passwd='123456',
            db='test',
            )
    cur = conn.cursor()
    cur.execute("create table my_student(id varchar(10), name varchar(20), age int);")

    conn.commit()
    conn.close()
    cur.close()

def delete_table():
    """删除表
    """
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='admin',
            # passwd='123456',
            db='test',
            )
    cur = conn.cursor()
    # cur.execute("drop table my_student;")
    cur.execute("drop table if exists my_student;")

    conn.commit()
    conn.close()
    cur.close()

def insert_data():
    """新增表数据
    """
    conn = MySQLdb.Connect(
            host='localhost',
            port=3306,
            user='Duome',
            # passwd='123456',
            db='test',
            )               # 函数中有默认参数的，等号两边不用空格
    cur = conn.cursor()     # 创建游标
    cur.execute('insert my_student value("001", "xiaofan", 18);' ) # 执行添加，注意语句中加入；
    # for num in xrange(2, 10):
    #     cur.execute('insert student value("00%d", "xiao%d", %d);' % (num, num, num))

    conn.commit()
    conn.close()
    cur.close()


def update_data():
    """修改表数据
    """
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='admin',
            # passwd='123456',
            db='test',
            )
    cur = conn.cursor()
    cur.execute("update my_student set age = '17' where name = 'xiaofan';")

    cur.close()
    conn.commit()
    conn.close()

def delete_data():
    """删除表数据
    """
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='Duome',
            db='test',
            )
    cur = conn.cursor()
    cur.execute("delete from my_student where name = 'xiaofan';")

    cur.close()
    conn.commit()
    conn.close()

def select_data():
    """显示表数据信息
    """
    conn = MySQLdb.connect(
            host='localhost',       # 主机——为ip地址（电脑ID）
            port=3306,      # 端口1-1024不能用 8000之后的
            user='admin',
            # passwd='123456',
            db='test',
            )
    cur = conn.cursor()     # cur游标，conn会话
    result = cur.execute('select * from my_student;')
    print type(result)
    print result
    for item in cur.fetchmany(result):
        print item

    cur.close()
    conn.commit()
    conn.close()



if __name__ == '__main__':
    # MySQLdb_test()
    # create_database()
    # create_table()
    delete_table()
    # delete_data()
    # insert_data()
    # select_data()
    # update_data()
    # delete_data()
