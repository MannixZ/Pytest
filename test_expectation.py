#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/3/20 17:00

@author: ZMJ

@file: test_expectation.py

'''

import pytest
@pytest.mark.parametrize('test_input,expected', [('3+5', 8),
                                                 ('2+4', 6),
                                                 pytest.param('6*9', 27, marks=pytest.mark.xfail),])
def test_eval(test_input, expected):
    print('-----开始用例-----')
    assert eval(test_input) == expected

@pytest.mark.parametrize('x', [0, 1, 2])
@pytest.mark.parametrize('y', [3, 4, 5])
def test_foo(x,y):
    print('测试数据组合：x->%s, y->%s' %(x, y))


if __name__ == '__main__':
    pytest.main(['-s', 'test_expectation.py'])