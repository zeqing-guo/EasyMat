# -*- coding: utf-8 -*-
'''
Created on 2014年3月5日

@author: gzq
'''
def mimeTypeDict(type):
    mineType = {
                "eps": "application/postscript",
                "ps": "application/postscript",
                "pdf": "application/pdf",
                "tif": "image/tiff",
                "tiff": "image/tiff",
                "svg": "image/svg+xml",
                "jpg": "image/jpeg",
                "png": "image/png",
                }
    return mineType[type]
