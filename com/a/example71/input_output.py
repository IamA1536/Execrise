#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : input_output.py
# @Author: A
# @Date  : 2019/1/24
# @Contact : qq1694522669@gmail.com

def input_stu(n):
    print("Please input the information about students:")
    a = []
    for i in range(n):
        b = [[input("Please input the number:"), input("Please input the name:")]]
        a.append(b)

    return a


def output_stu(a):
    for i in a:
        print(i)


if __name__ == "__main__":
    n = int(input("Please input a number:"))
    output_stu(input_stu(n))
