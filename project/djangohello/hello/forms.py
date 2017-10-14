# -*- coding=utf-8 -*-
from django import forms
from hello.models import Publisher
from django.core.exceptions import ValidationError

# def validate_name(value):
#     try:
#         Publisher.objects.get(name=value)   # 查到有数据了就带入validate_name函数，相当于回调
#         raise ValidationError("%s的信息已经存在" % value)
#     except Publisher.DoesNotExist:
#         pass

class PublisherForm(forms.ModelForm):
    # name = forms.CharField(label='名称', error_messages={"required": "这个项必填"})
    # address = forms.CharField(label='地址', error_messages={"required": "这个项必填"})
    # city = forms.CharField(label='城市')
    # state_province =forms.CharField(label='省份', error_messages={"required": "这个项必填"})
    # country = forms.CharField(label='国家', error_messages={"required": "这个项必填"})
    # website = forms.URLField(label='网址', error_messages={"required": "这个项必填"})
    # name = forms.CharField(label='名称', validators=[validate_name])

    # def clean_name(self):   # 验证某个字段
    #     value = self.cleaned_data.get('name')
    #     try:
    #         Publisher.objects.get(name=value)
    #         raise ValidationError("%s的信息已经存在" % value)
    #     except Publisher.DoesNotExist:
    #         pass
    #     return value
    # 表单验证
    def clean(self):
        cleaned_data = super(PublisherForm, self).clean()
        value = cleaned_data.get('name')
        try:
            Publisher.objects.get(name=value)
            self._errors['name'] = self.error_class(["%s的信息已经存在" % value])
        except Publisher.DoesNotExist:
            pass
        return cleaned_data
    class Meta:
        model = Publisher
        exclude = ("id",)   # 设置字段id不显示