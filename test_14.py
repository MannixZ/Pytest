#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 22:04
# @Author  : Mannix
# @Site    : 
# @File    : test_14.py
# @Software: PyCharm

import time
import pytest

@pytest.fixture(scope='function')
def start(request):
    print('start')

@pytest.mark.usefixtures('start')
def test_a():
    print('test_a')

@pytest.mark.usefixtures('start')
class Test_aaa():

    def test_01(self):
        print('test_01')

    def test_02(self):
        print('test_02')

if __name__ == '__main__':
    pytest.main(['-s', 'test_14.py'])