#!/usr/bin/env python
# coding: utf-8
import urllib2
import urllib

API_KEY = '07fa940f62796288e7cb675c92829ad0'
API_SECRET = 'ELWIYZZeYf-zPAloQt_1OtqF7CtlQX3W'

# f = file('fuyuanhui/1.jpg', 'a+')

#定义一个要提交的数据数组(字典)
data = {}
data['api_key'] = API_KEY
data['api_secret'] = API_SECRET
# data['img'] = f.read()
data['url'] = "https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/1.jpg"
#定义post的地址
url = 'http://apicn.faceplusplus.com/v2/detection/detect'
post_data = urllib.urlencode(data)


#提交，发送数据
request = urllib2.Request(url, post_data)
req=urllib2.urlopen(request)

#获取提交后返回的信息
content = req.read()
print content
