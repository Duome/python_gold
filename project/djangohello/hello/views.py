# -*- coding=utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.template import loader, RequestContext, Template
from hello.models import *
from hello.forms import PublisherForm
# Create your views here.

def hello(request, a):
    # print Publisher.objects.all()   # 返回的QuerySet，使用时，才会去执行sql语句
    user_list = User.objects.all()
    athlete = '0'
    athlete_list = [1, 2, 3, 4]
    sgregthernytyjtrh = 99
    value1 = "This text will be HTML-escaped"
    value2 = "<a herf=" ">百度</a>"
    value3 = Template("<a herf='http://www.baidu.com'>百度</a>")
    # print user_list.query
    # 接受url中的变量
    # print a

    # HttpRequest方法
    # print isinstance(request, HttpRequest)
    # print request.GET.get('key')
    # print request.POST.get('name')
    # print request.get_full_path()   # 返回路径，包含参数

    # HttpResponse方法
    # response = HttpResponse('Here is a web from Duome! Welcome!')
    # return response
    # Author.objects.get_or_create(name='你好')
    # user_list = Author.objects.all()

    # return render(request, 'table.html', {'user_list': user_list})   # render方法，自动传递上下文（request）

    # t = loader.get_template('table.html')   # 直接使用HttpResponse，装载模板
    # c = {'user_list': user_list}   # 传递给模板的参数
    # return HttpResponse(t.render(c, request),   # 使用的是模板中的render属性
    #                     content_type='text/html')   # 内容格式

    return render_to_response('a.html', locals(), context_instance=RequestContext(request))
    # render_to_response, locals传递作用域所有参数(会造成浪费)，模板中使用csrf_token需要指定上下文

    # return redirect('http://www.baidu.com')   # 跳转页面

def test(request, id, key):
    print id, key
    return render(request, 'table.html')

def add_publisher(request):
    if request.method == 'POST':
        # 一、不适用Form的情况
        # name = request.POST['name']   # 名字是表单元素name属性的值
        # address = request.POST.get('address')
        # Publisher.objects.create(
        #     name=name,
        #     address=address
        # )
        # return HttpResponse("添加出版社信息成功")

        # 使用django.form的情况
        # publisher_form = PublisherForm(request.POST)   # 表单对象通过post的数据初始化
        # if publisher_form.is_valid():
        #     Publisher.objects.create(
        #         name = publisher_form.cleaned_data['name'],
        #         address = publisher_form.cleaned_data['address'],
        #     )
        #     return HttpResponse("添加出版社信息成功")

        # 使用django.ModelForm
        publisher_form = PublisherForm(request.POST)   # 表单对象通过post的数据初始化
        if publisher_form.is_valid():
            publisher_form.save()
            return HttpResponse("添加出版社信息成功")

    else:
        publisher_form = PublisherForm()
    return render(request, 'add_publisher.html', locals())