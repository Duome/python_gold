# -*- coding: utf-8 -*-
__author__ = 'Duome'


# 读取储存数据
class Data_system(object):

    def raw_storage_data(self,save_file):
        """ 创建原始内存
        """
        self.save_file = save_file
        initial_data = {}
        with open(self.save_file, 'r') as f:
            for i in f:
                dataline = i.split(' ')
                names = dataline[0]
                codes = dataline[1].strip('\n')
                initial_data[names] = codes
        return initial_data

    def save_new_data(self,new_data):
        self.new_data = new_data
        with open(self.save_file, 'a') as f:
            newdata = self.new_data.iteritems()
            for names, codes in newdata:
                f.write('%s %s\n' % (names, codes))
