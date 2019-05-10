#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/5/9/0009 20:39

@author: ZMJ

@file: test_03.py

'''

import pytest

test_user_data = [
    {'user':'hahaguai', 'psw':123},
    {'user':'admin', 'psw':''}
]

@pytest.fixture(scope='module')
def login(request):
    user = request.param['user']
    psw = request.param['psw']
    print('登录账户: %s' % user)
    print('登录密码: %s' % psw)
    if psw:
        return True
    else:
        return False

@pytest.mark.parametrize('login', test_user_data, indirect=True)
def test_login(login):
    '''登录用例'''
    a = login
    print('测试用例中login的返回值:%s' %a)
    assert a, '失败原因：密码为空'

if __name__ == '__main__':
    pytest.main(['-s', 'test_03.py'])