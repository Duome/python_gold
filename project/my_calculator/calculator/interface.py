# -*- coding: utf-8 -*-
__author__ = 'Duome'

""" 显示屏只有有一行。
    显示屏上，数字前不得出现"0",
    例如不得出现20+2*3-05，但允许出现20+2*3-0，解决方式：键入20+2*3-0后，再键入5时，显示变为20+2*3-5。
    蓝#113F3D   灰#3C4F39    棕#5F5C33    绿#B3D66E    橙#F8931D
    淡#FFFC99   深#FFE882

"""

from Tkinter import *


class Interface(object):
    def __init__(self):
        self.text = []
        self.set_layout()

    def set_layout(self):
        root = Tk()
        root.title('calculator')
        root.config(bg='#113F3D')
        root.geometry('320x470+100+100')

        status_bar = Label(root, height=1, bg='#3C4F39')
        status_bar.pack(side=TOP, fill=X)

        title = Label(root, text='Dddmo', height=1, fg='#B3F16E', bg='#5F5C33', anchor='w')
        title.config(font=('times', '12', 'bold'))
        title.pack(side=TOP, fill=X)
        label = Label(root, bg='#113F3D',width=2)
        label.pack(side='top', fill=X)
        label_l = Label(root, bg='#113F3D',width=2)
        label_l.pack(side='left', fill=Y)
        label_r = Label(root, bg='#113F3D',width=2)
        label_r.pack(side='right', fill=Y)

        display_bar = Label(root, bg='#113F3D', width=10, height=20)
        display_bar.pack()
        self.equation = Label(display_bar, bg='#5F5C33', width=29, height=1, relief=SUNKEN)
        self.equation.config(font=('times', 12), anchor='e')
        self.equation.pack()
        self.operation_result = Label(display_bar, bg='#5F5C33', width=13, height=1, relief=SUNKEN)
        self.operation_result.config(font=('times', 25, 'bold'), anchor='e')
        self.operation_result.pack()

        label_t = Label(root, bg='#113F3D',height=2)
        label_t.pack(side='top', fill=X)
        label_b = Label(root, bg='#113F3D',height=2)
        label_b.pack(side='bottom', fill=X)

        frame = Frame(root, bg='#113F3D', width=100, height=500)
        frame.pack(fill=BOTH)

        button7 = Button(frame, text='7', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('7'))
        # button7.configure(width=10)
        button7.grid(row=0, column=1, padx=5, pady=7)
        button8 = Button(frame, text='8', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('8'))
        button8.grid(row=0, column=2, padx=5, pady=7)
        button9 = Button(frame, text='9', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('9'))
        button9.grid(row=0, column=3, padx=5, pady=7)
        button4 = Button(frame, text='4', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('4'))
        button_remove = Button(frame, text='DEL', fg='#B3F16E', bg='#F8931D', command=self.remove)
        button_remove.config(width=7, height=2, relief=RIDGE)
        button_remove.grid(row=0, column=4, padx=5, pady=7)
        button4.grid(row=1, column=1, padx=5, pady=7)
        button5 = Button(frame, text='5', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('5'))
        button5.grid(row=1, column=2, padx=5, pady=7)
        button6 = Button(frame, text='6', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('6'))
        button6.grid(row=1, column=3, padx=5, pady=7)
        button_multiply = Button(frame, text='*', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('*'))
        button_multiply.grid(row=1, column=4, padx=5, pady=7)
        button1 = Button(frame, text='1', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('1'))
        button1.grid(row=2, column=1, padx=5, pady=7)
        button2 = Button(frame, text='2', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('2'))
        button2.grid(row=2, column=2, padx=5, pady=7)
        button3 = Button(frame, text='3', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('3'))
        button3.grid(row=2, column=3, padx=5, pady=7)
        button_add = Button(frame, text='+', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('+'))
        button_add.grid(row=2, column=4, padx=5, pady=7)
        button0 = Button(frame, text='0', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=self.num0)
        button0.grid(row=3, column=1, padx=5, pady=7)
        button_point = Button(frame, text='.', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('.'))
        button_point.grid(row=3, column=2, padx=5, pady=7)
        button_mimus = Button(frame, text='-', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('-'))
        button_mimus.grid(row=3, column=3, padx=5, pady=7)
        button_clear = Button(frame, text='C', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=self.clear)
        button_clear.grid(row=3, column=4, padx=5, pady=7)
        button_divide = Button(frame, text='/', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('/'))
        button_divide.grid(row=4, column=1, padx=5, pady=7)
        button_power = Button(frame, text='^', fg='#B3F16E', bg='#3C4F39', width=7, height=2, relief=RIDGE, command=lambda: self.screen('**'))
        button_power.grid(row=4, column=2, padx=5, pady=7)
        button_equal = Button(frame, text='=', fg='#B3F16E', bg='#F8931D', width=17, height=2, relief=RIDGE, command=self.equal)
        button_equal.grid(row=4, column=3, columnspan=2, padx=5, pady=7)

        root.mainloop()

    def num0(self):
        # self.text.append('0')
        # self.equation.config(text=''.join(self.text))
        length = len(self.text)
        end_ele = int(self.text[length-1])
        if not self.text:
            pass
        elif isinstance(self.end_ele, int):
            self.text.append('0')
            self.equation.config(text=''.join(self.text))
        else:
            self.equation.config(text=''.join(self.text))

    def screen(self, num):
        self.text.append(num)
        self.equation.config(text=''.join(self.text))


    def remove(self):
        try:
            length = len(self.text)
            del self.text[length-1]
            self.equation.config(text=''.join(self.text))
        except IndexError:
            self.text = self.newtext
            leng = len(self.text)
            print leng
            del self.text[leng-1]
            self.equation.config(text=''.join(self.text))

    def clear(self):
        del self.text[:]
        self.equation.config(text=''.join(self.text))

    def equal(self):
        # firstnum = []
        if '.' in self.text:
            pass
        else:
            self.text.append('.0')
            # firstnum.append(i)
            # if i in ['+', '-', '/', '*', '^']:
            #     if '.' not in firstnum:
            #         num = self.text.index(i)
            #         self.text[num]='.0%s' %i
            #     else:
            #         pass
            #     break
        try:
            data = ''.join(self.text)
            self.newtext = list(data)
            result = eval(data)
            screen_data = str(result)
            self.operation_result.config(text=screen_data)
            del self.text[:]
            self.text.append(screen_data)
        except SyntaxError:
            self.operation_result.config(text='ERR')
            del self.text[:]



if __name__ == '__main__':
    start = Interface()

