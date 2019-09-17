#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/4/11 14:26

@author: ZMJ

@file: test_02.py

'''

from selenium import webdriver
import time
import pytest

# 测试账号数据
test_user_data = ['admin1', 'admin2']

@pytest.fixture(scope='module')
def login(request):
    user = request.param
    print('登录账户：%s' %user)
    return user

@pytest.mark.parametrize('login', test_user_data, indirect=True)
def test_login(login):
    '''登录用例'''
    a = login
    print('测试用例中login的返回值为 %s' %a)
    assert a != ""


def test_yoyo_01(browser):
    browser.get("https://www.baidu.com")
    time.sleep(2)
    t = browser.title
    assert 'baidu' in t


if __name__ == '__main__':
    pytest.main(['-s', 'test_02.py'])