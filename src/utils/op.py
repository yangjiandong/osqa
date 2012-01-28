#!/usr/bin/envs python
#-*- coding: utf-8 -*-#

#http://www.vimer.cn/2012/01/%E6%9C%80%E8%BF%91%E7%9A%84%E4%B8%80%E4%BA%9B%E6%8A%80%E6%9C%AF%E6%95%B4%E7%90%8620120109.html
def get_image_type(pd, is_path=True):
    """
    获取图片的类型，支持传入路径和文件内容
    """
    if is_path:
        f = file(pd, 'rb')
        data = f.read(10).encode('hex')
    else:
        data = pd.encode('hex')

    ftype = None

    if data.startswith('ffd8'):
        ftype = 'jpeg'
    if data.startswith('424d'):
        ftype = 'bmp'
    if data.startswith('474946'):
        ftype = 'git'
    elif data.startswith('89504e470d0a1a0a'):
        ftype = 'png'

    return ftype


