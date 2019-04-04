#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/4/3 10:49

@author: ZMJ

@file: test_assert1.py.py

'''
import pytest

def f():
    return 3

def test_function():
    a = f()
    assert a % 2 == 0, '判断a为偶数，当前a的值为：%s' %a

def test_zero_divison():
    '''断言异常'''
    with pytest.raises(ZeroDivisionError) as excifo:
        1 / 0

    # 断言异常类型type
    assert excifo.type == ZeroDivisionError
    # 断言异常value值
    assert 'division by zero' in str(excifo.value)
