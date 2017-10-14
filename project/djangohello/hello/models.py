# -*- coding=utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Publisher(models.Model):   # 相对于Book是主键类
    name = models.CharField(max_length=30, verbose_name="名称")
    address = models.CharField("地址", max_length=50)
    city = models.CharField('城市', max_length=60)
    state_province = models.CharField('省份', max_length=30)
    country = models.CharField('国家', max_length=50)
    website = models.URLField('网址')

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField('名称', max_length=30)

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class AuthorDetail(models.Model):
    sex = models.BooleanField('性别', max_length=1, choices=((0, '男'), (1, '女'),))
    email = models.EmailField('邮件')
    address = models.CharField('地址', max_length=50)
    birthday = models.DateField('生日')
    author = models.OneToOneField(Author)

    class Meta:
        verbose_name = '作者详情'
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.name

class Book(models.Model):   # 相对于Publisher和Author是外键类
    title = models.CharField('名称', max_length=100)
    authors = models.ManyToManyField(Author)   # 外键
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10)

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

# from django.db import models
#
# class Actor(models.Model):
#     actor = models.CharField('名字', max_length=20, null=True)
#
# class Production(models.Model):
#     name = models.CharField('名称', max_length=100)
#     actor = models.OneToOneField(Actor)