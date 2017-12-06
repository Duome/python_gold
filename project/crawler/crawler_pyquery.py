# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq

text ="""
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
 """
doc = pq(text)
# p = pq('<p id="hello" class="hello"></p>')('p')
# print p.attr("id")
# print p.attr("class")
# print p.attr("class", "hell")


# p = pq('<p id="hello" class="hello"></p>')('p')
# print p.addClass('beauty')
# print p.removeClass('hello')
# print p.css('font-size', '16px')
# print p.css('background-color','yellow')
# print p.css('font-size', '18px')


# p = pq('<p id="hello" class="hello"></p>')('p')
# print p.append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>')
# print p.prepend('<a>hello</a> Oh yes!')
# d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')
# p.prependTo(d('#test'))
# print p
# print d
# d.empty()
# print d

doc = pq(text)
lis = doc('li')
for li in lis.items():
    print li.html()

# print lis.each(lambda e: e)