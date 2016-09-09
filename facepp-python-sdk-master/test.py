# -*- coding: utf-8 -*-
API_KEY = '07fa940f62796288e7cb675c92829ad0'
API_SECRET = 'ELWIYZZeYf-zPAloQt_1OtqF7CtlQX3W'

from pprint import pformat
import json
import Emotion

def print_result(hint, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(k): encode(v) for (k, v) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hint
    result = encode(result)
    print '\n'.join(['  ' + i for i in pformat(result, width=75).split('\n')])

def writejson2file(obj, filename):
    with open(filename, 'w') as outfile:
        data = json.dumps(obj, indent=4, sort_keys=True)
        outfile.write(data)

from facepp import API

api = API(API_KEY, API_SECRET)

# IMAGE_DIR = 'http://cn.faceplusplus.com/static/resources/python_demo/'
# url = IMAGE_DIR + '4.jpg'

# url = "http://i.niupic.com/images/2016/08/20/6jJO2B.jpg"
# url = "http://i.niupic.com/images/2016/08/20/bkJFXA.jpg"
#
# face = api.detection.detect(url = url)
# face_height = face['face'][0]['position']['height'] * 0.01 * face['img_height']
# face_width = face['face'][0]['position']['width'] * 0.01 * face['img_width']
# face_id = face['face'][0]['face_id']
# points = api.detection.landmark(face_id = face_id)['result'][0]['landmark']
# # points['face_height'] = face_height
# # points['face_width'] = face_width
# # writejson2file(points, './test.json')
#
# points_list = list(points)
# points_list.sort()
#
# valid_points = {12: 0, 10: 9, 11: 18, 8: 7, 9: 16, 6: 6, 7: 15,
#                     44: 41, 43: 38, 42: 44, 46: 37, 45: 49, 4: 40, 48: 46, 47: 52, 5: 43, 39: 48, 40: 54, 41: 51,
#                     3: 58,
#                     13: 29, 14: 34, 15: 35, 16: 36, 17: 33,
#                     22: 79, 21: 82, 20: 81, 19: 80, 18: 75,
#                     1: 20, 23: 21, 24: 27, 25: 26, 26: 28, 27: 25, 30: 22, 29: 19, 28: 23,
#                     2: 70, 31: 67, 32: 73, 33: 72, 34: 74, 35: 71, 38: 68, 37: 65, 36: 69}
#
# out_data = []
# for i in range(1, 49):
#     in_data = []
#     in_data.append(points[points_list[valid_points[i]]]['x'])
#     in_data.append(points[points_list[valid_points[i]]]['y'])
#     out_data.append(in_data)
# print_result("", out_data)

# # 微笑分数
# smile_grade = face['face'][0]['attribute']['smiling']
# print smile_grade

# 表情相似度比对

def url2PointsList(url):
    face = api.detection.detect(url = url)
    face_id = face['face'][0]['face_id']
    points = api.detection.landmark(face_id = face_id)['result'][0]['landmark']
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

# <a href="http://www.niupic.com/photo/522177.html"><img src="http://i.niupic.com/images/2016/08/21/7dmFhq.jpg"></a>

# http://i.niupic.com/images/2016/08/21/cBMwu1.jpg 张旭 斜眼
# http://i.niupic.com/images/2016/08/21/43FQ37.jpg 朱天成 平静
# http://i.niupic.com/images/2016/08/21/SadQ7N.jpg 张旭 斜眼
# http://i.niupic.com/images/2016/08/21/5xTdVU.jpg 朱天成 斜眼
# http://i.niupic.com/images/2016/08/21/27Q0v8.jpg 张旭 平静
# http://i.niupic.com/images/2016/08/21/J7EdTs.jpg 张旭 平静
# http://i.niupic.com/images/2016/08/21/ZeeV6O.jpg 张旭 夸张
# http://i.niupic.com/images/2016/08/21/ZK5qmK.jpg 朱天成 平静
# http://i.niupic.com/images/2016/08/21/nK7CC8.jpg 朱天成 夸张
# http://i.niupic.com/images/2016/08/21/f9o2kQ.jpg 朱天成 夸张
# http://i.niupic.com/images/2016/08/21/HZ3hBC.jpg 张旭 夸张
# http://i.niupic.com/images/2016/08/21/pFXFnu.jpg 朱天成 斜眼

# http://i.niupic.com/images/2016/08/21/GkDdND.jpg 张旭 斜眼
# http://i.niupic.com/images/2016/08/21/S6PMwX.jpg 朱天成 平静
# http://i.niupic.com/images/2016/08/21/ooNMn0.jpg 张旭 斜眼
# http://i.niupic.com/images/2016/08/21/cmtpC5.jpg 朱天成 斜眼
# http://i.niupic.com/images/2016/08/21/blOvqq.jpg 张旭 平静
# http://i.niupic.com/images/2016/08/21/Wbr3Jm.jpg 张旭 平静
# http://i.niupic.com/images/2016/08/21/cW4BUK.jpg 张旭 夸张
# http://i.niupic.com/images/2016/08/21/Jin9A3.jpg 朱天成 平静
# http://i.niupic.com/images/2016/08/21/Tabpsi.jpg 朱天成 夸张
# http://i.niupic.com/images/2016/08/21/Vqv9wZ.jpg 朱天成 夸张
# http://i.niupic.com/images/2016/08/21/EEMtRK.jpg 张旭 夸张
# http://i.niupic.com/images/2016/08/21/43Am9v.jpg 朱天成 斜眼


# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/7dmFhq.jpg"))
# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/eYSG0M.jpg"))
# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/IRY0dk.jpg"))
# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/J3kSoD.jpg"))
# like,v= Emotion.proc_diff(url2PointsList("http://i.niupic.com/images/2016/08/21/7dmFhq.jpg"), url2PointsList("http://i.niupic.com/images/2016/08/21/IRY0dk.jpg"))
# print v
# print like

# ## 朱天成 平静 VS 朱天成 平静 0.0 32389.0000461 不可信
# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/S6PMwX.jpg"))
# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/Jin9A3.jpg"))
# like,v= Emotion.proc_diff(url2PointsList("http://i.niupic.com/images/2016/08/21/S6PMwX.jpg"), url2PointsList("http://i.niupic.com/images/2016/08/21/Jin9A3.jpg"))
# print v
# print like

# ## 张旭 平静 VS 张旭 平静 0.0 6023.00004062
# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/blOvqq.jpg"))
# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/Wbr3Jm.jpg"))
# like,v= Emotion.proc_diff(url2PointsList("http://i.niupic.com/images/2016/08/21/Wbr3Jm.jpg"), url2PointsList("http://i.niupic.com/images/2016/08/21/blOvqq.jpg"))
# print v
# print like

# ## 张旭 平静 VS 张旭 夸张 0.0 14164.026182
# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/blOvqq.jpg"))
# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/cW4BUK.jpg"))
# like,v= Emotion.proc_diff(url2PointsList("http://i.niupic.com/images/2016/08/21/cW4BUK.jpg"), url2PointsList("http://i.niupic.com/images/2016/08/21/blOvqq.jpg"))
# print v
# print like

# ## 张旭 夸张 VS 张旭 夸张 0.0 1446.0000141
# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/Vqv9wZ.jpg"))
# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/cW4BUK.jpg"))
# like,v= Emotion.proc_diff(url2PointsList("http://i.niupic.com/images/2016/08/21/cW4BUK.jpg"), url2PointsList("http://i.niupic.com/images/2016/08/21/Vqv9wZ.jpg"))
# print v
# print like

# ## 张旭 夸张 VS 张旭 夸张 0.0 1446.0000141
# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/Vqv9wZ.jpg"))
# print_result("", url2PointsList("http://i.niupic.com/images/2016/08/21/cW4BUK.jpg"))
# like,v= Emotion.proc_diff(url2PointsList("http://i.niupic.com/images/2016/08/21/cW4BUK.jpg"), url2PointsList("http://i.niupic.com/images/2016/08/21/Vqv9wZ.jpg"))
# print v
# print like

# # 朱天成 咪咪笑
# str1 = 'https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/209741014C27357CAB59BADB0F041AD0.jpg'
#
# # 朱天成 咪咪笑
# str2 = 'https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/BDC15BE7FAD12DCB7A2269CF88418A92.jpg'
#
# # 朱天成 平静
# str3 = 'https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/BA4E9F2ADDE02575205BEB2CA0E16636.jpg'
#
# # 朱天成 平静
# str4 = 'https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/FDDFBA9106F632C11CE26B21B6DB0BD7.jpg'

# ## 朱天成 咪咪笑 VS 朱天成 咪咪笑 99.9999815278 3.69444957864e-07 忽略
# print_result("", url2PointsList(str1))
# print_result("", url2PointsList(str2))
# like,v= Emotion.proc_diff(url2PointsList(str1), url2PointsList(str2))
# print v
# print like

# ## 朱天成 平静 VS 朱天成 平静 0.0 4207.0000025
# print_result("", url2PointsList(str3))
# print_result("", url2PointsList(str4))
# like,v= Emotion.proc_diff(url2PointsList(str3), url2PointsList(str4))
# print v
# print like

# ## 朱天成 平静 VS 朱天成 咪咪笑 0.0 5000.00238902
# print_result("", url2PointsList(str3))
# print_result("", url2PointsList(str1))
# like,v= Emotion.proc_diff(url2PointsList(str3), url2PointsList(str1))
# print v
# print like

# # 张瑞鹏 平静
# str1 = 'https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/591F2050DBED19D3254AEBD9FAF4C4A3.jpg'
#
# # 张瑞鹏 疑惑
# str2 = 'https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/C15BA81563C3C88D80A68ACB2949E4C2.jpg'
#
# # 张瑞鹏 疑惑
# str3 = 'https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/C5731E69F94016018B34CC9B9CF9D340.jpg'
#
# # 张瑞鹏 平静
# str4 = 'https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/EDB5FFB1DE380F5301C7113B6124B4C5.jpg'

# ## 张瑞鹏 平静 VS 张瑞鹏 平静 99.9992729096 1.45418072167e-05 疑惑
# a = str1
# b = str4
# print_result("", url2PointsList(a))
# print_result("", url2PointsList(b))
# like,v= Emotion.proc_diff(url2PointsList(a), url2PointsList(b))
# print v
# print like

# ## 张瑞鹏 平静 VS 张瑞鹏 疑惑 99.9992729096 1.45418072167e-05 0.0 2477.0015691
# a = str1
# b = str2
# print_result("", url2PointsList(a))
# print_result("", url2PointsList(b))
# like,v= Emotion.proc_diff(url2PointsList(a), url2PointsList(b))
# print v
# print like

# 张旭 模仿傅 一
# str1 = 'https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/31794369EB89FF31251D73B0DC9EA3CF.jpg'
str1 = 'http://i.niupic.com/images/2016/08/21/blOvqq.jpg'

# 张旭 模仿傅 二
str2 = "https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/97E12037F139859311C04AC1949C713A.jpg"

# 朱天成 模仿傅
str3 = 'https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/B5CB4D2C94B329E15EDFCA6DDC4133F2.jpg'

# 傅园慧
str4 = 'http://i4.cqnews.net/4G/attachement/png/site82/20160809/780cb8d50dd6191359bc0f.png'

## 张瑞鹏 模仿 傅园慧 疑惑 99.9992729096 1.45418072167e-05 0.0 2477.0015691
a = str1
b = str4
print_result("", url2PointsList(a))
print_result("", url2PointsList(b))
like,v= Emotion.proc_diff(url2PointsList(a), url2PointsList(b))
print v
print like