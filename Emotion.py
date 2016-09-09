#coding:utf-8
from random import randint
import numpy
import  math

def rand():
    return randint(0,30)


# example_data[12]=[1,1]
# example_data[16]=[1,1]
# example_data[14]=[3,3]
# #d1,2
# example_data[17]=[1,1]
# example_data[19]=[1,1]
# #d2,0
# example_data[24]=[1,1]
# example_data[28]=[3,3]
# #d3,-2
# example_data[26]=[5,5]
# example_data[22]=[3,3]
# #d4,2
# example_data[32]=[5,5]
# example_data[36]=[3,3]
# #d5,2
# example_data[34]=[5,5]
# example_data[30]=[3,3]
# #d6,2
# example_data[39]=[5,5]
# example_data[42]=[3,3]
# #d7,2
# example_data[4]=[5,5]
# example_data[3]=[3,3]
# #d8,2
# example_data[45]=[5,5]
# example_data[3]=[3,3]
# #d9,2根号2
# example_data[47]=[5,5]
# example_data[4]=[3,3]
# #d10,同上
# example_data[26]=[2,2]
# example_data[30]=[0,0]

# data[3]=[1,1]#pi/2
# data[38]=[1,2]#3pi/2
# data[39]=[1,1]#pi/4
# data[40]=[2,2]#3pi/4
# data[4]=[3,1]#7pi/4
# data[41]=[2,0]#5pi/4
# data[42]=[0,0.5]#0-pi/4

mouth=[4,39,40,41,5,42,43,4]
left_eye=[23,24,25,26,27,28,29,30,23]
right_eye=[31,32,33,34,35,36,37,38,31]
left_brow=[13,14,15,16,17,25,13]
right_brow=[18,19,20,21,22,33,18]
jaw=[6,8,10,12,11,9,7,6]#下巴
left_mouth=[4,46,45,4]
right_mouth=[5,48,47,5]

square={
    "right_eye":right_eye,
    "jaw":jaw,
    "left_mouth":left_mouth,
    "left_brow":left_brow,
    "left_eye":left_eye,
    "mouth":mouth,
    "right_brow":right_brow,
    "right_mouth":right_mouth,
    }
#
# wL = [
#     2,#right_eye
#     1,#jaw
#     1,#left_mouth
#     2,#left_brow
#     2,#left_eye
#     5,#mouth
#     2,#right_brow
#     1,#right_mouth
# ]

def process_compute_k(data):
    length = len(data)
    answer = []
    for i in range(length):
        k, theta = compute_k(data[i], data[(i+1)%length])
        x, y = data[i]
        answer += [[x, y, k, theta/numpy.pi]]

    return answer

def compute_k(point, _point):
    x, y = point
    _x, _y = _point
    delta_X = _x - x
    delta_Y = _y - y
    if delta_X == 0 and delta_Y >= 0:
        theta = numpy.pi/2
    elif delta_X ==0 and delta_Y < 0:
        theta = numpy.pi*3/2
    elif delta_X > 0 and delta_Y >= 0:
        theta = numpy.arctan(float(delta_Y)/delta_X)
    elif delta_X > 0 and delta_Y < 0:
        theta = numpy.arctan(float(delta_Y)/delta_X) + 2*numpy.pi
    else:
        theta = numpy.arctan(float(delta_Y)/delta_X) + numpy.pi

    return int(18*theta/numpy.pi), theta

def process_compute_l(data):
    length = len(data)
    answer = []
    for i in range(length):
        l = data[i][2] - data[(i + 1)%length][2]
        l = l if l >= 0 else l + 35
        answer.append(data[i] + [l])
    return answer

def process_data(square, data):
    answer = {}
    for k, v in square.items():
        _k = process_compute_k([data[x-1] for x in v])
        v = process_compute_l(_k)
        answer[k] = v
    return answer

# wT = [
#     2,
#     2,
#     1,
#     1,
#     5,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
# ]

def process_deforation(data):
    X, Y = [], []
    for x, y in data:
        X.append(float(x))
        Y.append(float(y))

    d = [
        abs(Y[14] - (Y[12] + Y[16])/2),#1
        abs(Y[19] - (Y[17] + Y[19])/2),#2
        Y[24] - Y[28],#3
        X[26] - X[22],#4
        Y[32] - Y[36],#5
        X[34] - X[30],#6
        Y[39] - Y[42],#7
        X[4] - X[3],#8
        numpy.sqrt((X[45] - X[3])**2 + (Y[45] - Y[3])**2 ),#9
        numpy.sqrt((X[47] - X[4])**2 + (Y[47] - Y[4])**2 ),#10
        (Y[22] + Y[26])/2 - Y[45],#11
        (Y[30] + Y[34])/2 - Y[47],#12
        abs(Y[11] - (Y[5] + Y[6])/2),#13
        numpy.sqrt((X[42] - X[11])**2 + (Y[42] - Y[11])**2 ),#14
        abs(Y[2]-Y[39]),#15
    ]

    for i in range(len(d)):
        d[i] = float(d[i])/numpy.sqrt((X[26] - X[30])**2 + (Y[26] - Y[30])**2)
    return d

def square_sum(L, W=None):
    sum = 0;
    if not W:
        for item in L :
            sum += item**2
    else :
        for l, w in zip(L, W):
            sum += l**2 * w
    return sum

def diff_L(IL, TL):
    d = []
    for I, T in zip(IL, TL):
        sum = 0
        for i, t in zip(I, T):
            sum += (i - t)**2/(i+t) if i+t != 0 else 0
        d.append(sum/2)
    return d

def diff_D(ID, TD):
    d = []
    for i, t in zip(ID, TD):
        v = (i-t)**2/(i+t) if (i+t) != 0 else 0
        d.append(v/2)
    return d

def diff(face_I, face_T, wL=None, wT=None):
    IL, ID = face_I
    TL, TD = face_T
    dL = diff_L(IL, TL)
    dD = diff_D(ID, TD)
    if not wL or not wT:
        return square_sum(dL) + square_sum(dD)
    else :
        return square_sum(dL, wL) + square_sum(dD, wT)

def drag_L(answer):
    L = []
    for k in answer.values():
        L.append([v[-1] for v in k])
    return L

def diff_percent(num):
    return 200/(1 + numpy.e**(-num)) - 100

def like_percent(num,count):
    if count==1:
        return (-2/(1 + math.exp(-0.000667826380186*num))+2)*0.5+0.5
    elif count==2:
        return (-2/(1 + math.exp(-0.000856389122827*num))+2)*0.5+0.5
    elif count==3:
        return (-2/(1 + math.exp(-0.000119528859508*num))+2)*0.5+0.5
    else:
        return (-2/(1+math.exp(-0.000230066610115*num))+2)*0.5+0.5

def proc_diff(data_I, data_L ,count,wL=None, wT=None, like=True):
    answer_I = process_data(square, data_I)
    answer_T = process_data(square, data_L)
    _v = diff(
        [drag_L(answer_I), process_deforation(data_I)],
        [drag_L(answer_T), process_deforation(data_L)],
        wL,
        wT
        )
    if like:
        return _v,like_percent(_v,count)
    else:
        return _v


