#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/3/19 20:09

@author: ZMJ

@file: conftest.py

'''

import pytest

@pytest.fixture()
def login():
    print('输入账号，密码先登录')

@pytest.fixture(scope='session')
def first1():
    print('score=session')
    a = 'yoyo'
    return a

