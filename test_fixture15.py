#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 22:08
# @Author  : Mannix
# @Site    : 
# @File    : test_fixture15.py
# @Software: PyCharm

import pytest

@pytest.fixture(scope='module')
def first():
    print('first')

@pytest.fixture(scope='module')
def sencond():
    print('sencond')

@pytest.mark.usefixtures('sencond')
@pytest.mark.usefixtures('first')
class TestFix():
    def test_1(self):
        print('test_1')
        assert 1 == 1

    def test_2(self):
        print('test_2')
        assert 2 == 1

if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture15.py'])