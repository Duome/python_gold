# -*- coding: utf-8 -*-


from blog import db


class Model(object):
    _key = None

    def __init__(self, field, value):
        db.hset(self._key, field, value)

    @classmethod
    def fields(cls):
        return db.hkeys(cls._key)

    @classmethod
    def values(cls):
        return db.hvals(cls._key)

    @classmethod
    def get(cls, k):
        return db.hget(cls._key, k)

    @classmethod
    def total(cls):
        return db.hlen(cls._key)

    @classmethod
    def exist(cls, field):
        return field in cls.fields()
