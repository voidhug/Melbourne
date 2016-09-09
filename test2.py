#!/usr/bin/env python
# coding: utf-8
import os


def IsSubString(SubStrList, Str):
    flag = True
    for substr in SubStrList:
        if not(substr in Str):
            flag = False
    return flag


def GetFileList(FindPath, FlagStr=[]):
    FileList = []
    FileNames = os.listdir(FindPath)
    if (len(FileNames) > 0):
        for fn in FileNames:
            if (len(FlagStr) > 0):
                if (IsSubString(FlagStr, fn)):
                    fullfilename = os.path.join(FindPath, fn)
                    FileList.append(fullfilename)
            else:
                fullfilename = os.path.join(FindPath, fn)
                FileList.append(fullfilename)
        if (len(FileList) > 0):
            FileList.sort()
    print FileList
    return FileList

GetFileList('/home/bluemit/Workplace/WeixinBot-master/news')
