#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 21:59
# @Author  : Mannix
# @Site    : 
# @File    : test_13.py
# @Software: PyCharm

import time
import pytest

@pytest.fixture(scope='function')
def start(request):
    print('start')

def test_a(start):
    print('testcase a')

class Test_aaa():
    def test_01(self, start):
        print('test_01')

    def test_02(self, start):
        print('test_02')

if __name__ == '__main__':
    pytest.main(['-s', 'test_13.py'])