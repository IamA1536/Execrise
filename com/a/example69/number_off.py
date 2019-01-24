#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : number_off.py
# @Author: A
# @Date  : 2019/1/24
# @Contact : qq1694522669@gmail.com

if __name__ == "__main__":
    n = int(input("please input a number:"))
    a = []
    for i in range(n):
        a.append(1)
    c = 0
    l = 0
    total = len(a)
    while total != 1:
        if a[l] == 1:
            c += 1

        if c == 3:
            a[l] = 0
            total -= 1
            c = 0
        if l < len(a) - 1:
            l += 1
        else:
            l = 0

    for i in range(len(a)):
        if a[i] == 1:
            print(i + 1)
            break
