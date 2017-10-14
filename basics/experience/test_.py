# -*- coding: utf-8 -*-
__author__ = 'Duome'

from string import Template # Template对象（substitute()方法，safe_substitute()方法）

def test_unicode():
    u = u'中文'    #显示指定unicode类型对象u
    str3 = u.encode('gb2312')    #以gb2312编码对unicode对像进行编码
    str1 = u.encode('gbk')      #以gbk编码对unicode对像进行编码
    str2 = u.encode('utf-8')    #以utf-8编码对unicode对像进行编码
    u1 = str.decode('gb2312')   #以gb2312编码对字符串str进行解码，以获取unicode
    # u2 = str.decode('utf-8')    #如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的unicode类型
    print u, str3, str1, str2, u1
    s = '中文'
    a = s.decode('utf-8')
    print a, type(str3), type(a)

    w = '你好'
    print type(w)

def file_readsize():
    with open('test_one.txt', 'w') as i:
        i .write('10 2 3 5')
    with open('test_one.txt', 'r') as f:
        while True:
            piece = f.read(2)        # 每次读取 1024 个字节（即 1 KB）的内容
            if not piece:
                break
            print piece

def test1():
    class A(object):
        def __init__(self):
            self.coordinate = {}
        def __str__(self):
            return 'point(%s)' % self.coordinate
        def __getitem__(self, key):
            return self.coordinate.get(key)
        def __setitem__(self, key, value):
            self.coordinate[key] = value
        def __delitem__(self, key):
            del self.coordinate[key]
            print 'delete %s' % key
        def __len__(self):
            return len(self.coordinate)
        __repr__ = __str__

    p = A()
    p['x'] = 2
    p['y'] = 5
    print p
    print len(p)

def test2():
    class A(object):
        def __init__(self, x, y):
            self.x, self.y = x, y
        def __call__(self, z):
            return self.x + self.y + z
    p = A(3, 4)
    print callable(p)
    print p(6)

def test3():
    s = Template('${a} ${b}')
    print s.substitute(a='hello', b='world!')

if __name__ == '__main__':
    test3()