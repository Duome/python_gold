# -*- coding: utf-8 -*-
__author__ = 'Duome'
"""
"""


from Tkinter import *
import tkMessageBox     # 调用对话框


def text():
    def oh():
        a = textpad.search('a', 1.0, stopindex=END)
        print a, type(a)
        b = textpad.tag_add('match', '1.0', END)
        print b, type(b)
    root = Tk()
    lnlabel = Label(root, width=2, bg='antique white')
    lnlabel.pack(side=LEFT, fill=Y)
    button = Button(lnlabel, text='oh')
    button.pack()

    textpad = Text(root, undo=True)     # undo功能
    textpad.pack(expand=YES, fill=BOTH)     # 允许进行扩展

    scroll = Scrollbar(textpad)     # 进度卷动条
    textpad.config(yscrollcommand=scroll.set)   # 显示Y轴
    scroll.config(command=textpad.yview)    # 与文本内容绑定
    scroll.pack(side=RIGHT,fill=Y)
    root.mainloop()




def hello_world():
    """创建窗口
    """
    root = Tk()     # Tk类的实例，返回根窗体实例（最底层窗体实例）
    label = Label(root, text='Hello world')     # 子对象，元素一是父窗体，元素二是UI元素
    label.pack()   # 窗口呈现
    root.mainloop()     # 死循环实现窗口一直呈现致程序结束

def hello_class():
    """使用类创建窗口
    """
    class App(object):
        def __init__(self, master):
            frame = Frame(master)
            frame.pack()

            self.button = Button(frame, text='Hello class', fg='red', command=frame.quit)
            self.button.pack()

            self.hiButton = Button(frame, text='Say Hi', command=self.say_hi)
            self.hiButton.pack()
        def say_hi(self):
            print 'Hi Duome, Thanks!'
    root = Tk()
    app = App(root)
    root.mainloop()
    root.destroy()

def widget_config():
    """设置配置
    """
    root = Tk()
    label = Label(root, text='Hello world')     # label的父级不能是frame可以是root
    label.config(cursor='gumby')
    label.config(height=10, width=30, fg='yellow', bg='#343343')    # 这里的位置是可以变得
    label.config(font=('times', '28', 'bold'))      # 这里索引对应的设置是不变的
    label.pack()
    root.mainloop()

def widget_style():
    """常用外观属性
    """
    button=Button(text='Duome', padx=10, pady=10)
    button.config(cursor='gumby')       # 鼠标
    button.config(bd=10, relief=RAISED)     # 边界
    button.config(bg='red', fg='yellow')    # 颜色
    button.config(font=('Helvetica', 10, 'bold italic'))    # 字体
    button.pack()
    button.mainloop()

def event_style():
    """事件实现方式command, bind, protocol
       事件格式化
       事件属性
    """
    root = Tk()
    def callback(event):
        frame.focus_set()
        print 'clicked at:', event.x, event.y   # 属性x, y

    def key(event):
        print 'pressed', repr(event.char)       # 属性char


    def closewindow():
        if tkMessageBox.askokcancel('Quit', 'Do you want to exit'):
            root.destroy()

    def button_click():
        print 'button clicked'


    frame = Frame(root, width=100, height=100)  # 这个代表root里的容器，设置的太小作用的部分就很小，所以尽量设大一点
    frame.bind('<Button-1>', callback)                      # bind事件实现方式
    frame.bind('<Key>',key)        # '<Key>'事件格式化
    frame.pack()
    button = Button(text='hello', command=button_click)     # command事件实现方式（限button）
    button.pack()
    root.protocol('WM_DELETE_WINDOW',closewindow)           # protocol事件实现方式
    root.mainloop()

def UI_toplevel():
    """UI组件中的窗口组件
       用来打开一个新窗口
    """
    root = Tk()
    root.title('root')
    top = Toplevel(bg='red')
    top.title('top')
    root.mainloop()

def UI_menu():
    """设置菜单
       父菜单、子菜单、下划线
    """
    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    def menu_call():
        print 'Thanks for using it!'
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New', command=menu_call)
    filemenu.add_command(label='open..', command=menu_call)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=menu_call)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='about..', command=menu_call)

    root.mainloop()

def UI_toolbar():
    """设置工具栏
    """
    root = Tk()
    def callback():
        print 'clicked tool bar button'
    toolbar = Frame(root)
    b = Button(toolbar, text='new', width=6, command=callback)
    b.pack(side=LEFT, padx=2, pady=2)   # 显示时设置从左到右和位置
    c = Button(toolbar, text='open', width=9, command=callback)
    c.pack(side=RIGHT, padx=10, pady=10)
    toolbar.pack(side=TOP,fill=X)   # fill拉伸，双向拉伸both
    root.mainloop()

def UI_messagebox():
    root = Tk()
    def callback1():
        if tkMessageBox.showerror('Sundy', 'Hi, Sundy'):    # 显示错误
            print 'Clicked Yes'
        else:
            print 'Clicked No'
    def callback2():
        if tkMessageBox.askyesno('Sundy', 'Hi, Sundy'):     # 显示是或否
            print 'Clicked Yes'
        else:
            print 'Clicked No'
    def callback3():
        if tkMessageBox.askquestion('Sundy', 'Hi, Sundy'):     # 显示是或否
            print 'Clicked Yes'
        else:
            print 'Clicked No'
    def callback4():
        if tkMessageBox.askokcancel('Sundy', 'Hi, Sundy'):     # 显示确定或取消
            print 'Clicked Yes'
        else:
            print 'Clicked No'
    def callback5():
        if tkMessageBox.showwarning('Sundy', 'Hi, Sundy'):     # 显示警告
            print 'Clicked Yes'
        else:
            print 'Clicked No'
    button1 = Button(root, text='Showerror', command=callback1)
    button2 = Button(root, text='Askyesno', command=callback2)
    button3 = Button(root, text='Askquestion', command=callback3)
    button4 = Button(root, text='Askokcancel', command=callback4)
    button5 = Button(root, text='Showwarning', command=callback5)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    root.mainloop()

def UI_statusBar():
    root = Tk()
    status = Label(root, text='Ln20', bd=1, relief=SUNKEN, anchor=W)    # anchor左对齐
    status.pack(side=BOTTOM, fill=X)
    root.mainloop()

def UI_grid():
    root = Tk()
    Label(root, text='First').grid(row=0)
    Label(root, text='Second').grid(row=1)
    e1 = Entry(root)
    e2 = Entry(root)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    Button(root, text='OK').grid(row=2)
    root.mainloop()

def UI_entry():
    root = Tk()
    # e = Entry(root)
    # e.pack()
    #
    # e.insert(0, "a default value")
    # e.delete(0, END)
    # print e.get()
    # e.config(show='*')      # 输入内容显示为*，输密码时可以设置
    v = StringVar()
    e = Entry(root, textvariable=v)
    e.pack()

    v.set("a default value")
    s = e.get()
    print s
    root.mainloop()

def UI_cavens():
    filename = u"C:\\Documents and Settings\\Administrator\\桌面\\tooopen_sy_127457023651.jpg"
    root = Tk()
    img = PhotoImage(file=filename)
    label = Label(root, text="hello",image=img)
    label.pack()
    root.mainloop()

if __name__ == '__main__':
    # hello_world()
    # hello_class()
    # widget_config()
    # widget_style()
    # event_style()
    # UI_toplevel()
    # UI_menu()
    # UI_toolbar()
    # UI_messagebox()
    # UI_statusBar()
    # UI_grid()
    # text()
    # UI_entry()
    UI_cavens()