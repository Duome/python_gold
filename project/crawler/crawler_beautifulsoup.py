# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
"""
soup = BeautifulSoup(html)    # 将本地html文件打开，创建soup对象
# print soup.prettify()    # 打印soup对象
# print soup.head.name    # name属性
# print type(soup.name)
# print type(soup.body.contents)
# print soup.p.contents
# print soup.body.contents
print soup.find_all('bo')