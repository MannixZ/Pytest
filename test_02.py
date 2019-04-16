#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/4/11 14:26

@author: ZMJ

@file: test_02.py

'''

import pytest

# 测试账号数据
test_user_data = ['admin1', 'admin2']

@pytest.fixture(scope='module')
def login(request):
    user = request.param
    print('登录账户：%s' %user)
    return user

@pytest.mark.parametrize('login', test_user_data)