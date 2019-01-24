#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : yang_hui_triangle.py
# @Author: A
# @Date  : 2019/1/24
# @Contact : qq1694522669@gmail.com

def yh_triangle(a):
    for i in range(1, 11):
        for j in range(1, 11):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    pass


if __name__ == "__main__":
    a = []
    for i in range(11):
        a.append([])
        for j in range(11):
            a[i].append(0)
    for i in range(11):
        a[i][0] = 1
    yh_triangle(a)
    for i in range(10):
        print(a[i])
