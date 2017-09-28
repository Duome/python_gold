# -*- coding: utf-8 -*-
__author__ = 'Duome'
""" 运算方法总和的类
    过滤价格Remove
"""

class Operation(object):

    def filter_prince(self, minValue, maxValue, searchData, defaultData):
        self.minValue = minValue        # 在界面entry中得到的每平最低价
        self.maxValue = maxValue        # 在界面entry中得到的每平最高价
        self.defaultData = defaultData      # 在数据处理中得到的数据内存
        self.searchData = searchData        # 在数据处理中得到的self.sheetnames
        self.ndata = {}
        for i in self.searchData:           # i 是每个sheet的名字
            row_nums = len(self.defaultData[i])
            self.ndata[i] = []
            self.ndata[i].append(self.defaultData[i][0])
            for row in range(row_nums - 1):
                price = self.defaultData[i][row + 1][2]
                if self.minValue == self.maxValue == price :
                    self.ndata[i].append(self.defaultData[i][row + 1])
                elif self.minValue <= price < self.maxValue:
                    self.ndata[i].append(self.defaultData[i][row + 1])
                else:
                    continue
        return self.ndata
