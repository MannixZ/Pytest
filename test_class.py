#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/3/19 12:28

@author: ZMJ

@file: test_class.py

'''

import pytest

class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'hello')

    def test_three(self):
        a = 'hello'
        b = 'hello world'
        assert a in b

if __name__ == '__main__':
    pytest.main(['-q', 'test_class.py'])