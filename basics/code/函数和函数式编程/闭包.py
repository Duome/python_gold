# -*- coding: utf-8 -*-
__author__ = 'Duome'

from math import pow

def closure():
    def make_pow(n):
        def inner_func(x):     # 嵌套定义了 inner_func
            return pow(x, n)   # 注意这里引用了外部函数的 n
        return inner_func      # 返回 inner_func
    return make_pow

def circulation():
    """ 尽量避免在闭包中引用循环变量，或者后续会发生变化的变量。
    """
    def count():
        funcs = []
        for i in [1, 2, 3]:
            def f():
                return i
            funcs.append(f)
        return funcs
    return count

def ciculation_right():
    def count():
        funcs = []
        for i in [1, 2, 3]:
            def g(param):
                f = lambda : param    # 这里创建了一个匿名函数
                return f
            funcs.append(g(i))        # 将循环变量的值传给 g
        return funcs
    return count

def circulation_main():
    a = circulation()
    f1, f2, f3 =  a()
    print f1(), f2(), f3()

def circulation_right_main():
    a = ciculation_right()
    f1, f2, f3 = a()
    print f1(), f2(), f3()

def closure_main():
    a = closure()
    pow2 = a(2)  # pow2 是一个函数，参数 2 是一个自由变量
    # del a        # 删除 make_pow
    # print a(3)
    print pow2(9)

if __name__ == '__main__':
    # circulation_main()
    # circulation_right_main()
    closure_main()