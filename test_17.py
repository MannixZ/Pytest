#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 22:20
# @Author  : Mannix
# @Site    : 
# @File    : test_17.py
# @Software: PyCharm

import time
import pytest

@pytest.fixture(scope='module', autouse=True)
def start(request):
    print('start')
    print('module %s' % request.module.__name__)
    print('启动浏览器')
    yield
    print('结束测试 end!')

class Test_aaa():
    @pytest.fixture(scope='function', autouse=True)
    def open_home(self, request):
        print('function： %s' % request.function.__name__)

    def test_01(self):
        print('test_01')

    def test_02(self):
        print('test_02')

if __name__ == '__main__':
    pytest.main(['-s', 'test_17.py'])