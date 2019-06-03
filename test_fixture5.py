#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 21:18
# @Author  : Mannix
# @Site    : 
# @File    : test_fixture5.py
# @Software: PyCharm

import pytest

@pytest.fixture()
def user():
    print('获取用户名')
    a = 'yoyo'
    return a

@pytest.fixture()
def psw():
    print('获取密码')
    b = '123456'
    return b

def test_1(user, psw):
    print('user: %s, psw: %s' %(user, psw))
    assert user == 'yoyo'

if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture5.py'])