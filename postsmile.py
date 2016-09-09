#!/usr/bin/env python
# coding: utf-8
import urllib2
import urllib
import random

smile_sentences = ['只有在你的微笑里，我才有呼吸。 —— 狄更斯',
         '不管怎样的事情，都请安静地愉快吧！这是人生。我们要依样地接受人生，勇敢地、大胆地，而且永远地微笑着。——卢森堡',
         '生活就是面对真实的微笑，就是越过障碍注视将来。—— 雨果',
         '美是力量，微笑是它的剑。——里德',
         '对我来说，保持健康的方法，不是讲营养，吃补药，而是一句话"在微笑中写作。"——冰心',
         '心情不好的时候也不能忘记微笑。——苍井空']

class Smile():
    API_KEY = '07fa940f62796288e7cb675c92829ad0'
    API_SECRET = 'ELWIYZZeYf-zPAloQt_1OtqF7CtlQX3W'

    def __init__(self, dst):
        self.dst = dst

    def get(self):
        data = {}
        data['api_key'] = self.API_KEY
        data['api_secret'] = self.API_SECRET
        # data['img'] = f.read()
        data['url'] = self.dst
        # 定义post的地址
        url = 'http://apicn.faceplusplus.com/v2/detection/detect'
        post_data = urllib.urlencode(data)

        # 提交，发送数据
        request = urllib2.Request(url, post_data)
        req = urllib2.urlopen(request)

        # 获取提交后返回的信息
        content = req.read()
        print content
        return content

    def get_simle_sentence(self):
        return smile_sentences[random.randint(0, 5)]