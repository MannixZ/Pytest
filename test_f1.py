#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/3/20 16:48

@author: ZMJ

@file: test_f1.py

'''

import pytest

@pytest.fixture(scope="module")
def open():
    print('打开浏览器，并且打开百度首页')

    yield
    print('执行teardown')
    print('关闭浏览器')

def test_s1(open):
    print('用例1：搜索python-1')

    raise NameError

def test_s2(open):
    print('用例2：搜索python-2')

def test_s3(open):
    print('用例3：搜索Python-3')

if __name__ == '__main__':
    pytest.main(['-s', 'test_f1.py'])