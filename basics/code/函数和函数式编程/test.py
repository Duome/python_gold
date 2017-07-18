# -*- coding: utf-8 -*-
__author__ = 'Duome'

from functools import wraps
""" 传入参数决定调用哪个闭包
"""

# def foo(word):
#     def bar(func):
#         def post_foo(*args, **kwargs):
#             return '%s Duome' % func(*args, **kwargs)
#
#         def per_foo(*args, **kwargs):
#             return '%s Cccfz' % func(*args, **kwargs)
#         try:
#             words = {'post':post_foo, 'per':per_foo}
#             return words[word]
#         except KeyError, e:
#             print "word must be 'post' or 'per'"
#     return bar
# @foo('e')
# def hello(name):
#     return 'hello %s' % name
#
#  hello('world')

import re
data = 'aaasssbb1bccc12458543257-2344'
patt = '.+?(\d+-\d+)'
pott = '\d+-\d+'
a = re.match(patt, data)
print a.group(1)
b = re.search(pott, data)
print b.group()
# print a.group(2)
print re.search('.+?1', data).group()
