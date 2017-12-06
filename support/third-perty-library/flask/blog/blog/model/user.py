# -*- coding: utf-8 -*-


from blog.model.model import Model


class User(Model):
    _key = 'user'

    def __init__(self, field, value):
        super(User, self).__init__(field ,value)
        self.username = field
        self.password = value

    def __repr__(self):
        return '<User: %s | Password: %s>' % (self.username, self.password)
