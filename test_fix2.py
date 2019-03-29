#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/3/19 21:17

@author: ZMJ

@file: test_fix2.py

'''

import pytest

def test_s4(login):
    print('用例4：登录之后其他动作4444')

def test_s5():
    print('用例5：不需要登录，操作555')

if __name__ == '__main__':
    pytest.main(['-s', 'test.fix2.py'])