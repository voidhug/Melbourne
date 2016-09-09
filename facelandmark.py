#!/usr/bin/env python
# coding: utf-8
import urllib2
import urllib
import json
from uplodePhotos import Uper
from postsmile import Smile
import Emotion


class Landmark():
    API_KEY = '07fa940f62796288e7cb675c92829ad0'
    API_SECRET = 'ELWIYZZeYf-zPAloQt_1OtqF7CtlQX3W'

    def __init__(self, dst):
        self.dst = dst

    def get(self):
        a = Uper(self.dst)
        dst = a.get()
        smile = Smile(self.dst)
        k = smile.get()
        smile_res = json.loads(k)
        self.face_id = smile_res['face'][0]['face_id']
        data = {}
        data['api_key'] = self.API_KEY
        data['api_secret'] = self.API_SECRET
        # data['img'] = f.read()
        data['face_id'] = self.face_id

        url = 'http://api.faceplusplus.com/detection/landmark'
        post_data = urllib.urlencode(data)

        request = urllib2.Request(url, post_data)
        req = urllib2.urlopen(request)

        content = req.read()
        landmark_res = json.loads(content)
        return dst, landmark_res

    def handle_res(self, landmark_res):
        points = landmark_res['result'][0]['landmark']
        points_list = list(points)
        points_list.sort()
        valid_points = {12: 0, 10: 9, 11: 18, 8: 7, 9: 16, 6: 6, 7: 15,
                        44: 41, 43: 38, 42: 44, 46: 37, 45: 49, 4: 40, 48: 46, 47: 52, 5: 43, 39: 48, 40: 54, 41: 51,
                        3: 58,
                        13: 29, 14: 34, 15: 35, 16: 36, 17: 33,
                        22: 79, 21: 82, 20: 81, 19: 80, 18: 75,
                        1: 20, 23: 21, 24: 27, 25: 26, 26: 28, 27: 25, 30: 22, 29: 19, 28: 23,
                        2: 70, 31: 67, 32: 73, 33: 72, 34: 74, 35: 71, 38: 68, 37: 65, 36: 69}
        out_data = []
        for i in range(1, 49):
            in_data = []
            in_data.append(points[points_list[valid_points[i]]]['x'])
            in_data.append(points[points_list[valid_points[i]]]['y'])
            out_data.append(in_data)
        return out_data


# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/1.jpg')
# b = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/1.jpg')

# ztc 4 1898
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/4.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/ztc4.jpg')

# zx 4 1582
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/4.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/zx4.jpg')

# ztc 3 4975
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/3.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/ztc3.jpg')

# zx 3 3045
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/3.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/zx3.jpg')

# ztc 2 770
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/2.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/ztc2.jpg')

# ztc 2 425
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/2.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/zx2.jpg')

# ztc 1 1314
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/1.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/ztc1.jpg')

# zx 1 545
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/1.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/zx1.jpg')

# ztc pingjing 1 290
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/1.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/ztcpingjing.jpg')

# ztc pingjing 2 993
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/2.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/ztcpingjing.jpg')

# ztc pingjing 3 5646
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/3.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/ztcpingjing.jpg')

# ztc pingjing 4 835
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/4.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/ztcpingjing.jpg')

# zx pingjing 1 1 脏
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/1.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/zxpingjing.jpg')

# zx pingjing 2 801
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/2.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/zxpingjing.jpg')

# zx pingjing 3 5935
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/3.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/zxpingjing.jpg')

# zx pingjing 4 1124
# a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/4.jpg')
# b = Landmark('/Users/voidhug/Desktop/zhaopian/zxpingjing.jpg')

# res_a = a.get()
# res_handled_a = a.handle_res(res_a)
# res_b = b.get()
# res_handled_b = b.handle_res(res_b)
# like,v= Emotion.proc_diff(res_handled_a, res_handled_b)
# print v
# print like

# 0.000856389122827
if __name__ == '__main__':
    str1 = 'http://i.niupic.com/images/2016/08/21/blOvqq.jpg'

    # 张旭 模仿傅 二
    str2 = "https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/97E12037F139859311C04AC1949C713A.jpg"

    # 朱天成 模仿傅
    str3 = 'https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/B5CB4D2C94B329E15EDFCA6DDC4133F2.jpg'

    str4 = 'http://i4.cqnews.net/4G/attachement/png/site82/20160809/780cb8d50dd6191359bc0f.png'

    # 张瑞鹏 模仿 傅园慧 疑惑 99.9992729096 1.45418072167e-05 0.0 2477.0015691s
    a = Landmark('/Users/voidhug/Desktop/GitHub/Melbourne/fuyuanhui/1.jpg')
    b = Landmark('/Users/voidhug/Desktop/zhaopian/zx1.jpg')
    res_a = a.get()
    res_handled_a = a.handle_res(res_a)
    res_b = b.get()
    res_handled_b = b.handle_res(res_b)
    v, like = Emotion.proc_diff(res_handled_a, res_handled_b,count)
    print v
    print like
