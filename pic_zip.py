#coding:utf-8
from PIL import Image

#等比例压缩图片
def resizeImg(ori_img, dst_img, dst_w, dst_h):
    im = Image.open(ori_img)
    im.thumbnail((dst_w, dst_h))
    im.save(dst_img)

if __name__ == '__main__':
    resizeImg("1.jpg","1_.jpg", 800 , 800)
