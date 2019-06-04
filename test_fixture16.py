#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 22:13
# @Author  : Mannix
# @Site    : 
# @File    : test_fixture16.py
# @Software: PyCharm

import pytest

@pytest.fixture(scope='module', autouse=True)
def start(request):
    print('start')
    print('module : %s' % request.module.__name__)
    print('启动浏览器')
    yield
    print('结束测试 end!')

@pytest.fixture(scope='function', autouse=True)
def open_home(request):
    print('funciton: %s 回到首页' % request.function.__name__)

def test_01():
    print('test_01')

def test_02():
    print('test_02')

if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture16.py'])