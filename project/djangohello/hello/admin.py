# -*- coding=utf-8 -*-
from django.contrib import admin
from hello.models import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# Register your models here.

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name',)
admin.site.register(Author)
admin.site.register(AuthorDetail)

# admin.site.register(Publisher, PublisherAdmin)

admin.site.register(Book)

# admin.site.register(Actor)
# admin.site.register(Production)