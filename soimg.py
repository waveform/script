#!/usr/bin/python
#coding:utf-8
import sys 
import ctypes
from PIL import Image

def load(filename, size):
    buf_idx = 0
    buffer_type = ctypes.c_uint * size
    data = buffer_type()
    with open(filename, "r") as fin:
        lines = fin.readlines()
        for l in lines:
            if len(l) < 1: continue
            if l[0] == '#': continue
            tokens = l.split()[1:]
            for t in tokens:
                data[buf_idx] = int(t, 16)
                buf_idx = buf_idx + 1
            if buf_idx >= size: break
    return data

def conv(filename, width, height):
    size = width * height * 1
    data = load(filename, size)
    bmp_name = filename+".bmp" 
    im = Image.frombytes('RGBA', (width, height), data)
    im.save(bmp_name)
def conv8(filename, width, height):
    size = width * height / 4
    data_8 = load(filename, size)
    new_type = ctypes.c_uint * (size * 4)
    data = new_type()
    for i in xrange(size):
        data[4*i+0] = data_8[i] & 0x000000ff;
        data[4*i+1] = (data_8[i] & 0x0000ff00) >> 8;
        data[4*i+2] = (data_8[i] & 0x00ff0000) >> 16;
        data[4*i+3] = (data_8[i] & 0xff000000) >> 24;
    bmp_name = filename+".bmp"
    im = Image.frombytes('RGBA', (width, height), data)
    im.save(bmp_name)
def conv565(filename, width, height):
    size = width * height / 2
    data_565 = load(filename, size)
    new_type = ctypes.c_uint * (size * 2)
    data = new_type()
    for i in xrange(size):
        lo = i << 1
        hi = lo | 1
        data[lo] = 0xff000000;
        data[lo] |= (data_565[i] & 0x001f) << 3;
        data[lo] |= (data_565[i] & 0x07e0) << 5;
        data[lo] |= (data_565[i] & 0xf800) << 8;
        data[hi] = 0xff000000;
        data[hi] |= (data_565[i] & 0x001f0000) >> 13;
        data[hi] |= (data_565[i] & 0x07e00000) >> 11;
        data[hi] |= (data_565[i] & 0xf8000000) >> 8;
    bmp_name = filename+".bmp"
    im = Image.frombytes('RGBA', (width, height), data)
    im.save(bmp_name)
def conv888(filename, width, height):
    size = width * height * 3 / 4
    data = load(filename, size)
    bmp_name = filename+".bmp" 
    im = Image.frombytes('RGB', (width, height), data)
    im.save(bmp_name)
def help():
    doc = """ Usage: so_img.py data.file width height fmt(RGBA8|RGB8|RGB565|R8) """ 
    print doc


if __name__ == "__main__":
    if len(sys.argv) < 4:
        help()
        exit()
    filename = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    fmt = "RGBA8"
    if len(sys.argv) == 5: fmt = sys.argv[4]
    print filename
    func_tbl = {
        "RGBA8": conv, 
        "RGB565": conv565,
        "RGB8": conv888,
        "R8": conv8,
    }
    if fmt not in func_tbl:
        print "unknown fmt. please check supported fmt on doc."
    else:
        func_tbl[fmt](filename, width, height)
