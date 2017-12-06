# -*- coding: utf-8 -*-


from blog.model.model import Model


class Article(Model):
    _key = 'article'

    def __init__(self, field, value):
        super(Article, self).__init__(field, value)
        self.title = field
        self.content = value

    def __repr__(self):
        return '<Title: %s | Content: %s>' % (self.title, self.content)
