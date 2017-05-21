# -*- coding: utf-8 -*-
__author__ = 'Duome'
from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
import os

filename = ''

# 作者信息
def author():
    showinfo('作者信息', '本软件由Duome完成')

def about():
    showinfo('版权信息.Copyright','本软件版权归属为Duome')

# 文件操作
def openfile():
    """打开文件名，为全局的，方便保存
       将之前文件清空
       root的title为文件名
    """
    global filename     # 定义一个全局变量
    filename = askopenfilename(defaultextension = '.txt')   #获取文件名称，默认扩展名为'.txt'
    if filename == '':      # 若没有选择
        filename = None     # 名字为空
    else:
        root.title('FileName:' + os.path.basename(filename))    # 得到实际路径
        textpad.delete(1.0, END)    # 清空文件
    f = open(filename, 'r')
    textpad.insert(1.0, f.read())   # 插入文件
    f.close()

def newfile():
    """清空当前内容
       title也清空
    """
    global filename
    root.title('未命名文件')
    filename = None
    textpad.delete(1.0,END)

def save():
    """在原文件名下存储
       若没有原文件，跳到saveas()
    """
    global filename
    try:
        f = open(filename, 'w')     # 没有文件名时，抛异常
        msg = textpad.get(1.0, END)
        f.write(msg)
        f.close()
    except:
        saveas()

def saveas():
    """另存需要弹出对话框，可以重命名
    """
    f = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')  # 默认文件名，初始化格式
    global filename
    filename = f
    fh = open(f, 'w')
    msg = textpad.get(1.0, END)
    fh.write(msg)
    fh.close()
    root.title('FileName:' + os.path.basename(f))

# 编辑操作(TK库)
def cut():
    textpad.event_generate('<<Cut>>')

def copy():
    textpad.event_generate('<<Copy>>')

def paste():
    textpad.event_generate('<<Paste>>')

def redo():
    textpad.event_generate('<<Redo>>')

def undo():
    textpad.event_generate('<<Undo>>')

def selectAll():
    textpad.tag_add('sel', '1.0', END)

# def goselect():
#     """button的回调函数——get值，search值，tag_add出来
#     """
#     cont = entry.get()
#     Scont = textpad.search(cont, start, stopindex=END)
#     Scont.tag_add('sel', '1.0', END)

def select():
    """弹出对话框——label、entry、button
    """
    selectlevel = Toplevel(root)
    selectlevel.geometry('250x30+200+250')
    label = Label(selectlevel, text='Find')
    label.grid(row=0, column=1, padx=5)
    entry = Entry(selectlevel, width=20)
    entry.grid(row=0, column=2, padx=20)
    def goselect():
        print 'search'
        # cont = entry.get()
        # textpad.search(cont, 1.0, stopindex=END)
        # textpad.tag_add('match', '1.0', END)
    button = Button(selectlevel,text='查找', command=goselect)# command=goselect)(lambda x : goselect)(1))
    button.grid(row=0, column=3, padx=5)


root = Tk()
root.title('Duome Node')
root.geometry('800x500+100+100')    # 窗口大小是500x500像素，初始化显示位置是topleft, topright为100

# Create Menu
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command(label='新建', accelerator='Ctrl + N', command=newfile)    # 加快捷键
filemenu.add_command(label='打开', accelerator='Ctrl + O', command=openfile)
filemenu.add_command(label='保存', accelerator='Ctrl + S', command=save)
filemenu.add_command(label='另存为', accelerator='Ctrl +Shift + N', command=saveas)
menubar.add_cascade(label='文件', menu=filemenu)

editmenu = Menu(root)
editmenu.add_command(label='撤销', accelerator='Ctrl + Z', command=undo)
editmenu.add_command(label='重做', accelerator='Ctrl + Y', command=redo)
editmenu.add_separator()
editmenu.add_command(label='剪切', accelerator='Ctrl + X', command=cut)
editmenu.add_command(label='复制', accelerator='Ctrl + C', command=copy)
editmenu.add_command(label='粘贴', accelerator='Ctrl + V', command=paste)
editmenu.add_separator()
editmenu.add_command(label='查找', accelerator='Ctrl + F', command=select)
editmenu.add_command(label='全选', accelerator='Ctrl + A', command=selectAll)
menubar.add_cascade(label='编辑',menu=editmenu)

aboutmenu = Menu(root)
aboutmenu.add_command(label='作者', command=author)
aboutmenu.add_command(label='版权', command=about)
menubar.add_cascade(label='关于', menu=aboutmenu)

# Create Toolbar
toolbar = Frame(root, height=25,bg='light sea green')
toolbar.pack(expand=NO, fill=X)
button1 = Button(toolbar,text='打开', bd=3, relief=RAISED, command=openfile)
button1.pack(side=LEFT, padx=5, pady=5)
button1 = Button(toolbar,text='保存', bd=3, relief=RAISED, command=save)
button1.pack(side=LEFT)

# Create Statusbar
status = Label(root, text='Ln20', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# Create linenumber & text
lnlabel = Label(root, width=2, bg='antique white')
lnlabel.pack(side=LEFT, fill=Y)

textpad = Text(root, undo=True)     # undo功能
textpad.pack(expand=YES, fill=BOTH)     # 允许进行扩展

scroll = Scrollbar(textpad)     # 进度卷动条
textpad.config(yscrollcommand=scroll.set)   # 显示Y轴
scroll.config(command=textpad.yview)    # 与文本内容绑定
scroll.pack(side=RIGHT,fill=Y)


root.mainloop()