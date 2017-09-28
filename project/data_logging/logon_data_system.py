# -*- coding: utf-8 -*-
__author__ = 'Duome'

""" 模拟登录数据系统：用于管理用户名和密码。
    实现登录账号创建。
    实现已存在用户可以用登录名字和密码返回系统。
    实现新用户不能用别人的登录名建立用户账号
"""

from storage_data import Data_system


class Logon_data_system(object):

    def __init__(self,save_file):
        self.save_file = save_file
        self.data_system = Data_system()
        self.initial_data = self.data_system.raw_storage_data(self.save_file)
        self.ndata = self.initial_data.iterkeys()
        self.data = self.initial_data.items()

    def olduer(self):
        while True:
            names = raw_input('请输入您的用户名：')
            codes = raw_input('请输入您的密码：')
            if (names, codes) in self.data:
                print '登录成功！'
                break
            else:
                print '用户名或密码错误！'
# 注册

    def newuer(self):
        # 创建新增内存
        self.new_data = {}
        names = raw_input('请设置您的用户名：')
        if names in self.ndata:
            print '用户名已存在，请跟换用户名重新注册或直接登录'
            return self.showmenu()          # 在类里引用自己的方法，括号中不用加self
        else:
            codes = raw_input('请设置您的密码：')
            print '登录成功！'
            self.new_data[names] = codes
        self.data_system.save_new_data(self.new_data)

    def showmenu(self):
        while True:
            start = raw_input('输入1直接登录，输入2进行注册：')
            if start == '1':
                self.olduer()
                break
            elif start == '2':
                self.newuer()
                break
            else:
                print '无法识别，请重新输入！'

if __name__ == '__main__':
    start = Logon_data_system('data.txt')
    start.showmenu()
