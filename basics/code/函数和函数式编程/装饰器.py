# -*- coding: utf-8 -*-
__author__ = 'Duome'
""" 不改变函数hello的定义，增强函数的功能
    闭包add_main()
    装饰器 decorator_main()
    带有参数的装饰器args__main()
    对带有参数的函数装饰decorator_args_main()， decorator_kwargs_mian()
    多个装饰器decorators_main()
"""

def add(func):
    def inter_add():
        return '$' + func() + '$'
    return inter_add

def add_args(func):
    def inter_add_args(*args, **kwargs):
        ret = func(*args, **kwargs)
        return '$%s$' % ret
    return inter_add_args

def args_add(tag):
    def decorator(func):
        def inter_args_add(*args, **kwargs):
            ret = func(*args, **kwargs)
            return '%s%s%s' % (tag, ret, tag)
        return inter_args_add
    return decorator

def add_one(func):
    def inter_add_one():
        return '$%s$' % func()
    return  inter_add_one

def add_tow(func):
    def inter_add_tow():
        return '@%s@' % func()
    return inter_add_tow

def hello():
    return 'hello world'

class Add(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        return '$%s$' % self.func(*args, **kwargs)

class Add_args(object):
	def __init__(self, tag):
		self.tag = tag
	def __call__(self, func):
		def inter(*args, **kwargs):
			ret = func(*args, **kwargs)
			return '%s%s%s' % (self.tag, ret, self.tag)
		return inter
# -----------------------------------
def decorator():
    """ 装饰器可以定义多个
        离函数定义最近的装饰器先被调用
    """
    @add    # 是一个装饰器，『装饰』了函数 hello，并返回一个函数，将其赋给 hello
    def hello():
        return 'hello world'
    # hello = add(hello)

    return hello

def decorator_args():
    """ 函数中添加一个参数
    """
    @add_args
    def hi(name):
        return 'hello %s' % name
    return hi

def decorator_kwargs():
    """ 函数中添加多个参数
    """
    @add_args
    def hi(name1, name2):
        return 'hello %s %s' % (name1, name2)
    return hi

def args_decorator():
    # tag_add = args_add('%')
    # @tag_add
    @args_add('b')
    def hello(name):
        return 'hello %s' % name
    return hello

def decorators():
    @add_one
    @add_tow
    def hello():
        return 'hello world'
    return hello
def class_decorator():
    @Add
    def hello(name):
        return 'hello%s' % name
    return  hello

def class_args_decorator():
	@Add_args('%')
	def hello(name):
		return 'hello %s' % name
	return hello
# -----------------------------------
def add_main():
    """ 直接使用闭包
    """
    global hello    # 导入全局变量hello，改变的也是全局变量
    hello = add(hello)
    print hello()

def decorator_main():
    start = decorator()
    start()

def decorator_args_main():
    start = decorator_args()
    print start('world')

def decorator_kwargs_mian():
    start = decorator_kwargs()
    print start('world', 'Duome')

def args_main():
    start = args_decorator()
    print start('world')

def decorators_main():
    start = decorators()
    print start()

def class_mian():
    start = class_decorator()
    print start('world')

def class_args_mian():
    start = class_args_decorator()
    print start('world')

if __name__ == '__main__':
    # add_main()
    # decorator_main()
    # decorator_args_main()
    # decorator_kwargs_mian()
    # args__main()
    # decorators_main()
    # class_mian()
    class_args_mian()