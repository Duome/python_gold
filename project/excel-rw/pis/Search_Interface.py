# -*- coding: utf-8 -*-
__author__ = 'Duome'

""" 成都房产信息搜索界面
    label
    工具栏grid搜索最低价位，最高价位，确定
"""

from Tkinter import *
from tkMessageBox import *
from Arithmetic import Operation
from Data_processing import Data_processing
import os


def search_interface():
    # 建标题
    root = Tk()
    root.config(bg='#F8F8FF')
    root.title(u'成都房产信息搜索')
    root.geometry('650x300+100+100')

    # 建背景图
    # canvas=Canvas(root,width=400,height=400)
    # canvas.pack()
    # filename = 'frame.gif'
    # img = PhotoImage(file=filename)
    # canvas.create_image(100,100,image=img)
    # Label(root, text="abc", image=img).pack(side=Button)

    # 建主题
    label1 = Label(root, text=u'成都房产信息搜索', width=80, anchor=W)
    label1.config(fg='#000080', bg='#1E90FF')
    label1.config(font=('verdana', '25', 'bold'))
    label1.pack()
    label2 = Label(root, width=3, bg='#F0F8FF', anchor=W)
    label2.pack(side=LEFT, fill=BOTH)

    #建工具栏
    frame = Frame(root, width=10000, height=10000, bg='#F8F8FF')
    frame.pack()
    entry1 = Entry(frame, width=10, cursor='xterm')
    entry1.insert(0, u'每平最低价')
    entry1.config(bg='#F5F5F5')
    entry1.config(font=('Arial', '15'))
    entry1.grid(row=0, column=1, padx=20)
    label3 = Label(frame, text=u'————', width=8)
    label3.config(fg='#00008B', bg='#F8F8FF')
    label3.grid(row=0, column=2, padx=5)
    entry2 = Entry(frame, width=10, cursor='xterm')
    entry2.insert(0, u'每平最高价')
    entry2.config(bg='#F5F5F5')
    entry2.config(font=('Arial', '15'))
    entry2.grid(row=0, column=3, padx=20)

    def price_search():
        try:
            lprice = int(entry1.get())
            hprice = int(entry2.get())
            if lprice >= 0 and hprice >= 0 and lprice <= hprice:
                Get_data = Data_processing()
                default_data = Get_data.get_data('E:\\study_python\\python_gold\\project\\excel-rw\\anjuke.xlsx')
                search_data = Get_data.sheetnames
                Price = Operation()
                New_data = Price.filter_prince(lprice, hprice, search_data, default_data)
                Get_data.save_data(New_data)
            else:
                showerror('错误输入', u'输入无法识别，请重新输入')
        except ValueError:
            showerror('错误输入', u'输入无法识别，请重新输入')

    def open_file():
        os.system('"D:\Microsoft Office\Office14\EXCEL.EXE" search.xlsx')

    button = Button(frame, text=u'确定', width=10)
    button.config(font=('Arial', '10', 'bold'))
    button.config(fg='#191970', bg='#00BFFF', command=price_search)
    button.grid(row=0, column=4, padx=10)

    button = Button(frame, text=u'打开文件', width=10)
    button.config(font=('Arial', '10', 'bold'))
    button.config(fg='#191970', bg='#00BFFF', command=open_file)
    button.grid(row=0, column=5, padx=10)


    root.mainloop()