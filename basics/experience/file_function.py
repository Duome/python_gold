# -*- coding: utf-8 -*-
__author__ = 'Duome'
"""write_file
"""
import os

def write_file_one():
    """ 将内容写入新建立的文件
        创建文件
        并写入东西
    """
    while True:
        fname = raw_input('您创建的文件名为：')
        if os.path.exists(fname):
            print '您的文件已存在，请跟换文件名！'
        else:
            break
    my_file = open(fname, 'a')
    while True:
        my_note = raw_input('请输入文件内容：')
        my_file.write('%s\n' % my_note)
        if my_note == '.':
            break
        else:
            pass
    my_file.close()


def write_file_list():
    """将内容写入新建的文件
       用列表进行写入
    """
    while True:
        fname = raw_input('您创建的文件名为：')
        if os.path.exists(fname):
            print '您的文件已存在，请跟换文件名！'
        else:
            break
    note = []
    while True:
        my_note = raw_input('请输入文件内容：')
        if my_note == '.':
            break
        else:
            note.append(my_note)
    my_file = open(fname, 'w')
    my_file.writelines(['%s\n' % x for x in note]) #将列表中的内容写入文件
    my_file.close()

def write_file_add():
    """将一个文件中的内容追加写入
       另一个文件
    """
    a = open('a', 'a')
    b = open('b', 'r')
    c = b.read()
    a.write('%s\n' % c)
    a.close()
    b.close()


def write_file_four():
    """使用with..as..将一个文件中的内容
       追加写入另一个文件
       省去关闭文件这一步骤
    """
    with open('a', 'a') as file_a:
        with open('b', 'r') as file_b:
            file_a.writelines([file_b.read(), '\n'])


def read_file_one():
    """读取用户输入文件的内容
    """
    name = raw_input('请输入您需要读取的文件名：')
    fname = open(name, 'r')
    fname_read = fname.read()
    print fname_read


def read_file_two():
    """利用异常测试，读取用户输入文件
    """
    fname = raw_input('请输入您需要读取的文件名：')
    print
    try:
        my_file = open(fname, 'r')
        # for eachline in my_file:
        #     print eachline,
    except IOError, e:
        print '读取文件错误：', e
    else:
        for eachline in my_file:
            # line = eachline.strip('\n') # 可以用strip()去掉文件每行结束的行结束符
            # print line
            print eachline,  # 可以用加逗号','的方法让print语句自动生成行结束符



if __name__ == '__main__':
    write_file_two()
    read_file_two()
