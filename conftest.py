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

