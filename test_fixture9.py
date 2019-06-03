#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 21:36
# @Author  : Mannix
# @Site    : 
# @File    : test_fixture9.py
# @Software: PyCharm

import pytest

@pytest.fixture(scope='class')
def first():
    print('scope 为class级别')
    a = 'yoyo'
    return a

class TestCase():
    def test_1(self, first):
        print('测试账号: %s' % first)
        assert first == 'yoyo'

    def test_2(self, first):
        print('test_2')
        assert first == 'yoyo'
    def test_3(self, first1):
        print('test_3')
        assert first1 == 'yoyo'

if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture9.py'])
