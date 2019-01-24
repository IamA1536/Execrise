#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : change_array.py
# @Author: A
# @Date  : 2019/1/24
# @Contact : qq1694522669@gmail.com

if __name__ == "__main__":
    a = [int(i) for i in input().split(" ")]
    max_a = a[0]
    max_index = 0
    min_a = a[0]
    min_index = 0

    for i in range(len(a)):
        if a[i] > max_a:
            max_a = a[i]
            max_index = i
        if a[i] < min_a:
            min_a = a[i]
            min_index = i

    a[0], a[max_index] = a[max_index], a[0]
    a[-1], a[min_index] = a[min_index], a[-1]
    print(a)
