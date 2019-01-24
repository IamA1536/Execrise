#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : move_array.py
# @Author: A
# @Date  : 2019/1/24
# @Contact : qq1694522669@gmail.com
from collections import deque

if __name__ == "__main__":
    a = [int(i) for i in input("Please input array:").split(" ")]
    m = int(input("Please input number:"))
    a = deque(a, maxlen=len(a))
    a.rotate(m)
    print(list(a))
