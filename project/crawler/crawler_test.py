# -*- coding:utf-8 -*-
import urllib
import urllib2
import requests

# 爬网页
def crawler_html():
    response = urllib2.urlopen('http://www.baidu.com')
    print response.read()

# 爬网页，构造request
def crawler_html_request():
    """
    推荐方法，构建请求，获取响应，逻辑更加清晰明确
    """
    request = urllib2.Request('http://www.baidu.com')
    response = urllib2.urlopen(request)
    print response.read()

# 爬网页，动态传递参数
def crawler_html_post():
    values = {'username': 'duomesiki@163.com', 'password':'duome520!'}
    data = urllib.urlencode(values)
    url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    print response.read()

def crawler_html_get():
    values = {}
    values['username'] = "duomesiki@163.com"
    values['password'] = "duome520!"
    data = urllib.urlencode(values)
    url = "http://passport.csdn.net/account/login"
    geturl = url + "?" + data
    request = urllib2.Request(geturl)
    response = urllib2.urlopen(request)
    print response.read()

def requests_metond():
    import requests

    r = requests.get('http://www.baidu.com')
    print type(r)  # 结果类型
    print r.status_code  # 状态码
    print r.encoding  # 编码方式
    print r.text  # 内容
    print r.cookies

def requests_json():
    r = requests.get('a.json')
    print r.text
    print r.json()

def requests_header():
    payload = {'key1': 'value1', 'key2': 'value2'}
    headers = {'content-type': 'application/json'}
    r = requests.get("http://httpbin.org/get", params=payload, headers=headers)
    print r.url
    print r.text

def requests_cookies():
    # url = 'http://www.baidu.com'
    # r = requests.get(url)
    # print r.cookies
    # print r.cookies['example_cookie_name']
    url = 'http://httpbin.org/cookies'
    cookies = dict(cookies_are='working')
    r = requests.get(url, cookies=cookies)
    print r.text

def requests_verify():
    r = requests.get('https://kyfw.12306.cn/otn/', verify=False)
    # r = requests.get('https://github.com', verify=True)
    print r.text

if __name__ == '__main__':
    requests_verify()