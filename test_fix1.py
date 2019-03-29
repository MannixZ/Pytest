#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/3/19 20:10

@author: ZMJ

@file: test_fix1.py

'''

import pytest

def test_s1(login):
    print('用例1：登录之后其他动作111')

def test_s2():
    print('用例2：不需要登录，操作222')

def test_s3(login):
    print('用例3：登录之后其他动作333')

if __name__ == '__main__':
    pytest.main(['-s', 'test_fix1.py'])