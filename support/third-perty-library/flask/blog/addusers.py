# -*- coding: utf-8 -*-


from blog.model.user import User


def addusers():
    for i in xrange(1, 6):
        print User('user%d' % i, '123')


if __name__ == '__main__':
    addusers()
