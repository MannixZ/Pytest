#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/3/19 17:37

@author: ZMJ

@file: test_fixt.py

'''

import pytest

def setup_module():
    print('setup_moudle: 整个.py模块只会执行一次')

def teardown_module():
    print('teardown_moudle: 整个.py模块只会执行一次')

def setup_function():
    print('setup_funciton:每个用例开始前都会执行')

def teardown_function():
    print('teardown_function:每个用例结束后都会执行')

def test_one():
    print('正在执行----test_one')
    x = 'this'
    assert 'h' in x

def test_two():
    print('正在执行----test_two')
    x = 'hello'
    assert hasattr(x, 'check')

def test_three():
    print('正在执行----test_three')
    a = 'hello'
    b = 'hello world'
    assert a in b


class TestCase():

    def setup_class(self):
        print('setup_class: 所有用例执行之前')

    def teardown_class(self):
        print('teardown_class: 所有用例执行之后')

    def test_four(self):
        print('正在执行----test_four')
        x = 'hello'
        assert hasattr(x, 'check')

    def test_five(self):
        print('正在执行----test_five')
        a = 'hello'
        b = 'hello world'
        assert a in b


if __name__ == '__main__':
    pytest.main(['-s', 'test_fixt.py'])