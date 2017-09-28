# -*- coding: utf-8 -*-
__author__ = 'Duome'
text = ['5', '.', '2', '+', '3']
from Tkinter import *
import re
from filter import add, power, mimus, divide, multiply
from copy import deepcopy
def a():
    firstnum = []
    for i in text:
        print i

        firstnum.append(i)
        print firstnum
        if i in ['+', '-', '/', '*', '^']:
            if '.' not in firstnum:
                print firstnum
                num = text.index(i)
                text[num]='.0%s' %i
            else:
                continue
            break
    print eval(''.join(text))
    print eval('2.0/3+1')

def b():
    root = Tk()
    label = Label(root, height=2, bg='#113F3D')
    label.pack(side='top', fill=X)
    frame = Frame(root)
    frame.pack()
    text = []
    def screen(i):
        text.append(i)
        label.config(text=''.join(text))
    for i in range(10):
        rownum = [3, 2, 2, 2, 1, 1, 1, 0, 0, 0]
        column = [1, 1, 2, 3, 1, 2, 3, 1, 2, 3]
        ele = str(i)
        Button(frame, text=ele, fg='#B3F16E', bg='#3C4F39', width=7, height=2,relief=RIDGE,
               command=lambda: screen(ele)
               ).grid(row=rownum[i], column=column[i], padx=5, pady=7)
    root.mainloop()


def c():
    list = ['5','.', '2', '^', '2', '2', '2', '/', '1']
    string = ''.join(list)
    # print re.split('(\d+)', string) # 第一个元素和最后一个元素不为数字，按类型将字符分成列表
    numsdata = re.split('\+|-|\*|\^|/', string)
    signdata = re.findall('\D', string)
    print numsdata, signdata


def d():
    text = ['3', '.', '2','-', '2', '.']
    string = ''.join(text)
    numsdata = re.split('\D', string)
    signdata = re.findall('\D', string)

    while  '.' in signdata:
        signdata.remove('.')
    print numsdata, signdata
    database = {'+':add, '^':power, '-':mimus, '*':multiply, '/':divide}
    # for s in [['*', '/'], ['+', '-']]:
    #     while signdata:
    #         i = signdata[0]
    #         if i in s:
    #             site = signdata.index(i)
    #             a = float(numsdata[site])
    #             b = float(numsdata[site+1])
    #             result = database[i](a, b)
    #             del numsdata[site]
    #             numsdata[site] = result
    #             signdata.remove(i)
    #             print numsdata, signdata


def e():
    a = [1, 2, 3]
    b = deepcopy(a)
    b.append(4)
    print a, b

if __name__ == '__main__':
    e()


