# -*- coding: utf-8 -*-
import os


class Uper():
    def __init__(self, name):
        self.name = name

    def get(self):
        loads = 'cp ' + self.name
        loads += ' ../SybilPhotos'
        os.system(loads)
        os.chdir("../SybilPhotos")
        os.system("git pull origin master")
        os.system("git add .")
        os.system("git commit -m \"来了一个服务器\"")
        os.system("git push")
        return 'https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/' + self.name.split('/')[-1]

# https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/1.jpg
