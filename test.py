__author__ = 'voidhug'
import math
def exp(x):
    return (-2/(1+math.exp(-0.000856389122827*x))+2)*0.5+0.5

def get(y,x):
    y=(y-0.5)*2
    return -math.log(-2/(y-2)-1)/x


print get(0.91,425)
print exp(770)