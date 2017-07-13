#!/usr/bin/python
#coding:utf-8
import sys
import ctypes
class Conv(ctypes.Union):
    _fields_ = [("f", ctypes.c_float), ("u", ctypes.c_uint)]

def f2h(f):
    m = Conv()
    m.f = ctypes.c_float(f)
    return hex(m.u)

def h2f(u):
    m = Conv()
    m.u = ctypes.c_uint(u)
    return m.f

def conv(filename):
    fin = open(filename, "r")
    lines = fin.readlines()
    for i,l in enumerate(lines):
        print "%02d"%i,
        data = l.split()[1:]
        for n in data:
            print ("%3.4f"%h2f(int(n, 16))).rjust(10),
        print ""


if __name__ == "__main__":
    filename = sys.argv[-1]
    print filename
    conv(filename)
