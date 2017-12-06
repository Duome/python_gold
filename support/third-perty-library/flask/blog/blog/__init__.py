# -*- coding: utf-8 -*-

from flask import Flask
from flask_redis import FlaskRedis

#创建项目对象
app = Flask(__name__)

#加载配置文件内容
app.config.from_object('blog.setting')     #模块下的setting文件名，不用加py后缀

db = FlaskRedis(app)

from blog.model import model, user, article
from blog.controller import blog_message
